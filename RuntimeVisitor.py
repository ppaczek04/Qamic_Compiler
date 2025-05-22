from antlr4 import *
from gen.YoScriptVisitor import YoScriptVisitor

class ReturnSignal(Exception):
    def __init__(self, value, line):
        super().__init__(value)
        self.value = value
        self.line = line

class BreakSignal(Exception):
    def __init__(self, line):
        super().__init__(f"Break at line {line}")
        self.line = line

class RuntimeVisitor(YoScriptVisitor):

    def __init__(self):
        self.env_stack = [{}]
        self.functions = {}

    @property
    def current_env(self):
        return self.env_stack[-1]

    def visitProgram(self, ctx):
        try:
            return self.visit(ctx.statements())
        except BreakSignal as e:
            # break poza pętlą
            raise RuntimeError(f"'nahh' used outside the loop at line {e.line}")
        except ReturnSignal as e:
            # return poza funkcją
            raise RuntimeError(f"'goback' used outside the function at line {e.line}")

    def visitStatements(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()

        value = self.visit(ctx.expression())
        self.current_env[name] = value
        return value

    def visitExpression_stmt(self, ctx):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx):
        return self.visit(ctx.comparison())

    def visitComparison(self, ctx):
        left = self.visit(ctx.arithmetic(0))
        ops = [t.getText() for t in ctx.EQEQUAL()] + [t.getText() for t in ctx.NOTEQUAL()]
        rhs = ctx.arithmetic()[1:]

        for op, subctx in zip(ops, rhs):
            right = self.visit(subctx)
            if op == '==':
                left = (left == right)
            else:  # op == '!='
                left = (left != right)
        return left

    def visitArithmetic(self, ctx):
        left = self.visit(ctx.term(0))
        ops = [t.getText() for t in ctx.PLUS()] + [t.getText() for t in ctx.MINUS()]
        rhs = ctx.term()[1:]

        for op, subctx in zip(ops, rhs):
            right = self.visit(subctx)
            if op == '+':
                left += right
            else:  # op == '-'
                left -= right
        return left

    def visitTerm(self, ctx):
        left = self.visit(ctx.factor(0))
        ops = [t.getText() for t in ctx.STAR()] + [t.getText() for t in ctx.SLASH()]
        rhs = ctx.factor()[1:]

        for op, subctx in zip(ops, rhs):
            right = self.visit(subctx)
            if op == '*':
                left *= right
            else:  # op == '/'
                if right == 0:
                    line = ctx.start.line
                    # Dzielenie przez 0
                    raise RuntimeError(f"Division by zero at line {line}")
                left /= right
        return left

    def visitFactor(self, ctx):
        if ctx.PLUS():
            return +self.visit(ctx.factor(0))
        if ctx.MINUS():
            return -self.visit(ctx.factor(0))
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            for env in reversed(self.env_stack):
                if name in env:
                    return env[name]
            # Sprawdzamy czy zmienna była wcześniej zdefiniowana
            raise NameError(f"Variable '{name}' not defined")
        else:
            return self.visit(ctx.expression())

    def visitList_literal(self, ctx):
        return [self.visit(e) for e in ctx.expression()]

    def visitIf_stmt(self, ctx):
        # lista wszystkich warunków i bloków
        cond_parens = ctx.cond_paren()
        blocks = ctx.block()
        line0 = cond_parens[0].start.line

        # 1) if
        cond0 = self.visit(cond_parens[0].expression())
        if not isinstance(cond0, bool):
            raise RuntimeError(f"If condition must be boolean at line {line0}")
        if cond0:
            return self.visit(blocks[0].statements())

        # 2) elif
        for i in range(1, len(cond_parens)):
            line_i = cond_parens[i].start.line
            cond_i = self.visit(cond_parens[i].expression())
            if not isinstance(cond_i, bool):
                raise RuntimeError(f"If condition must be boolean at line {line_i}")
            if cond_i:
                return self.visit(blocks[i].statements())

        # 3) else
        if ctx.IDK():
            return self.visit(blocks[-1].statements())

    def visitBreak_stmt(self, ctx):
        line = ctx.start.line
        raise BreakSignal(line)

    def visitReturn_stmt(self, ctx):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        line = ctx.start.line
        raise ReturnSignal(val, line)

    def visitFor_stmt(self, ctx):
        iterable = self.visit(ctx.expression())
        var = ctx.IDENTIFIER().getText()

        for val in iterable:
            self.current_env[var] = val
            try:
                self.visit(ctx.block().statements())
            except BreakSignal:
                break

    def visitFunc_def(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = [p.getText() for p in ctx.param_list().IDENTIFIER()] if ctx.param_list() else []

        self.functions[name] = (params, ctx.block().statements())

    def visitFunction_call(self, ctx):
        name = ctx.IDENTIFIER().getText()
        args = [self.visit(arg) for arg in ctx.arg_list().expression()] if ctx.arg_list() else []

        if name == 'print':
            print(*args)
            return None

        if name in self.functions:
            params, body = self.functions[name]
            # Sprawdzamy czy liczba argumentów się zgadza
            if len(args) != len(params):
                raise RuntimeError(f"Function '{name}' expects {len(params)} args, got {len(args)}")

            local_env = dict(zip(params, args))
            self.env_stack.append(local_env)
            try:
                self.visit(body)
            except ReturnSignal as r:
                result = r.value
            else:
                result = None
            self.env_stack.pop()
            return result
        # Sprawdzamy czy funkcja była wcześniej zdefiniowana
        else:
            raise RuntimeError(f"Function '{name}' not defined")
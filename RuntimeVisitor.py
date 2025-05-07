from antlr4 import *
from gen.YoScriptVisitor import YoScriptVisitor

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class BreakSignal(Exception):
    pass

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
        except BreakSignal:
            # break poza pętlą
            raise RuntimeError("‘nahh’ used outside the loop")

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
                left /= right
        return left

    def visitFactor(self, ctx):
        if ctx.PLUS():
            return +self.visit(ctx.factor(0))
        if ctx.MINUS():
            return -self.visit(ctx.factor(0))
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            for env in reversed(self.env_stack):
                if name in env:
                    return env[name]
            raise NameError(f"Variable '{name}' not defined")
        elif ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return self.visit(ctx.expression())

    def visitList_literal(self, ctx):
        return [self.visit(e) for e in ctx.expression()]

    def visitIf_stmt(self, ctx):
        cond = self.visit(ctx.cond_paren().expression())
        if cond:
            self.visit(ctx.block(0).statements())
        elif len(ctx.block()) > 1:
            self.visit(ctx.block(1).statements())

    def visitBreak_stmt(self, ctx):
        raise BreakSignal()

    def visitReturn_stmt(self, ctx):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        raise ReturnSignal(val)

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
        else:
            raise Exception(f"Function '{name}' not defined")

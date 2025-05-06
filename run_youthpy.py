# run_youthpy.py

from antlr4 import *
from gen.YoScriptLexer import YoScriptLexer
from gen.YoScriptParser import YoScriptParser
from gen.YoScriptVisitor import YoScriptVisitor

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class BreakSignal(Exception):
    pass

class RuntimeVisitor(YoScriptVisitor):
    def __init__(self):
        self.globals = {}
        self.functions = {}

    def visitProgram(self, ctx):
        return self.visit(ctx.statements())

    def visitStatements(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.globals[name] = value
        return value

    def visitExpression_stmt(self, ctx):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx):
        return self.visit(ctx.comparison())
    
    def visitComparison(self, ctx):
        left = self.visit(ctx.arithmetic(0))
        for i in range(1, len(ctx.arithmetic())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.arithmetic(i))
            if op == '==':
                left = float(left == right)
            elif op == '!=':
                left = float(left != right)
        return left

    def visitTerm(self, ctx):
        left = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))
            if op == '*':
                left *= right
            elif op == '/':
                left /= right
        return left

    def visitFactor(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.factor())
            return +val if op == '+' else -val
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.globals.get(name, None)
        elif ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return self.visit(ctx.expression())

    def visitList_literal(self, ctx):
        return [self.visit(e) for e in ctx.expression()]

    def visitIf_stmt(self, ctx):
        cond = self.visit(ctx.cond_block().expression())
        if cond:
            self.visit(ctx.cond_block().statements())
        elif ctx.alt_block():
            self.visit(ctx.alt_block().statements())

    def visitBreak_stmt(self, ctx):
        raise BreakSignal()

    def visitReturn_stmt(self, ctx):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        raise ReturnSignal(val)

    def visitFor_stmt(self, ctx):
        iterable = self.visit(ctx.expression())
        var = ctx.IDENTIFIER().getText()
        for val in iterable:
            self.globals[var] = val
            try:
                self.visit(ctx.statements())
            except BreakSignal:
                break

    def visitFunc_def(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = [p.getText() for p in ctx.param_list().IDENTIFIER()] if ctx.param_list() else []
        self.functions[name] = (params, ctx.statements())

    def visitFunction_call(self, ctx):
        name = ctx.IDENTIFIER().getText()
        args = [self.visit(arg) for arg in ctx.arg_list().expression()] if ctx.arg_list() else []

        if name == 'print':
            print(*args)
            return None

        if name in self.functions:
            params, body = self.functions[name]
            backup = self.globals.copy()
            self.globals.update(dict(zip(params, args)))
            try:
                self.visit(body)
            except ReturnSignal as r:
                result = r.value
            else:
                result = None
            self.globals = backup
            return result
        else:
            raise Exception(f"Function '{name}' not defined")

def run_file(filename):
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = YoScriptLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = YoScriptParser(tokens)
    tree = parser.program()
    RuntimeVisitor().visit(tree)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run_youthpy.py <file.youthpy>")
    else:
        run_file(sys.argv[1])

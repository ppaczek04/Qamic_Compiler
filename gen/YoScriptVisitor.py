# Generated from YoScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .YoScriptParser import YoScriptParser
else:
    from YoScriptParser import YoScriptParser

# This class defines a complete generic visitor for a parse tree produced by YoScriptParser.

class YoScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YoScriptParser#program.
    def visitProgram(self, ctx:YoScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#statements.
    def visitStatements(self, ctx:YoScriptParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#statement.
    def visitStatement(self, ctx:YoScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#expression_stmt.
    def visitExpression_stmt(self, ctx:YoScriptParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#assignment.
    def visitAssignment(self, ctx:YoScriptParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#if_stmt.
    def visitIf_stmt(self, ctx:YoScriptParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#cond_block.
    def visitCond_block(self, ctx:YoScriptParser.Cond_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#alt_block.
    def visitAlt_block(self, ctx:YoScriptParser.Alt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#break_stmt.
    def visitBreak_stmt(self, ctx:YoScriptParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#return_stmt.
    def visitReturn_stmt(self, ctx:YoScriptParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#for_stmt.
    def visitFor_stmt(self, ctx:YoScriptParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#func_def.
    def visitFunc_def(self, ctx:YoScriptParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#param_list.
    def visitParam_list(self, ctx:YoScriptParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#expression.
    def visitExpression(self, ctx:YoScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#term.
    def visitTerm(self, ctx:YoScriptParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#factor.
    def visitFactor(self, ctx:YoScriptParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#atom.
    def visitAtom(self, ctx:YoScriptParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#list_literal.
    def visitList_literal(self, ctx:YoScriptParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#function_call.
    def visitFunction_call(self, ctx:YoScriptParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#arg_list.
    def visitArg_list(self, ctx:YoScriptParser.Arg_listContext):
        return self.visitChildren(ctx)



del YoScriptParser
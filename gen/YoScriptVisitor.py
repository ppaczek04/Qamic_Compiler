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


    # Visit a parse tree produced by YoScriptParser#expression_statement.
    def visitExpression_statement(self, ctx:YoScriptParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#assignment_statement.
    def visitAssignment_statement(self, ctx:YoScriptParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#reassignment_statement.
    def visitReassignment_statement(self, ctx:YoScriptParser.Reassignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#if_statement.
    def visitIf_statement(self, ctx:YoScriptParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#while_statement.
    def visitWhile_statement(self, ctx:YoScriptParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#for_statement.
    def visitFor_statement(self, ctx:YoScriptParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#function_definition.
    def visitFunction_definition(self, ctx:YoScriptParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#typed_parameters.
    def visitTyped_parameters(self, ctx:YoScriptParser.Typed_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#typed_parameter.
    def visitTyped_parameter(self, ctx:YoScriptParser.Typed_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#return_statement.
    def visitReturn_statement(self, ctx:YoScriptParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#expression_list.
    def visitExpression_list(self, ctx:YoScriptParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#expression.
    def visitExpression(self, ctx:YoScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#operator.
    def visitOperator(self, ctx:YoScriptParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#primary.
    def visitPrimary(self, ctx:YoScriptParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#function_call.
    def visitFunction_call(self, ctx:YoScriptParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YoScriptParser#type.
    def visitType(self, ctx:YoScriptParser.TypeContext):
        return self.visitChildren(ctx)



del YoScriptParser
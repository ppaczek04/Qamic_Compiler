# Generated from YoScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .YoScriptParser import YoScriptParser
else:
    from YoScriptParser import YoScriptParser

# This class defines a complete listener for a parse tree produced by YoScriptParser.
class YoScriptListener(ParseTreeListener):

    # Enter a parse tree produced by YoScriptParser#program.
    def enterProgram(self, ctx:YoScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by YoScriptParser#program.
    def exitProgram(self, ctx:YoScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by YoScriptParser#statements.
    def enterStatements(self, ctx:YoScriptParser.StatementsContext):
        pass

    # Exit a parse tree produced by YoScriptParser#statements.
    def exitStatements(self, ctx:YoScriptParser.StatementsContext):
        pass


    # Enter a parse tree produced by YoScriptParser#statement.
    def enterStatement(self, ctx:YoScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#statement.
    def exitStatement(self, ctx:YoScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#expression_statement.
    def enterExpression_statement(self, ctx:YoScriptParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#expression_statement.
    def exitExpression_statement(self, ctx:YoScriptParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#assignment_statement.
    def enterAssignment_statement(self, ctx:YoScriptParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#assignment_statement.
    def exitAssignment_statement(self, ctx:YoScriptParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#reassignment_statement.
    def enterReassignment_statement(self, ctx:YoScriptParser.Reassignment_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#reassignment_statement.
    def exitReassignment_statement(self, ctx:YoScriptParser.Reassignment_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#if_statement.
    def enterIf_statement(self, ctx:YoScriptParser.If_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#if_statement.
    def exitIf_statement(self, ctx:YoScriptParser.If_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#while_statement.
    def enterWhile_statement(self, ctx:YoScriptParser.While_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#while_statement.
    def exitWhile_statement(self, ctx:YoScriptParser.While_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#for_statement.
    def enterFor_statement(self, ctx:YoScriptParser.For_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#for_statement.
    def exitFor_statement(self, ctx:YoScriptParser.For_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#function_definition.
    def enterFunction_definition(self, ctx:YoScriptParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by YoScriptParser#function_definition.
    def exitFunction_definition(self, ctx:YoScriptParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by YoScriptParser#typed_parameters.
    def enterTyped_parameters(self, ctx:YoScriptParser.Typed_parametersContext):
        pass

    # Exit a parse tree produced by YoScriptParser#typed_parameters.
    def exitTyped_parameters(self, ctx:YoScriptParser.Typed_parametersContext):
        pass


    # Enter a parse tree produced by YoScriptParser#typed_parameter.
    def enterTyped_parameter(self, ctx:YoScriptParser.Typed_parameterContext):
        pass

    # Exit a parse tree produced by YoScriptParser#typed_parameter.
    def exitTyped_parameter(self, ctx:YoScriptParser.Typed_parameterContext):
        pass


    # Enter a parse tree produced by YoScriptParser#return_statement.
    def enterReturn_statement(self, ctx:YoScriptParser.Return_statementContext):
        pass

    # Exit a parse tree produced by YoScriptParser#return_statement.
    def exitReturn_statement(self, ctx:YoScriptParser.Return_statementContext):
        pass


    # Enter a parse tree produced by YoScriptParser#expression_list.
    def enterExpression_list(self, ctx:YoScriptParser.Expression_listContext):
        pass

    # Exit a parse tree produced by YoScriptParser#expression_list.
    def exitExpression_list(self, ctx:YoScriptParser.Expression_listContext):
        pass


    # Enter a parse tree produced by YoScriptParser#expression.
    def enterExpression(self, ctx:YoScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by YoScriptParser#expression.
    def exitExpression(self, ctx:YoScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by YoScriptParser#operator.
    def enterOperator(self, ctx:YoScriptParser.OperatorContext):
        pass

    # Exit a parse tree produced by YoScriptParser#operator.
    def exitOperator(self, ctx:YoScriptParser.OperatorContext):
        pass


    # Enter a parse tree produced by YoScriptParser#primary.
    def enterPrimary(self, ctx:YoScriptParser.PrimaryContext):
        pass

    # Exit a parse tree produced by YoScriptParser#primary.
    def exitPrimary(self, ctx:YoScriptParser.PrimaryContext):
        pass


    # Enter a parse tree produced by YoScriptParser#function_call.
    def enterFunction_call(self, ctx:YoScriptParser.Function_callContext):
        pass

    # Exit a parse tree produced by YoScriptParser#function_call.
    def exitFunction_call(self, ctx:YoScriptParser.Function_callContext):
        pass


    # Enter a parse tree produced by YoScriptParser#type.
    def enterType(self, ctx:YoScriptParser.TypeContext):
        pass

    # Exit a parse tree produced by YoScriptParser#type.
    def exitType(self, ctx:YoScriptParser.TypeContext):
        pass



del YoScriptParser
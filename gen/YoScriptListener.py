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


    # Enter a parse tree produced by YoScriptParser#expression_stmt.
    def enterExpression_stmt(self, ctx:YoScriptParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by YoScriptParser#expression_stmt.
    def exitExpression_stmt(self, ctx:YoScriptParser.Expression_stmtContext):
        pass


    # Enter a parse tree produced by YoScriptParser#assignment.
    def enterAssignment(self, ctx:YoScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YoScriptParser#assignment.
    def exitAssignment(self, ctx:YoScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YoScriptParser#if_stmt.
    def enterIf_stmt(self, ctx:YoScriptParser.If_stmtContext):
        pass

    # Exit a parse tree produced by YoScriptParser#if_stmt.
    def exitIf_stmt(self, ctx:YoScriptParser.If_stmtContext):
        pass


    # Enter a parse tree produced by YoScriptParser#cond_block.
    def enterCond_block(self, ctx:YoScriptParser.Cond_blockContext):
        pass

    # Exit a parse tree produced by YoScriptParser#cond_block.
    def exitCond_block(self, ctx:YoScriptParser.Cond_blockContext):
        pass


    # Enter a parse tree produced by YoScriptParser#alt_block.
    def enterAlt_block(self, ctx:YoScriptParser.Alt_blockContext):
        pass

    # Exit a parse tree produced by YoScriptParser#alt_block.
    def exitAlt_block(self, ctx:YoScriptParser.Alt_blockContext):
        pass


    # Enter a parse tree produced by YoScriptParser#break_stmt.
    def enterBreak_stmt(self, ctx:YoScriptParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by YoScriptParser#break_stmt.
    def exitBreak_stmt(self, ctx:YoScriptParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by YoScriptParser#return_stmt.
    def enterReturn_stmt(self, ctx:YoScriptParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by YoScriptParser#return_stmt.
    def exitReturn_stmt(self, ctx:YoScriptParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by YoScriptParser#for_stmt.
    def enterFor_stmt(self, ctx:YoScriptParser.For_stmtContext):
        pass

    # Exit a parse tree produced by YoScriptParser#for_stmt.
    def exitFor_stmt(self, ctx:YoScriptParser.For_stmtContext):
        pass


    # Enter a parse tree produced by YoScriptParser#func_def.
    def enterFunc_def(self, ctx:YoScriptParser.Func_defContext):
        pass

    # Exit a parse tree produced by YoScriptParser#func_def.
    def exitFunc_def(self, ctx:YoScriptParser.Func_defContext):
        pass


    # Enter a parse tree produced by YoScriptParser#param_list.
    def enterParam_list(self, ctx:YoScriptParser.Param_listContext):
        pass

    # Exit a parse tree produced by YoScriptParser#param_list.
    def exitParam_list(self, ctx:YoScriptParser.Param_listContext):
        pass


    # Enter a parse tree produced by YoScriptParser#expression.
    def enterExpression(self, ctx:YoScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by YoScriptParser#expression.
    def exitExpression(self, ctx:YoScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by YoScriptParser#comparison.
    def enterComparison(self, ctx:YoScriptParser.ComparisonContext):
        pass

    # Exit a parse tree produced by YoScriptParser#comparison.
    def exitComparison(self, ctx:YoScriptParser.ComparisonContext):
        pass


    # Enter a parse tree produced by YoScriptParser#arithmetic.
    def enterArithmetic(self, ctx:YoScriptParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by YoScriptParser#arithmetic.
    def exitArithmetic(self, ctx:YoScriptParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by YoScriptParser#term.
    def enterTerm(self, ctx:YoScriptParser.TermContext):
        pass

    # Exit a parse tree produced by YoScriptParser#term.
    def exitTerm(self, ctx:YoScriptParser.TermContext):
        pass


    # Enter a parse tree produced by YoScriptParser#factor.
    def enterFactor(self, ctx:YoScriptParser.FactorContext):
        pass

    # Exit a parse tree produced by YoScriptParser#factor.
    def exitFactor(self, ctx:YoScriptParser.FactorContext):
        pass


    # Enter a parse tree produced by YoScriptParser#atom.
    def enterAtom(self, ctx:YoScriptParser.AtomContext):
        pass

    # Exit a parse tree produced by YoScriptParser#atom.
    def exitAtom(self, ctx:YoScriptParser.AtomContext):
        pass


    # Enter a parse tree produced by YoScriptParser#list_literal.
    def enterList_literal(self, ctx:YoScriptParser.List_literalContext):
        pass

    # Exit a parse tree produced by YoScriptParser#list_literal.
    def exitList_literal(self, ctx:YoScriptParser.List_literalContext):
        pass


    # Enter a parse tree produced by YoScriptParser#function_call.
    def enterFunction_call(self, ctx:YoScriptParser.Function_callContext):
        pass

    # Exit a parse tree produced by YoScriptParser#function_call.
    def exitFunction_call(self, ctx:YoScriptParser.Function_callContext):
        pass


    # Enter a parse tree produced by YoScriptParser#arg_list.
    def enterArg_list(self, ctx:YoScriptParser.Arg_listContext):
        pass

    # Exit a parse tree produced by YoScriptParser#arg_list.
    def exitArg_list(self, ctx:YoScriptParser.Arg_listContext):
        pass



del YoScriptParser
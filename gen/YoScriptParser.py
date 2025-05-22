# Generated from C:/Studia/Kompilatory_projekt/YoScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,253,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,1,
        1,4,1,56,8,1,11,1,12,1,57,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,5,
        1,67,8,1,10,1,12,1,70,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,79,8,2,
        1,3,1,3,3,3,83,8,3,1,4,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,5,5,93,8,5,
        10,5,12,5,96,9,5,1,5,1,5,5,5,100,8,5,10,5,12,5,103,9,5,1,5,1,5,1,
        6,1,6,1,6,3,6,110,8,6,1,6,1,6,3,6,114,8,6,1,6,1,6,1,6,3,6,119,8,
        6,1,6,1,6,5,6,123,8,6,10,6,12,6,126,9,6,1,6,3,6,129,8,6,1,6,1,6,
        3,6,133,8,6,1,6,3,6,136,8,6,1,7,1,7,1,7,1,7,1,8,1,8,3,8,144,8,8,
        1,9,1,9,3,9,148,8,9,1,9,3,9,151,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,3,11,163,8,11,1,11,1,11,3,11,167,8,11,1,11,1,
        11,3,11,171,8,11,1,12,1,12,1,12,5,12,176,8,12,10,12,12,12,179,9,
        12,1,13,1,13,1,14,1,14,1,14,5,14,186,8,14,10,14,12,14,189,9,14,1,
        15,1,15,1,15,5,15,194,8,15,10,15,12,15,197,9,15,1,16,1,16,1,16,5,
        16,202,8,16,10,16,12,16,205,9,16,1,17,1,17,1,17,3,17,210,8,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,223,8,
        18,1,19,1,19,1,19,1,19,5,19,229,8,19,10,19,12,19,232,9,19,3,19,234,
        8,19,1,19,1,19,1,20,1,20,1,20,3,20,241,8,20,1,20,1,20,1,21,1,21,
        1,21,5,21,248,8,21,10,21,12,21,251,9,21,1,21,0,0,22,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,3,1,0,17,18,1,
        0,13,14,1,0,15,16,273,0,44,1,0,0,0,2,50,1,0,0,0,4,78,1,0,0,0,6,80,
        1,0,0,0,8,84,1,0,0,0,10,90,1,0,0,0,12,106,1,0,0,0,14,137,1,0,0,0,
        16,141,1,0,0,0,18,145,1,0,0,0,20,152,1,0,0,0,22,158,1,0,0,0,24,172,
        1,0,0,0,26,180,1,0,0,0,28,182,1,0,0,0,30,190,1,0,0,0,32,198,1,0,
        0,0,34,209,1,0,0,0,36,222,1,0,0,0,38,224,1,0,0,0,40,237,1,0,0,0,
        42,244,1,0,0,0,44,45,3,2,1,0,45,46,5,0,0,1,46,1,1,0,0,0,47,49,5,
        34,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,
        53,1,0,0,0,52,50,1,0,0,0,53,62,3,4,2,0,54,56,5,34,0,0,55,54,1,0,
        0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,61,
        3,4,2,0,60,55,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,68,1,0,0,0,64,62,1,0,0,0,65,67,5,34,0,0,66,65,1,0,0,0,67,70,1,
        0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,68,1,0,0,0,71,
        79,3,6,3,0,72,79,3,8,4,0,73,79,3,12,6,0,74,79,3,20,10,0,75,79,3,
        16,8,0,76,79,3,18,9,0,77,79,3,22,11,0,78,71,1,0,0,0,78,72,1,0,0,
        0,78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,
        1,0,0,0,79,5,1,0,0,0,80,82,3,26,13,0,81,83,5,34,0,0,82,81,1,0,0,
        0,82,83,1,0,0,0,83,7,1,0,0,0,84,85,5,33,0,0,85,86,5,19,0,0,86,88,
        3,26,13,0,87,89,5,34,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,9,1,0,0,
        0,90,94,5,22,0,0,91,93,5,34,0,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,101,3,2,1,0,
        98,100,5,34,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,23,0,0,105,
        11,1,0,0,0,106,107,5,7,0,0,107,109,3,14,7,0,108,110,5,34,0,0,109,
        108,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,124,3,10,5,0,112,
        114,5,34,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,
        116,5,8,0,0,116,118,3,14,7,0,117,119,5,34,0,0,118,117,1,0,0,0,118,
        119,1,0,0,0,119,120,1,0,0,0,120,121,3,10,5,0,121,123,1,0,0,0,122,
        113,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,
        135,1,0,0,0,126,124,1,0,0,0,127,129,5,34,0,0,128,127,1,0,0,0,128,
        129,1,0,0,0,129,130,1,0,0,0,130,132,5,9,0,0,131,133,5,34,0,0,132,
        131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,136,3,10,5,0,135,
        128,1,0,0,0,135,136,1,0,0,0,136,13,1,0,0,0,137,138,5,20,0,0,138,
        139,3,26,13,0,139,140,5,21,0,0,140,15,1,0,0,0,141,143,5,10,0,0,142,
        144,5,34,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,17,1,0,0,0,145,
        147,5,11,0,0,146,148,3,26,13,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        150,1,0,0,0,149,151,5,34,0,0,150,149,1,0,0,0,150,151,1,0,0,0,151,
        19,1,0,0,0,152,153,5,6,0,0,153,154,5,33,0,0,154,155,5,12,0,0,155,
        156,3,26,13,0,156,157,3,10,5,0,157,21,1,0,0,0,158,159,5,5,0,0,159,
        160,5,33,0,0,160,162,5,20,0,0,161,163,3,24,12,0,162,161,1,0,0,0,
        162,163,1,0,0,0,163,164,1,0,0,0,164,166,5,21,0,0,165,167,5,34,0,
        0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,170,3,10,5,
        0,169,171,5,34,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,23,1,0,0,
        0,172,177,5,33,0,0,173,174,5,26,0,0,174,176,5,33,0,0,175,173,1,0,
        0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,25,1,0,0,
        0,179,177,1,0,0,0,180,181,3,28,14,0,181,27,1,0,0,0,182,187,3,30,
        15,0,183,184,7,0,0,0,184,186,3,30,15,0,185,183,1,0,0,0,186,189,1,
        0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,29,1,0,0,0,189,187,1,0,
        0,0,190,195,3,32,16,0,191,192,7,1,0,0,192,194,3,32,16,0,193,191,
        1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,31,1,
        0,0,0,197,195,1,0,0,0,198,203,3,34,17,0,199,200,7,2,0,0,200,202,
        3,34,17,0,201,199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,
        1,0,0,0,204,33,1,0,0,0,205,203,1,0,0,0,206,210,3,36,18,0,207,208,
        7,1,0,0,208,210,3,34,17,0,209,206,1,0,0,0,209,207,1,0,0,0,210,35,
        1,0,0,0,211,223,5,33,0,0,212,223,5,1,0,0,213,223,5,2,0,0,214,223,
        5,3,0,0,215,223,5,4,0,0,216,223,3,38,19,0,217,223,3,40,20,0,218,
        219,5,20,0,0,219,220,3,26,13,0,220,221,5,21,0,0,221,223,1,0,0,0,
        222,211,1,0,0,0,222,212,1,0,0,0,222,213,1,0,0,0,222,214,1,0,0,0,
        222,215,1,0,0,0,222,216,1,0,0,0,222,217,1,0,0,0,222,218,1,0,0,0,
        223,37,1,0,0,0,224,233,5,24,0,0,225,230,3,26,13,0,226,227,5,26,0,
        0,227,229,3,26,13,0,228,226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,
        0,0,230,231,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,233,225,1,0,
        0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,236,5,25,0,0,236,39,1,0,
        0,0,237,238,5,33,0,0,238,240,5,20,0,0,239,241,3,42,21,0,240,239,
        1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,5,21,0,0,243,41,
        1,0,0,0,244,249,3,26,13,0,245,246,5,26,0,0,246,248,3,26,13,0,247,
        245,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        43,1,0,0,0,251,249,1,0,0,0,32,50,57,62,68,78,82,88,94,101,109,113,
        118,124,128,132,135,143,147,150,162,166,170,177,187,195,203,209,
        222,230,233,240,249
    ]

class YoScriptParser ( Parser ):

    grammarFileName = "YoScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'yep'", "'nope'", 
                     "'forreal'", "'for'", "'if'", "'tho'", "'idk'", "'nahh'", 
                     "'goback'", "'in'", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "':'", "'.'", "'int'", "'str'", "'bool'", "'none'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "STRING", "TRUE", "FALSE", 
                      "FORREAL", "FOR", "IF", "THO", "IDK", "NAHH", "GOBACK", 
                      "IN", "PLUS", "MINUS", "STAR", "SLASH", "EQEQUAL", 
                      "NOTEQUAL", "EQUAL", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "COMMA", "COLON", "DOT", "INT", "STR", "BOOLEAN", 
                      "NONE", "IDENTIFIER", "NEWLINE", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expression_stmt = 3
    RULE_assignment = 4
    RULE_block = 5
    RULE_if_stmt = 6
    RULE_cond_paren = 7
    RULE_break_stmt = 8
    RULE_return_stmt = 9
    RULE_for_stmt = 10
    RULE_func_def = 11
    RULE_param_list = 12
    RULE_expression = 13
    RULE_comparison = 14
    RULE_arithmetic = 15
    RULE_term = 16
    RULE_factor = 17
    RULE_atom = 18
    RULE_list_literal = 19
    RULE_function_call = 20
    RULE_arg_list = 21

    ruleNames =  [ "program", "statements", "statement", "expression_stmt", 
                   "assignment", "block", "if_stmt", "cond_paren", "break_stmt", 
                   "return_stmt", "for_stmt", "func_def", "param_list", 
                   "expression", "comparison", "arithmetic", "term", "factor", 
                   "atom", "list_literal", "function_call", "arg_list" ]

    EOF = Token.EOF
    NUMBER=1
    STRING=2
    TRUE=3
    FALSE=4
    FORREAL=5
    FOR=6
    IF=7
    THO=8
    IDK=9
    NAHH=10
    GOBACK=11
    IN=12
    PLUS=13
    MINUS=14
    STAR=15
    SLASH=16
    EQEQUAL=17
    NOTEQUAL=18
    EQUAL=19
    OPEN_PAREN=20
    CLOSE_PAREN=21
    OPEN_BRACE=22
    CLOSE_BRACE=23
    OPEN_BRACKET=24
    CLOSE_BRACKET=25
    COMMA=26
    COLON=27
    DOT=28
    INT=29
    STR=30
    BOOLEAN=31
    NONE=32
    IDENTIFIER=33
    NEWLINE=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(YoScriptParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(YoScriptParser.EOF, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = YoScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.statements()
            self.state = 45
            self.match(YoScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.NEWLINE)
            else:
                return self.getToken(YoScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = YoScriptParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 47
                self.match(YoScriptParser.NEWLINE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.statement()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 54
                        self.match(YoScriptParser.NEWLINE)
                        self.state = 57 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==34):
                            break

                    self.state = 59
                    self.statement() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 65
                    self.match(YoScriptParser.NEWLINE) 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_stmt(self):
            return self.getTypedRuleContext(YoScriptParser.Expression_stmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(YoScriptParser.AssignmentContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(YoScriptParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(YoScriptParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(YoScriptParser.Break_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(YoScriptParser.Return_stmtContext,0)


        def func_def(self):
            return self.getTypedRuleContext(YoScriptParser.Func_defContext,0)


        def getRuleIndex(self):
            return YoScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = YoScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.expression_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.func_def()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(YoScriptParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_expression_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_stmt" ):
                listener.enterExpression_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_stmt" ):
                listener.exitExpression_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_stmt" ):
                return visitor.visitExpression_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expression_stmt(self):

        localctx = YoScriptParser.Expression_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.expression()
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(YoScriptParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YoScriptParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(YoScriptParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(YoScriptParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = YoScriptParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(YoScriptParser.IDENTIFIER)
            self.state = 85
            self.match(YoScriptParser.EQUAL)
            self.state = 86
            self.expression()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(YoScriptParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(YoScriptParser.OPEN_BRACE, 0)

        def statements(self):
            return self.getTypedRuleContext(YoScriptParser.StatementsContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(YoScriptParser.CLOSE_BRACE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.NEWLINE)
            else:
                return self.getToken(YoScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = YoScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(YoScriptParser.OPEN_BRACE)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.match(YoScriptParser.NEWLINE) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 97
            self.statements()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 98
                self.match(YoScriptParser.NEWLINE)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(YoScriptParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YoScriptParser.IF, 0)

        def cond_paren(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.Cond_parenContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.Cond_parenContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.BlockContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.BlockContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.NEWLINE)
            else:
                return self.getToken(YoScriptParser.NEWLINE, i)

        def THO(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.THO)
            else:
                return self.getToken(YoScriptParser.THO, i)

        def IDK(self):
            return self.getToken(YoScriptParser.IDK, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = YoScriptParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(YoScriptParser.IF)
            self.state = 107
            self.cond_paren()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 108
                self.match(YoScriptParser.NEWLINE)


            self.state = 111
            self.block()
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==34:
                        self.state = 112
                        self.match(YoScriptParser.NEWLINE)


                    self.state = 115
                    self.match(YoScriptParser.THO)
                    self.state = 116
                    self.cond_paren()
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==34:
                        self.state = 117
                        self.match(YoScriptParser.NEWLINE)


                    self.state = 120
                    self.block() 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 127
                    self.match(YoScriptParser.NEWLINE)


                self.state = 130
                self.match(YoScriptParser.IDK)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 131
                    self.match(YoScriptParser.NEWLINE)


                self.state = 134
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_parenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(YoScriptParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(YoScriptParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_cond_paren

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_paren" ):
                listener.enterCond_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_paren" ):
                listener.exitCond_paren(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_paren" ):
                return visitor.visitCond_paren(self)
            else:
                return visitor.visitChildren(self)




    def cond_paren(self):

        localctx = YoScriptParser.Cond_parenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond_paren)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(YoScriptParser.OPEN_PAREN)
            self.state = 138
            self.expression()
            self.state = 139
            self.match(YoScriptParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAHH(self):
            return self.getToken(YoScriptParser.NAHH, 0)

        def NEWLINE(self):
            return self.getToken(YoScriptParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_break_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = YoScriptParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(YoScriptParser.NAHH)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 142
                self.match(YoScriptParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOBACK(self):
            return self.getToken(YoScriptParser.GOBACK, 0)

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(YoScriptParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = YoScriptParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(YoScriptParser.GOBACK)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8607784990) != 0):
                self.state = 146
                self.expression()


            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(YoScriptParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(YoScriptParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(YoScriptParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(YoScriptParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(YoScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return YoScriptParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = YoScriptParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(YoScriptParser.FOR)
            self.state = 153
            self.match(YoScriptParser.IDENTIFIER)
            self.state = 154
            self.match(YoScriptParser.IN)
            self.state = 155
            self.expression()
            self.state = 156
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORREAL(self):
            return self.getToken(YoScriptParser.FORREAL, 0)

        def IDENTIFIER(self):
            return self.getToken(YoScriptParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(YoScriptParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(YoScriptParser.CLOSE_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(YoScriptParser.BlockContext,0)


        def param_list(self):
            return self.getTypedRuleContext(YoScriptParser.Param_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.NEWLINE)
            else:
                return self.getToken(YoScriptParser.NEWLINE, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = YoScriptParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(YoScriptParser.FORREAL)
            self.state = 159
            self.match(YoScriptParser.IDENTIFIER)
            self.state = 160
            self.match(YoScriptParser.OPEN_PAREN)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 161
                self.param_list()


            self.state = 164
            self.match(YoScriptParser.CLOSE_PAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 165
                self.match(YoScriptParser.NEWLINE)


            self.state = 168
            self.block()
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 169
                self.match(YoScriptParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.IDENTIFIER)
            else:
                return self.getToken(YoScriptParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.COMMA)
            else:
                return self.getToken(YoScriptParser.COMMA, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = YoScriptParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(YoScriptParser.IDENTIFIER)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 173
                self.match(YoScriptParser.COMMA)
                self.state = 174
                self.match(YoScriptParser.IDENTIFIER)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(YoScriptParser.ComparisonContext,0)


        def getRuleIndex(self):
            return YoScriptParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = YoScriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.ArithmeticContext,i)


        def EQEQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.EQEQUAL)
            else:
                return self.getToken(YoScriptParser.EQEQUAL, i)

        def NOTEQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.NOTEQUAL)
            else:
                return self.getToken(YoScriptParser.NOTEQUAL, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = YoScriptParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.arithmetic()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 183
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 184
                self.arithmetic()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.TermContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.PLUS)
            else:
                return self.getToken(YoScriptParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.MINUS)
            else:
                return self.getToken(YoScriptParser.MINUS, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = YoScriptParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.term()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.term()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.FactorContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.FactorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.STAR)
            else:
                return self.getToken(YoScriptParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.SLASH)
            else:
                return self.getToken(YoScriptParser.SLASH, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = YoScriptParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.factor()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.factor()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(YoScriptParser.AtomContext,0)


        def factor(self):
            return self.getTypedRuleContext(YoScriptParser.FactorContext,0)


        def PLUS(self):
            return self.getToken(YoScriptParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(YoScriptParser.MINUS, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = YoScriptParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 20, 24, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.atom()
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YoScriptParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(YoScriptParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(YoScriptParser.STRING, 0)

        def TRUE(self):
            return self.getToken(YoScriptParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YoScriptParser.FALSE, 0)

        def list_literal(self):
            return self.getTypedRuleContext(YoScriptParser.List_literalContext,0)


        def function_call(self):
            return self.getTypedRuleContext(YoScriptParser.Function_callContext,0)


        def OPEN_PAREN(self):
            return self.getToken(YoScriptParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(YoScriptParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(YoScriptParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return YoScriptParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = YoScriptParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_atom)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(YoScriptParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(YoScriptParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(YoScriptParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(YoScriptParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.match(YoScriptParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.list_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 217
                self.function_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 218
                self.match(YoScriptParser.OPEN_PAREN)
                self.state = 219
                self.expression()
                self.state = 220
                self.match(YoScriptParser.CLOSE_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(YoScriptParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(YoScriptParser.CLOSE_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.COMMA)
            else:
                return self.getToken(YoScriptParser.COMMA, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_list_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_literal" ):
                listener.enterList_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_literal" ):
                listener.exitList_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = YoScriptParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(YoScriptParser.OPEN_BRACKET)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8607784990) != 0):
                self.state = 225
                self.expression()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 226
                    self.match(YoScriptParser.COMMA)
                    self.state = 227
                    self.expression()
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 235
            self.match(YoScriptParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(YoScriptParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(YoScriptParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(YoScriptParser.CLOSE_PAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(YoScriptParser.Arg_listContext,0)


        def getRuleIndex(self):
            return YoScriptParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = YoScriptParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(YoScriptParser.IDENTIFIER)
            self.state = 238
            self.match(YoScriptParser.OPEN_PAREN)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8607784990) != 0):
                self.state = 239
                self.arg_list()


            self.state = 242
            self.match(YoScriptParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YoScriptParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YoScriptParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YoScriptParser.COMMA)
            else:
                return self.getToken(YoScriptParser.COMMA, i)

        def getRuleIndex(self):
            return YoScriptParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = YoScriptParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expression()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 245
                self.match(YoScriptParser.COMMA)
                self.state = 246
                self.expression()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






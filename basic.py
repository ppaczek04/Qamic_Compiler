from tokens import *
from lexer import *
from parser import *
            
########################################
# RUN
########################################

def run(fn, text):
    #Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    #Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()

    return ast, None

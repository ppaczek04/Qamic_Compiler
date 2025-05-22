import sys
from antlr4 import *
from gen.YoScriptLexer import YoScriptLexer
from gen.YoScriptParser import YoScriptParser
from RuntimeVisitor import RuntimeVisitor

def run_file(filename):
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = YoScriptLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = YoScriptParser(tokens)
    tree = parser.program()
    try:
        RuntimeVisitor().visit(tree)
    except RuntimeError as e:
        print(f"Runtime error: {e}")
        sys.exit(1)
    except NameError as e:
        print(f"Name error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py <file.youth>")
        sys.exit(1)
    run_file(sys.argv[1])

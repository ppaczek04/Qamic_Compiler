# from tokens import *
# from lexer import *
# import sys

# def token_to_html(token):
#     """Konwertuje token na HTML z odpowiednim kolorem."""
#     token_colors = {
#         TT_INT: "blue",
#         TT_FLOAT: "blue",
#         TT_PLUS: "red",
#         TT_MINUS: "red",
#         TT_MUL: "red",
#         TT_DIV: "red",
#         TT_LPAREN: "green",
#         TT_RPAREN: "green",
#     }
#     color = token_colors.get(token.type, "black")
#     return f'<span style="color: {color};">{token}</span>'

# def highlight_syntax(input_file, output_file):
#     """Odczytuje plik wejściowy, analizuje tokeny i zapisuje pokolorowany HTML."""
#     with open(input_file, "r") as f:
#         code = f.read()
    
#     lexer = Lexer(input_file, code)
#     tokens, error = lexer.make_tokens()
#     if error:
#         print(error.as_string())
#         return
    
#     highlighted_code = "".join(token_to_html(tok) + " " for tok in tokens)
    
#     html_content = f"""
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <title>Highlighted Code</title>
#     </head>
#     <body>
#         <pre>{highlighted_code}</pre>
#     </body>
#     </html>
#     """
    
#     with open(output_file, "w") as f:
#         f.write(html_content)
    
#     print(f"Pokolorowany kod zapisano w {output_file}")

# # Przykładowe użycie: highlight_syntax("input.bas", "output.html")

from tokens import *
from lexer import *

def token_to_html(token):
    """Konwertuje token na HTML z odpowiednim kolorem i symbolem."""
    token_colors = {
        TT_INT: "blue",
        TT_FLOAT: "blue",
        TT_PLUS: "red",
        TT_MINUS: "red",
        TT_MUL: "red",
        TT_DIV: "red",
        TT_LPAREN: "green",
        TT_RPAREN: "green",
    }
    
    token_symbols = {
        TT_PLUS: "+",
        TT_MINUS: "-",
        TT_MUL: "*",
        TT_DIV: "/",
        TT_LPAREN: "(",
        TT_RPAREN: ")"
    }
    
    color = token_colors.get(token.type, "black")
    symbol = token_symbols.get(token.type, str(token.value))  # Jeśli to liczba, wyświetl wartość
    
    return f'<span style="color: {color};">{symbol}</span>'

def highlight_syntax(input_file, output_file):
    """Odczytuje plik wejściowy, analizuje tokeny i zapisuje pokolorowany HTML."""
    with open(input_file, "r") as f:
        code = f.read()
    
    lexer = Lexer(input_file, code)
    tokens, error = lexer.make_tokens()
    if error:
        print(error.as_string())
        return
    
    highlighted_code = "".join(token_to_html(tok) + " " for tok in tokens)
    
    html_content = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Highlighted Code</title>
    </head>
    <body>
        <pre>{highlighted_code}</pre>
    </body>
    </html>
    """
    
    with open(output_file, "w") as f:
        f.write(html_content)
    
    print(f"Pokolorowany kod zapisano w {output_file}")

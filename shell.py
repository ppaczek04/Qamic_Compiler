# import basic

# while True:

#     text = input('basic> ')
#     # run method creates Lexer with text to scan, 
#     # it returns token list as a result and potential errors as error
#     result, error = basic.run('<stdin>', text)

#     if error:
#         print(error.as_string())
#     else:
#         print(result)

# VERSION FOR INPUT FROM FILE
import basic
from syntax import *

with open("input.txt", "r") as file:
    text = file.read()

result, error = basic.run("input.txt", text)

if error:
    print(error.as_string())
else:
    print(result)

# Generowanie kolorowanego HTML
highlight_syntax("input.txt", "output.html")
print("Wygenerowano plik output.html z pokolorowaną składnią.")
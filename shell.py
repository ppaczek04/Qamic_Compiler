import basic

while True:
    text = input('basic> ')
    # run method creates Lexer with text to scan, 
    # it returns token list as a result and potential errors as error
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
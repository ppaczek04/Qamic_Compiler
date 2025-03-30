# Qamic_Compiler
Writing our own programming language as a project for my univeristy laboratory.
![Qamic logo](resources/images/Qamic_logo.png) 
## Introduction
We are writing our own programming language for our univeristy course. For now, our lexer can interpret text file into tokens an print them out, including error handling (so if lexer cant interpret sth, info about where and what happened will be returned).


## Project structure:

- shell.py ----> contains the main loop of our compiler taking input
- basic.py ----> contains logic of the project
- lexer.py ----> contains lexer (scanner) and errors for scanning
- parser.py ----> contains parser
- tokens.py ----> contains all tokens
- syntax.py ----> contains code generating html file

------------
- input.txt ----> contains code to analyse
- output.html ----> containes coloured input
- resources/images 
- readme.md

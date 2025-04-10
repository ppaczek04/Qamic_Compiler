// Młodzieżowy Python (yoScript)
grammar YoScript;

// ===== Lexer Rules =====
// Tokeny
NUMBER: '-'? ('0' | [1-9][0-9]*)( '.' [0-9]+ )? ( ('e' | 'E') [+-]? [0-9]+ )?;
STRING: '"' ( '\\' . | ~["\\] )* '"' | '\'' ( '\\' . | ~['\\] )* '\'';
BOOLEAN_LITERAL: 'tru' | 'nope';

// Operatory
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
LESS: '<';
GREATER: '>';
EQUAL: '=';
EQEQUAL: '==';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';

// Znaki interpunkcyjne
COLON: ':';
COMMA: ',';
DOT: '.';
SEMI: ';';

// Nawiasy
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';

// Słowa kluczowe
BREAK: 'nahh';
ELSE: 'else';
RETURN: 'ima';
CONTINUE: 'goon';
DEF: 'function';
IF: 'if';
WHILE: 'while';
FOR: 'forreal';
CLASS: 'class';
IN: 'in';

// Typy
INT_TYPE: 'int';
STR_TYPE: 'str';
FLOAT_TYPE: 'float';
BOOL_TYPE: 'bool';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;

// ===== Parser Rules =====
program: statements EOF;

statements: NEWLINE* statement (NEWLINE+ statement)* NEWLINE*;

statement
    : expression_statement
    | assignment_statement
    | reassignment_statement
    | if_statement
    | while_statement
    | for_statement
    | function_definition
    | return_statement;

expression_statement: expression NEWLINE?;

assignment_statement: IDENTIFIER COLON type EQUAL expression SEMI?;

reassignment_statement: IDENTIFIER EQUAL expression SEMI?;

if_statement: IF expression OPEN_BRACE NEWLINE statements CLOSE_BRACE NEWLINE? (ELSE OPEN_BRACE NEWLINE statements CLOSE_BRACE)?;

while_statement: WHILE expression OPEN_BRACE NEWLINE statements CLOSE_BRACE;

for_statement: FOR IDENTIFIER IN expression OPEN_BRACE NEWLINE statements CLOSE_BRACE;

function_definition: DEF IDENTIFIER OPEN_PAREN typed_parameters? CLOSE_PAREN OPEN_BRACE NEWLINE statements CLOSE_BRACE;

typed_parameters: typed_parameter (COMMA typed_parameter)*;

typed_parameter: IDENTIFIER COLON type;

return_statement: RETURN expression? SEMI?;

expression_list: expression (COMMA expression)*;

expression: primary (operator primary)*;

operator
    : PLUS
    | MINUS
    | STAR
    | SLASH
    | LESS
    | GREATER
    | EQEQUAL
    | LESSEQUAL
    | GREATEREQUAL;

primary
    : IDENTIFIER
    | NUMBER
    | STRING
    | BOOLEAN_LITERAL
    | OPEN_PAREN expression CLOSE_PAREN
    | OPEN_BRACKET expression_list? CLOSE_BRACKET
    | function_call;

function_call: IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN;

type: INT_TYPE | STR_TYPE | FLOAT_TYPE | BOOL_TYPE;

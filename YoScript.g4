grammar YoScript;

// ───── Parser ─────────────────────────────────────────

program         : statements EOF ;

// ogólna sekwencja instrukcji
statements      : NEWLINE* statement (NEWLINE+ statement)* NEWLINE* ;

statement
    : expression_stmt
    | assignment
    | if_stmt
    | for_stmt
    | break_stmt            // ← już działa
    | return_stmt           // ← już działa
    | func_def
    ;

// ─── proste ─────────────────
expression_stmt : expression NEWLINE? ;
assignment      : IDENTIFIER EQUAL expression NEWLINE? ;

// ─── sterowanie ─────────────
block           : OPEN_BRACE NEWLINE* statements NEWLINE* CLOSE_BRACE NEWLINE? ;
if_stmt         : IF cond_paren block (IDK block)? ;
cond_paren      : OPEN_PAREN expression CLOSE_PAREN ;
break_stmt      : NAHH NEWLINE? ;
return_stmt     : GOBACK expression? NEWLINE? ;

// ─── pętla for ──────────────
for_stmt        : FOR IDENTIFIER IN expression block ;

// ─── funkcje ────────────────
func_def        : FORREAL IDENTIFIER OPEN_PAREN param_list? CLOSE_PAREN block NEWLINE? ;
param_list      : IDENTIFIER (COMMA IDENTIFIER)* ;

// ─── wyrażenia ──────────────
expression : comparison ;
comparison : arithmetic ((EQEQUAL | NOTEQUAL) arithmetic)* ;
arithmetic : term ((PLUS | MINUS) term)* ;
term       : factor ((STAR | SLASH) factor)* ;
factor     : atom | (PLUS | MINUS) factor ;

atom
    : IDENTIFIER
    | NUMBER
    | STRING
    | list_literal
    | function_call
    | OPEN_PAREN expression CLOSE_PAREN
    ;

// literał listy  [1, 2, 3]
list_literal    : OPEN_BRACKET (expression (COMMA expression)*)? CLOSE_BRACKET ;

// wywołanie funkcji
function_call   : IDENTIFIER OPEN_PAREN arg_list? CLOSE_PAREN ;
arg_list        : expression (COMMA expression)* ;

// ───── Lexer ─────────────────────────────────────────

// literały
NUMBER          : '-'? ( '0' | [1-9] [0-9]* ) ( '.' [0-9]+ )?;
STRING          : '"' ( '\\' . | ~["\\] )* '"' | '\'' ( '\\' . | ~['\\] )* '\'';

// słowa-klucze (najdłuższe najpierw)
FORREAL         : 'forreal';      // def-funkcji
FOR             : 'for';          // pętla
IF              : 'if';
IDK             : 'idk';          // else
NAHH            : 'nahh';         // break
GOBACK          : 'goback';       // return
IN              : 'in';

// operatory i delimitery
PLUS            : '+';
MINUS           : '-';
STAR            : '*';
SLASH           : '/';
EQEQUAL         : '==';
NOTEQUAL        : '!=';
EQUAL           : '=';
OPEN_PAREN      : '(';
CLOSE_PAREN     : ')';
OPEN_BRACE      : '{';
CLOSE_BRACE     : '}';
OPEN_BRACKET    : '[';            // ★ dla listy
CLOSE_BRACKET   : ']';
COMMA           : ',';
COLON           : ':';
DOT             : '.';

// typy (minimum)
INT             : 'int';
STR             : 'str';
BOOLEAN         : 'bool';
NONE            : 'none';

// identyfikatory / whitespace
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE         : '\r'? '\n';
WS              : [ \t]+ -> skip;
COMMENT         : '#' ~[\r\n]* -> skip;
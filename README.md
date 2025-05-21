# YoScript – interpreter języka inspirowanego Pythonem

**YoScript** to lekki, edukacyjny język skryptowy z „młodzieżowym” słownictwem (np. `forreal`, `nahh`, `goback`) i blokami oznaczanymi nawiasami klamrowymi `{}` zamiast wcięć. Jego celem jest poznanie zasad budowy interpreterów przy użyciu ANTLR 4.

---

## 1. Dane studenta

* **Imię i nazwisko:** Piotr Peca, Piotr Pączek

---

## 2. Dane kontaktowe:

* **E-mail:** 
  * piotrpeca@student.agh.edu.pl 
  * ppaczek@student.agh.edu.pl

---

## 3. Założenia programu

1. **Cele ogólne:**

   * Stworzyć interpreter języka o składni inspirowanej Pythonem, lecz z uproszczonym blokowaniem i slangowymi słowami-kluczami.
   * Poznać przepływ pracy z ANTLR 4: od gramatyki, przez parser, po wykonanie AST.
2. **Rodzaj translatora:** Interpreter.
3. **Planowany wynik:**

   * Interpreter języka YoScript, która jest młodzieżową odmianą uproszczonego Pythona z nawiasami.
4. **Język implementacji:** Python 3.
5. **Scanner/parser:** ANTLR 4 (generowany parser w Pythonie).

---

## 4. Opis tokenów

| Token           | Lexem               | Znaczenie                       |
|-----------------| ------------------- |---------------------------------|
| `NUMBER`        | `123.45`            | liczba                          |
| `STRING`        | `"abc"` lub `'abc'` | ciąg znaków                     |
| `FORREAL`       | `forreal`           | definicja funkcji               |
| `FOR`           | `for`               | pętla                           |
| `IF`            | `if`                | warunek                         |
| `IDK`           | `idk`               | else                            |
| `NAHH`          | `nahh`              | break                           |
| `GOBACK`        | `goback`            | return                          |
| `IN`            | `in`                | słowo-klucz pętli               |
| `PLUS`          | `+`                 | dodawanie                       |
| `MINUS`         | `-`                 | odejmowanie                     |
| `STAR`          | `*`                 | mnożenie                        |
| `SLASH`         | `/`                 | dzielenie                       |
| `EQEQUAL`       | `==`                | równość                         |
| `NOTEQUAL`      | `!=`                | nierówność                      |
| `EQUAL`         | `=`                 | przypisanie                     |
| `OPEN_PAREN`    | `(`                 | nawias otwierający              |
| `CLOSE_PAREN`   | `)`                 | nawias zamykający               |
| `OPEN_BRACE`    | `{`                 | początek bloku                  |
| `CLOSE_BRACE`   | `}`                 | koniec bloku                    |
| `OPEN_BRACKET`  | `[`                 | początek listy                  |
| `CLOSE_BRACKET` | `]`                 | koniec listy                    |
| `COMMA`         | `,`                 | separator                       |
| `COLON`         | `:`                 | (rezerwowane na adnotacje typu) |
| `DOT`           | `.`                 | notacja dostępu                 |
| `INT`           | `int`               | typ integer                     |
| `STR`           | `str`               | typ string                      |
| `BOOLEAN`       | `bool`              | typ boolean                     |
| `NONE`          | `none`              | typ None/null                   |
| `IDENTIFIER`    | `x`, `foo`          | nazwa zmiennej/funkcji          |
| `NEWLINE`       | `'\r'? '\n'`          | nowa linia                      |
| `WS`            | `[ \t]+ -> skip`          | whitespace                      |
| `COMMENT`       | `'#' ~[\r\n]* -> skip`          | komentarz                       |

---

## 5. Gramatyka formatu

### ANTLR 4 (YoScript.g4 excerpt)

```antlr
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
    | break_stmt           
    | return_stmt          
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

// ── literał listy  [1, 2, 3] ──────────────
list_literal    : OPEN_BRACKET (expression (COMMA expression)*)? CLOSE_BRACKET ;

// ─── wywołanie funkcji ──────────────
function_call   : IDENTIFIER OPEN_PAREN arg_list? CLOSE_PAREN ;
arg_list        : expression (COMMA expression)* ;
```

---

## 6. Narzędzia i generatory

* **ANTLR 4.13.2** – do generacji leksera, parsera i klas Visitor/Listener.
* **Java 11+** – wymagana przez ANTLR.
* **`antlr4-python3-runtime`** – Pythonowy runtime do uruchamiania parsera.
* **PyCharm + plugin ANTLR v4** (opcjonalnie) – podświetlanie `.g4`, podgląd drzewa.

---

## 7. Krótka instrukcja obsługi

1. **Generacja parsera**

   ```bash
   alias antlr4='java -jar ~/tools/antlr-4.13.2-complete.jar'
   antlr4 -Dlanguage=Python3 -visitor YoScript.g4 -o gen
   ```
2. **Instalacja runtime’u**

   ```bash
   pip install antlr4-python3-runtime
   ```
3. **Uruchomienie skryptu**

   ```bash
   python run.py examples/example1
   ```
   
---

## 8. Przykład użycia

`examples/example_test`:

```youth
# Funkcja do mnożenia przez dwa
forreal timesTwo(x) {
    goback x * 2
}

# Funkcja testująca konkretną wartość
forreal isSpecial(n) {
    if (n == 3) {
        goback 1
    }
    idk {
        goback 0
    }
}

# Funkcja bez parametrów
forreal greet() {
    print("Welcome to YoScript!")
}

# Przypisanie listy
nums = [1, 2, 3, 4]

# Wywołanie funkcji bez argumentów
greet()

# Pętla + funkcje + if + idk + break
for n in nums {
    doubled = timesTwo(n)
    print("n:", n, "doubled:", doubled)

    if (isSpecial(n) == 1) {
        print(n, "is special!")
    }
    idk {
        print(n, "is not special.")
    }

    if (n == 4) {
        print("Breaking at", n)
        nahh
    }
}

# Proste obliczenia
a = 10
b = 2
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Porównania
print("a == b:", a == b)
print("a != b:", a != b)

```

**Output:**

```
Welcome to YoScript!
n: 1.0 doubled: 2.0
1.0 is not special.
n: 2.0 doubled: 4.0
2.0 is not special.
n: 3.0 doubled: 6.0
3.0 is special!
n: 4.0 doubled: 8.0
4.0 is not special.
Breaking at 4.0
a + b = 12.0
a - b = 8.0
a * b = 20.0
a / b = 5.0
a == b: False
a != b: True
```

---

## 9. Obsługa błędów

* **Błędy semantyczne/runtime:**

  * `NameError` przy odwołaniu do niezdefiniowanej zmiennej lub funkcji,
  * `RuntimeError("‘nahh’ użyte poza pętlą")`,
  * `ReturnSignal` i `BreakSignal` – wyjątki-sygnały sterujące przepływem.
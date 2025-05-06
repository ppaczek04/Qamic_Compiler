# YoScript

**YoScript** is a fun, simplified Python-inspired language created for learning compiler construction with ANTLR 4.  
It uses youth-style slang for keywords (e.g., `forreal`, `nahh`, `goback`) and curly braces `{}` for blocks instead of indentation, making parsing easier and more flexible.

---

## 🚀 How to Run

### 1. Requirements
- Java 11+
- ANTLR 4.13.x (e.g. `antlr-4.13.2-complete.jar`)
- Python 3 with `antlr4-python3-runtime` (if using Python target)

### 2. Generating the Lexer and Parser (Python target)
```bash
alias antlr4='java -jar ~/tools/antlr-4.13.2-complete.jar'

antlr4 -Dlanguage=Python3 -visitor YoScript.g4
```

This generates:
- `YoScriptLexer.py`
- `YoScriptParser.py`
- `YoScriptVisitor.py`
- `YoScript.tokens`

---

## 🧪 Example Program

```youthpy
forreal timesTwo(x) {
    goback x * 2
}

nums = [1, 2, 3]
for n in nums {
    print(timesTwo(n))
    if (n == 2) {
        nahh
    }
}
```

Expected output:
```
2
4
```

---

## 📜 Token Reference

| Token        | Lexeme     | Meaning                 |
|--------------|------------|--------------------------|
| `FORREAL`    | `forreal`  | function definition      |
| `FOR`        | `for`      | loop                     |
| `IF`         | `if`       | condition                |
| `IDK`        | `idk`      | else block               |
| `NAHH`       | `nahh`     | break                    |
| `GOBACK`     | `goback`   | return                   |
| `IN`         | `in`       | loop keyword             |
| `PLUS`       | `+`        | addition                 |
| `MINUS`      | `-`        | subtraction              |
| `STAR`       | `*`        | multiplication           |
| `SLASH`      | `/`        | division                 |
| `EQEQUAL`    | `==`       | equality comparison      |
| `NOTEQUAL`   | `!=`       | inequality comparison    |
| `EQUAL`      | `=`        | assignment               |
| `NUMBER`     | `123.45`   | number                   |
| `STRING`     | `"abc"`    | string                   |
| `IDENTIFIER`  | `x`        | variable or function name        |
| `OPEN_PAREN`  | `(`        | start of parameter list/grouping |
| `CLOSE_PAREN` | `)`        | end of parameter list/grouping   |
| `OPEN_BRACE`  | `{`        | block start                      |
| `CLOSE_BRACE` | `}`        | block end                        |
| `OPEN_BRACKET`| `[`        | list start                       |
| `CLOSE_BRACKET`| `]`       | list end                         |
| `COMMA`       | `,`        | separator                        |
| `COLON`       | `:`        | used in type annotations         |
| `DOT`         | `.`        | attribute/method access          |

---

## 📁 Project Structure

```
.
├── YoScript.g4           # ANTLR grammar
├── YoScriptLexer.py      # generated lexer
├── YoScriptParser.py     # generated parser
├── YoScriptVisitor.py    # generated visitor base class
├── run_youthpy.py        # your custom interpreter (to implement)
└── examples/
    └── demo.youthpy       # sample YoScript file
```

---

## 🛠️ Running your own program

1. Write code in `examples/demo.youthpy`
2. Run it with:
```bash
python run_youthpy.py examples/demo.youthpy
```

Have fun with **YoScript**! 😎
# YoScript

**YoScript** (aka *Youth Python*) – humorystyczny, uproszczony dialekt Pythona używany do ćwiczeń z gramatyk i narzędzia ANTLR 4.  
Zamiast klasycznych słów-kluczy używa slangu (np. `forreal`, `nahh`), a bloki kodu ograniczane są klamrami `{}` – bez wcięć.

---

## 🚀 Jak uruchomić

### 1. Wymagania
- Java 11+
- ANTLR 4.13.x (np. `antlr-4.13.2-complete.jar`)
- Python 3 + `antlr4-python3-runtime`

### 2. Generowanie parsera (Python target)
```bash
alias antlr4='java -jar ~/tools/antlr-4.13.2-complete.jar'

antlr4 -Dlanguage=Python3 -visitor YoScript.g4
```

Wygeneruje m.in.:
- `YoScriptLexer.py`
- `YoScriptParser.py`
- `YoScriptVisitor.py`

---

## 🧪 Przykładowy program

```youthpy
forreal timesTwo(x) {
    goback x * 2
}

nums = [1, 2, 3]
for n in nums {
    print(timesTwo(n))
    if n == 2 {
        nahh
    }
}
```

Oczekiwane wyjście:
```
2
4
```

---

## 📜 Tokeny języka

| Token        | Lexem     | Znaczenie               |
|--------------|-----------|--------------------------|
| `FORREAL`    | `forreal` | definicja funkcji        |
| `FOR`        | `for`     | pętla `for`              |
| `IF`         | `if`      | instrukcja warunkowa     |
| `IDK`        | `idk`     | gałąź `else`             |
| `NAHH`       | `nahh`    | `break`                  |
| `GOBACK`     | `goback`  | `return`                 |
| `IN`         | `in`      | składnia pętli           |
| `PLUS`       | `+`       | dodawanie                |
| `MINUS`      | `-`       | odejmowanie              |
| `STAR`       | `*`       | mnożenie                 |
| `SLASH`      | `/`       | dzielenie                |
| `EQEQUAL`    | `==`      | porównanie               |
| `NOTEQUAL`   | `!=`      | różne                    |
| `EQUAL`      | `=`       | przypisanie              |
| `NUMBER`     | `123.45`  | liczba                   |
| `STRING`     | `"abc"`   | łańcuch znaków           |
| `IDENTIFIER` | `x`       | identyfikator            |

---

## 📁 Struktura katalogu

```
.
├── YoScript.g4           # plik gramatyki ANTLR
├── YoScriptLexer.py      # lexer (wygenerowany)
├── YoScriptParser.py     # parser (wygenerowany)
├── YoScriptVisitor.py    # visitor (wygenerowany)
├── run_youthpy.py        # interpreter (Twoja implementacja)
└── examples/
    └── demo.youthpy      # przykładowy kod
```

---

## 🛠️ Uruchomienie własnego programu

1. Zapisz kod w pliku `examples/demo.youthpy`
2. Uruchom interpreter:
```bash
python run_youthpy.py examples/demo.youthpy
```

Miłej zabawy z **YoScript**! 😎

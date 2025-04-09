# token_types.py

TOKEN_TYPES = {
    "KEYWORDS": {
        "program", "begin", "end", "var", "integer", "writeln"
    },
    "OPERATORS": {
        "+": "PLUS",
        "-": "MINUS",
        "*": "MULT",
        "/": "DIV",
        ":=": "ASSIGN",
        "=": "EQUAL"
    },
    "DELIMITERS": {
        ";": "SEMICOLON",
        ".": "DOT",
        ",": "COMMA",
        "(": "LPAREN",
        ")": "RPAREN",
        ":": "COLON"
    }
}

# token_types.py

TIPO_TOKENS = {
    "PALAVRA-CHAVE": {
        "program", "var", "integer", "real", "string", "begin", "end", "for", 
        "to", "while", "do", "break", "continue", "if", "else", "then", "write",
        "writeln", "read", "readln"
    },
    "OPERATORS": {
        "+": "PLUS",
        "-": "MINUS",
        "*": "MULT",
        "/": "DIV",
        ":=": "ASSIGN",
        "=": "EQUAL"
    },
    "DELIMITADOR": {
        ";": "PONTO_VIRGULA",
        ".": "PONTO_FINAL",
        ",": "VIRGULA",
        "(": "ABRE_PARENTESES",
        ")": "FECHA_PARENTESES",
        ":": "DOIS_PONTOS"
    }
}

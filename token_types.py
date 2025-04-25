# Dicionário de tipos de tokens para o analisador léxico #
TIPO_TOKENS = {
    "PALAVRA-CHAVE": {
        "program", "var", "integer", "real", "string", "boolean",
        "begin", "end", "for", "to", "while", "do", "break", "continue",
        "if", "else", "then", "write", "writeln", "read", "readln"
    },
    "OPERADORES": {
        "+": "ADICAO",
        "-": "SUBTRACAO",
        "*": "MULTIPLICACAO",
        "/": "DIVISAO_REAL",
        "mod": "MODULO",
        "div": "DIVISAO_INTEIRA",
        ":=": "ATRIBUICAO",
    },
    "DELIMITADOR": {
        ";": "PONTO_VIRGULA",
        ".": "PONTO_FINAL",
        ",": "VIRGULA",
        "(": "ABRE_PARENTESES",
        ")": "FECHA_PARENTESES",
        ":": "DOIS_PONTOS"
    },
    "LOGICOS": {
        "or": "OU",
        "and": "E",
        "not": "NAO"
    },
    "RELACIONAIS": {
        "==": "IGUAL",
        "=": "IGUAL",
        "<>": "DIFERENTE",
        "<": "MENOR",
        ">": "MAIOR",
        "<=": "MENOR_IGUAL",
        ">=": "MAIOR_IGUAL"
    }
}

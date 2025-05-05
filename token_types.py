# Dicionário de tipos de tokens para o analisador léxico #
TIPO_TOKENS = {
    "PALAVRA-CHAVE": {
        "program": 1, 
        "var": 2, 
        "integer": 3, 
        "real": 4, 
        "string": 5, 
        "boolean": 6,
        "begin": 7, 
        "end": 8, 
        "for": 9, 
        "to": 10, 
        "while": 11, 
        "do": 12, 
        "break": 13, 
        "continue": 14,
        "if": 15, 
        "else": 16, 
        "then": 17, 
        "write": 18, 
        "writeln": 19, 
        "read": 20, 
        "readln": 21
    },
    "OPERADORES": {
        "+": 22,
        "-": 23,
        "*": 24,
        "/": 25,
        "mod": 26,
        "div": 27,
        ":=": 28,
    },
    "DELIMITADOR": {
        ";": 29,
        ".": 30,
        ",": 31,
        "(": 32,
        ")": 33,
        ":": 34
    },
    "LOGICOS": {
        "or": 35,
        "and":36,
        "not": 37
    },
    "RELACIONAIS": {
        "==": 38,
        "=": 38,
        "<>": 39,
        "<": 40,
        ">": 41,
        "<=": 42,
        ">=": 43
    }
}

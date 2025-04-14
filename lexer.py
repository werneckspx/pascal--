# lexer.py

from token_types import TIPO_TOKENS

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        self.variables = {}


    def tokenize(self):
        while self.pos < len(self.code):
            current_char = self.code[self.pos]

            if current_char.isspace():
                self._advance_whitespace(current_char)
            elif current_char.isalpha():
                self._identificador_ou_palavrachave()
            elif current_char.isdigit():
                self._number()
            elif current_char == '"':
                self._string()
            else:
                self._operator_or_delimiter()
        return self.tokens

    def _advance(self):
        self.pos += 1
        self.col += 1

    def _advance_whitespace(self, char):
        if char == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.pos += 1

    def _identificador_ou_palavrachave(self):
        start_pos = self.pos
        start_col = self.col
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == "_"):
            self._advance()
        lexeme = self.code[start_pos:self.pos]
        token_type = "PALAVRA-CHAVE" if lexeme.lower() in TIPO_TOKENS["PALAVRA-CHAVE"] else "IDENTIFICADOR"
        self.tokens.append((token_type, lexeme, self.line, start_col))

    def _number(self):
        start_pos = self.pos
        start_col = self.col
        while self.pos < len(self.code) and self.code[self.pos].isdigit():
            self._advance()
        lexeme = self.code[start_pos:self.pos]
        self.tokens.append(("NUMBER", lexeme, self.line, start_col))

    def _string(self):
        start_col = self.col
        self._advance()  # skip opening "
        start_pos = self.pos
        while self.pos < len(self.code) and self.code[self.pos] != '"':
            self._advance()
        lexeme = self.code[start_pos:self.pos]
        self._advance()  # skip closing "
        self.tokens.append(("STRING", lexeme, self.line, start_col))

    def _operator_or_delimiter(self):
        start_col = self.col
        ch = self.code[self.pos]
        two_char_op = self.code[self.pos:self.pos+2]
        if two_char_op in TIPO_TOKENS["OPERATORS"]:
            self.tokens.append((TIPO_TOKENS["OPERATORS"][two_char_op], two_char_op, self.line, start_col))
            self._advance()
            self._advance()
        elif ch in TIPO_TOKENS["OPERATORS"]:
            self.tokens.append((TIPO_TOKENS["OPERATORS"][ch], ch, self.line, start_col))
            self._advance()
        elif ch in TIPO_TOKENS["DELIMITADOR"]:
            self.tokens.append((TIPO_TOKENS["DELIMITADOR"][ch], ch, self.line, start_col))
            self._advance()
        else:
            print(f"Unknown character {ch} at line {self.line}, col {self.col}")
            self._advance()
    
    def simulate_output(self):
        output = []
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            # Trata declaração de variáveis
            if token[0] == "PALAVRA-CHAVE" and token[1] == "var":
                i += 1
                while self.tokens[i][0] == "IDENTIFICADOR":
                    var_name = self.tokens[i][1]
                    self.variables[var_name] = 0
                    i += 1
                    if self.tokens[i][0] == "DOIS_PONTOS":
                        i += 1  # tipo
                        i += 1  # pula o tipo
                    if self.tokens[i][0] == "PONTO_VIRGULA":
                        i += 1
                        break

            # Trata atribuição: x := 2 + 2;
            elif token[0] == "IDENTIFICADOR" and self.tokens[i + 1][0] == "ASSIGN":
                var_name = token[1]
                i += 2  # pula o IDENTIFICADOR e o :=
                expr = ""
                while self.tokens[i][0] not in ["PONTO_VIRGULA"]:
                    t_type, lex, *_ = self.tokens[i]
                    if t_type in ["NUMBER", "IDENTIFICADOR"]:
                        if t_type == "IDENTIFICADOR":
                            expr += str(self.variables.get(lex, 0))
                        else:
                            expr += lex
                    elif t_type == "PLUS":
                        expr += "+"
                    elif t_type == "MINUS":
                        expr += "-"
                    elif t_type == "MULTIPLY":
                        expr += "*"
                    elif t_type == "DIVIDE":
                        expr += "/"
                    i += 1
                try:
                    self.variables[var_name] = eval(expr)
                except Exception:
                    self.variables[var_name] = "error"

            # Trata writeln(...)
            elif token[0] == "PALAVRA-CHAVE" and token[1] == "writeln":
                if self.tokens[i + 1][0] == "ABRE_PARENTESES":
                    i += 2
                    out_line = ""
                    while self.tokens[i][0] != "FECHA_PARENTESES":
                        t_type, lex, *_ = self.tokens[i]
                        if t_type == "STRING":
                            out_line += lex
                        elif t_type == "NUMBER":
                            out_line += lex
                        elif t_type == "IDENTIFICADOR":
                            out_line += str(self.variables.get(lex, "undefined"))
                        elif t_type == "PLUS":
                            out_line += " + "
                        i += 1
                    output.append(out_line.strip())
            i += 1
        return output

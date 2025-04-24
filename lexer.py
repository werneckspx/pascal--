from token_types import TIPO_TOKENS

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        self.variables = {}
        self.var_types = {}

    # def tokenize(self):
    #     while self.pos < len(self.code):
    #         current_char = self.code[self.pos]

    #         if current_char.isspace():
    #             self._advance_whitespace(current_char)
    #         elif current_char.isalpha():
    #             self._identificador_ou_palavrachave()
    #         elif current_char.isdigit() or current_char in "$&":
    #             self._number()
    #         elif current_char == '"':
    #             self._string()
    #         elif current_char == "'":
    #             self._char()
    #         elif current_char in [">", "<", "="]:
    #             self._relacionais()
    #         else:
    #             self._operator_or_delimiter()
    #     return self.tokens

    def tokenize(self):
        while self.pos < len(self.code):
            current_char = self.code[self.pos]

            if current_char.isspace():
                self._advance_whitespace(current_char)
            elif current_char == '/' and self._peek_next() == '/':
                self.comentario_simples()
            elif current_char == '{':
                self.comentario_multilinha()
            elif current_char.isalpha():
                #self._logicos()
                self._identificador_ou_palavrachave()
            elif current_char.isdigit():
                self._number()
            elif current_char == '"':
                self._string()
            elif current_char == "'":
                self._char()
            elif current_char.isdigit() or current_char in "$&":
                self._number()
            elif current_char == ">" or current_char == "<" or current_char == "=":
                self._relacionais()
            else:
                self._operator_or_delimiter()
        return self.tokens

    def _peek_next(self):
        if self.pos + 1 < len(self.code):
            return self.code[self.pos + 1]
        return ''

    def comentario_simples(self):
        # avanca ate o fim da linha ou fim do codigo
        while self.pos < len(self.code) and self.code[self.pos] != '\n':
            self._advance()
        # avanca o '\n' tambem para proxima linha
        if self.pos < len(self.code) and self.code[self.pos] == '\n':
            # atualiza a linha e a coluna
            self.line += 1
            self.col = 1
            self.pos += 1

    def comentario_multilinha(self):
        start_line = self.line
        start_col = self.col
        self._advance()  # avanca o '{'
        while self.pos < len(self.code) and self.code[self.pos] != '}':
            if self.code[self.pos] == '\n':
                self.line += 1
                self.col = 1
                self._advance()
            else:
                self._advance()
        if self.pos < len(self.code) and self.code[self.pos] == '}':
            self._advance()
        else:
            self.tokens.append(("ERROR", "Comentário multi-linha não fechado", start_line, start_col))

    def _advance(self):
        self.pos += 1
        self.col += 1

    def _advance_whitespace(self, char):
        if char == '\n':
            self.line += 1
            self.col = 1
        elif char == '\t':
            self.col += 4  # considera tabulacao como 4 colunas
        else:
            self.col += 1
        self.pos += 1
    
    def _logicos(self):
        """Operadores logicos"""
        start_col = self.col
        start_pos = self.pos
        
        while self.pos < len(self.code) and self.code[self.pos].isalnum():
            self._advance()
        
        lexeme = self.code[start_pos:self.pos]
        
        if lexeme in TIPO_TOKENS["LOGICOS"]:
            self.tokens.append(("LOGICOS", lexeme, self.line, start_col))
        else:
            #pode dar prolema esse else de erro
            self.tokens.append(("ERROR", f"Token desconhecido {lexeme}", self.line, start_col))

    def _char(self):
        start_col = self.col
        start_line = self.line
        self._advance()

        start_content = self.pos
        while self.pos < len(self.code) and self.code[self.pos] != "'":
            self._advance()

        char_content = self.code[start_content:self.pos]

        if len(char_content) == 1 and self.pos < len(self.code) and self.code[self.pos] == "'":
            self._advance()
            self.tokens.append(("CHAR", char_content, start_line, start_col))
        else:
            self.tokens.append(("ERROR", "Char mal formado: deve conter exatamente 1 caractere", start_line, start_col))
            if self.pos < len(self.code) and self.code[self.pos] == "'":
                self._advance()

    def _identificador_ou_palavrachave(self):
        start_pos = self.pos
        start_col = self.col
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == "_"):
            self._advance()
        lexeme = self.code[start_pos:self.pos]
        lexeme_lower = lexeme.lower()
        if lexeme_lower in TIPO_TOKENS["PALAVRA-CHAVE"]:
            token_type = "PALAVRA-CHAVE"
            token_name = lexeme
        elif lexeme_lower in TIPO_TOKENS["OPERADORES"]:
            token_type = TIPO_TOKENS["OPERADORES"][lexeme_lower]
            token_name = lexeme
        else:
            token_type = "IDENTIFICADOR"
            token_name = lexeme
        self.tokens.append((token_type, token_name, self.line, start_col))

    def _number(self):
        start_pos = self.pos
        start_col = self.col

        if self.code[self.pos] == '$':
            self._advance()
            start_hex = self.pos
            while self.pos < len(self.code) and self.code[self.pos].isalnum():
                if self.code[self.pos].upper() not in "0123456789ABCDEF":
                    self.tokens.append(("ERROR", "Hexadecimal mal formado", self.line, start_col))
                    return
                self._advance()
            lexeme = self.code[start_pos:self.pos]
            if self.pos == start_hex:
                self.tokens.append(("ERROR", "Hexadecimal vazio", self.line, start_col))
            else:
                self.tokens.append(("NUMBER_HEX", lexeme, self.line, start_col))

        elif self.code[self.pos] == '&':
            self._advance()
            start_octal = self.pos
            while self.pos < len(self.code) and self.code[self.pos].isdigit():
                if self.code[self.pos] not in "01234567":
                    self.tokens.append(("ERROR", "Octal mal formado", self.line, start_col))
                    return
                self._advance()
            lexeme = self.code[start_pos:self.pos]
            if self.pos == start_octal:
                self.tokens.append(("ERROR", "Octal vazio", self.line, start_col))
            else:
                self.tokens.append(("NUMBER_OCT", lexeme, self.line, start_col))

        else:
            has_dot = False
            while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == "."):
                if self.code[self.pos] == ".":
                    if has_dot:
                        self.tokens.append(("ERROR", "Número real mal formado (ponto duplo)", self.line, start_col))
                        break
                        return
                    if self.pos + 1 < len(self.code) and self.code[self.pos + 1] == ".":
                        break
                    has_dot = True
                self._advance()
            lexeme = self.code[start_pos:self.pos]
            if lexeme.endswith("."):
                self.tokens.append(("ERROR", "Número real mal formado (ponto final)", self.line, start_col))
            elif lexeme.count(".") > 1:
                self.tokens.append(("ERROR", "Número mal formado com múltiplos pontos", self.line, start_col))
            else:
                tipo = "NUMBER_REAL" if has_dot else "NUMBER_INT"
                self.tokens.append((tipo, lexeme, self.line, start_col))

    # def _string(self):
    #     start_col = self.col
    #     start_line = self.line
    #     self._advance()
    #     lexeme = []

    #     while self.pos < len(self.code):
    #         current_char = self.code[self.pos]

    #         if current_char == '\n':
    #             self.tokens.append(("ERROR", "String não fechada antes de nova linha", start_line, start_col))
    #             return

    #         if current_char == '"':
    #             self._advance()
    #             self.tokens.append(("STRING", ''.join(lexeme), start_line, start_col))
    #             return
            

    #         lexeme.append(current_char)
    #         self._advance()

    #     self.tokens.append(("ERROR", "String não fechada", start_line, start_col))

    def _string(self):
        """Tratamento das strings"""
        start_col = self.col
        start_line = self.line  # linha inicial
        self._advance() 
        lexeme = []

        while self.pos < len(self.code):
            current_char = self.code[self.pos]

            if current_char == '\n':
                # em tese erro para string q n fecha na linha
                self.tokens.append(("ERROR", "String não fechada antes de nova linha", start_line, start_col))
                return

            if current_char == '"':
                # Fecha a string
                self._advance() 
                self.tokens.append(("STRING", ''.join(lexeme), start_line, start_col))
                return

            if current_char == '\\':
                '''possivelmente fazendo algo errado tem que olhar'''
                self._advance()  
                if self.pos >= len(self.code):
                    self.tokens.append(("ERROR", "Escape incompleto", start_line, start_col))
                    return

                escape_char = self.code[self.pos]
                if escape_char == 'n':
                    lexeme.append('\n')
                elif escape_char == 't':
                    lexeme.append('\t')
                elif escape_char == 'r':
                    lexeme.append('\r')
                elif escape_char == '\\':
                    lexeme.append('\\')   
                else:
                    lexeme.append('\\')  
                    lexeme.append(escape_char)
                self._advance()  
            else:
                # Caractere normal
                lexeme.append(current_char)
                self._advance()

        # string nao fechada
        self.tokens.append(("ERROR", "String não fechada", start_line, start_col))

    # def _relacionais(self):
    #     start_col = self.col
    #     dois_char_op = self.code[self.pos:self.pos+2]
    #     if dois_char_op in TIPO_TOKENS["RELACIONAIS"]:
    #         self.tokens.append((TIPO_TOKENS["RELACIONAIS"][dois_char_op], dois_char_op, self.line, start_col))
    #         self._advance()
    #         self._advance()
    #     elif self.code[self.pos] in TIPO_TOKENS["RELACIONAIS"]:
    #         lexeme = self.code[self.pos]
    #         self.tokens.append((TIPO_TOKENS["RELACIONAIS"][lexeme], lexeme, self.line, start_col))
    #         self._advance()
    #     else:
    #         self.tokens.append(("ERROR", "Operador relacional inválido", self.line, start_col))
    #         self._advance()
    
    def _relacionais(self):
        """Operadores relacionais e atribuição"""
        start_col = self.col
        dois_char_op = self.code[self.pos:self.pos+2]  

        #  ==, <=, >=, <>
        if dois_char_op in TIPO_TOKENS["RELACIONAIS"]:
            self.tokens.append((TIPO_TOKENS["RELACIONAIS"][dois_char_op], dois_char_op, self.line, start_col))
            self._advance()
            self._advance()
        #  '='
        elif self.code[self.pos] == '=':
            if (self.pos + 1 < len(self.code) and self.code[self.pos + 1].isalnum()) or (self.pos + 2 < len(self.code) and self.code[self.pos + 2].isalnum()):
                self.tokens.append(("EQUAL", "=", self.line, start_col))
            else:
                self.tokens.append((TIPO_TOKENS["RELACIONAIS"]["="], "=", self.line, start_col))
            self._advance()
        #  <, >
        elif self.code[self.pos] in TIPO_TOKENS["RELACIONAIS"]:
            lexeme = self.code[self.pos]
            self.tokens.append((TIPO_TOKENS["RELACIONAIS"][lexeme], lexeme, self.line, start_col))
            self._advance()
        else:
            self.tokens.append(("ERROR", f"Operador relacional inválido '{self.code[self.pos]}'", self.line, start_col))
            self._advance()

    def _operator_or_delimiter(self):
        start_col = self.col
        ch = self.code[self.pos]
        two_char_op = self.code[self.pos:self.pos+2]
        if two_char_op in TIPO_TOKENS["OPERADORES"]:
            self.tokens.append((TIPO_TOKENS["OPERADORES"][two_char_op], two_char_op, self.line, start_col))
            self._advance()
            self._advance()
        elif ch in TIPO_TOKENS["OPERADORES"]:
            self.tokens.append((TIPO_TOKENS["OPERADORES"][ch], ch, self.line, start_col))
            self._advance()
        elif ch in TIPO_TOKENS["DELIMITADOR"]:
            self.tokens.append((TIPO_TOKENS["DELIMITADOR"][ch], ch, self.line, start_col))
            self._advance()
        else:
            self._advance()

    def simulate_output(self):
        output = []
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            if token[0] == "PALAVRA-CHAVE" and token[1].lower() == "var":
                i += 1
                while i < len(self.tokens) and self.tokens[i][0] == "IDENTIFICADOR":
                    var_name = self.tokens[i][1]
                    i += 1
                    if i < len(self.tokens) and self.tokens[i][0] == "DOIS_PONTOS":
                        i += 1
                        tipo = self.tokens[i][1].lower()
                        if tipo == "char":
                            self.variables[var_name] = ''
                        elif tipo == "boolean":
                            self.variables[var_name] = False
                        else:
                            self.variables[var_name] = 0
                        self.var_types[var_name] = tipo
                        i += 1
                    if i < len(self.tokens) and self.tokens[i][0] == "PONTO_VIRGULA":
                        i += 1

            elif token[0] == "IDENTIFICADOR" and i+1 < len(self.tokens) and self.tokens[i+1][0] == "ASSIGN":
                var_name = token[1]
                var_type = self.var_types.get(var_name, "integer")
                i += 2
                expr = ""
                is_real = False
                is_boolean_expr = False
                assigned = False

                while i < len(self.tokens) and self.tokens[i][0] != "PONTO_VIRGULA":
                    t_type, lex, *_ = self.tokens[i]

                    if t_type in ["NUMBER_INT", "NUMBER_REAL", "NUMBER_HEX", "NUMBER_OCT", "IDENTIFICADOR"]:
                        if t_type == "IDENTIFICADOR":
                            val = self.variables.get(lex, 0)
                            expr += str(val)
                        elif t_type == "NUMBER_HEX":
                            expr += str(int(lex[1:], 16))
                        elif t_type == "NUMBER_OCT":
                            expr += str(int(lex[1:], 8))
                        elif t_type == "NUMBER_REAL":
                            expr += lex
                            is_real = True
                        elif t_type == "NUMBER_INT":
                            expr += lex
                    elif t_type in ["MENOR", "MAIOR", "IGUAL", "MENOR_IGUAL", "MAIOR_IGUAL", "DIFERENTE"]:
                        expr += f" {lex} "
                        is_boolean_expr = True
                    elif t_type == "PLUS":
                        expr += "+"
                    elif t_type == "MINUS":
                        expr += "-"
                    elif t_type == "MULT":
                        expr += "*"
                    elif t_type == "DIV":
                        expr += "/"
                        is_real = True
                    
                    elif t_type == "STRING":
                        if var_type == "string":
                            self.variables[var_name] = lex
                            assigned = True
                        else:
                            self.tokens.append(("ERROR", "Tipo incompatível: esperado string", token[2], token[3]))
                            assigned = True
                        i += 1
                        break
                    i += 1

                if assigned:
                    continue

                try:
                    if var_type == "boolean" or is_boolean_expr:
                        self.variables[var_name] = bool(eval(expr))
                    elif var_type == "real" or is_real:
                        self.variables[var_name] = float(eval(expr))
                    elif expr:
                        self.variables[var_name] = int(eval(expr))
                except:
                    self.variables[var_name] = "error"

            elif token[0] == "PALAVRA-CHAVE" and token[1].lower() == "writeln":
                if i+1 < len(self.tokens) and self.tokens[i+1][0] == "ABRE_PARENTESES":
                    i += 2
                    out_line = ""
                    while i < len(self.tokens) and self.tokens[i][0] != "FECHA_PARENTESES":
                        t_type, lex, *_ = self.tokens[i]
                        if t_type == "STRING":
                            out_line += lex
                        elif t_type == "CHAR":
                            out_line += lex
                        elif t_type == "IDENTIFICADOR":
                            out_line += str(self.variables.get(lex, "undefined"))
                        i += 1
                    output.append(out_line.strip())
            i += 1
        return output

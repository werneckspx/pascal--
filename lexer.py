from token_types import TIPO_TOKENS

class Lexer:
    """Classe Lexer para analisar o código fonte e gerar tokens."""
    def __init__(self, source_code):
        self.code = source_code
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        self.variables = {}
        self.var_types = {}

    def tokenize(self):
        """Método principal para tokenizar o código fonte."""
        while self.pos < len(self.code):
            current_char = self.code[self.pos]

            if current_char.isspace():
                self._avançar_espaco_em_branco_(current_char)
            elif current_char == '/' and self._olhar_proximo() == '/':
                self.comentario_simples()
            elif current_char == '{':
                self.comentario_multilinha()
            elif current_char.isalpha():
                self._identificador_ou_palavrachave_ou_logico() # Aqui dentro analisa se pode ser operador Lógico também #
            elif current_char.isdigit():
                self._numero()
            elif current_char == '"':
                self._string()
            elif current_char == "'":
                self._char()
            elif current_char.isdigit() or current_char in "$&":
                self._numero()
            elif current_char == ">" or current_char == "<" or current_char == "=":
                self._relacionais()
            else:
                self._operador_ou_delimitador_()
        return self.tokens

    def _olhar_proximo(self):
        """ Olha o próximo caractere sem avançar a posição """
        if self.pos + 1 < len(self.code):
            return self.code[self.pos + 1]
        return ''

    def comentario_simples(self):
        """ avanca ate o fim da linha ou fim do codigo """
        while self.pos < len(self.code) and self.code[self.pos] != '\n':
            self._advance()
        # avanca o '\n' tambem para proxima linha
        if self.pos < len(self.code) and self.code[self.pos] == '\n':
            # atualiza a linha e a coluna
            self.line += 1
            self.col = 1
            self.pos += 1

    def comentario_multilinha(self):
        """Tratamento de comentario multi linha"""
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
        """Avança a posição do cursor no código fonte."""
        self.pos += 1
        self.col += 1

    def _avançar_espaco_em_branco_(self, char):
        """Avança os espaços em branco e atualiza a linha e coluna."""
        if char == '\n':
            self.line += 1
            self.col = 1
        elif char == '\t':
            self.col += 4  # considera tabulacao como 4 colunas
        else:
            self.col += 1
        self.pos += 1


    def _identificador_ou_palavrachave_ou_logico(self):
        """Tratamento de identificadores, palavras-chave e operadores lógicos"""
        start_pos = self.pos
        start_col = self.col

        # Avança enquanto for alfanumérico ou "_"
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == "_"):
            self._advance()

        lexeme = self.code[start_pos:self.pos]

        # Verifica se o lexema não está vazio
        if not lexeme:
            return

        lexeme_lower = lexeme.lower()

        # Verifica se é um operador lógico
        if lexeme_lower in TIPO_TOKENS["LOGICOS"]:
            token_number = TIPO_TOKENS["LOGICOS"][lexeme_lower]
            self.tokens.append((token_number, lexeme, self.line, start_col))
            return

        # Verifica se é uma palavra-chave
        if lexeme_lower in TIPO_TOKENS["PALAVRA-CHAVE"]:
            token_number = TIPO_TOKENS["PALAVRA-CHAVE"][lexeme_lower]
            self.tokens.append((token_number, lexeme, self.line, start_col))
            return

        # Caso contrário, trata como identificador
        self.tokens.append(("IDENTIFICADOR", lexeme, self.line, start_col))

    def _numero(self):
        """Tratamento de números"""
        start_pos = self.pos
        start_col = self.col

        # verifica hexadecimal "$"
        if self.code[self.pos] == '$':
            self._advance()
            start_hex = self.pos
            # Verifica se o próximo caractere é um dígito hexadecimal
            while self.pos < len(self.code) and self.code[self.pos].isalnum():
                if self.code[self.pos].upper() not in "0123456789ABCDEF":
                    self.tokens.append(("ERROR", "Hexadecimal mal formado", self.line, start_col))
                    return
                self._advance()
            lexeme = self.code[start_pos:self.pos]
            if self.pos == start_hex:
                self.tokens.append(("ERROR", "Hexadecimal vazio", self.line, start_col))
            else:
                self.tokens.append(("NUMERO_HEX", lexeme, self.line, start_col))

        #verifica hexadecimal "0x"
        elif self.code[self.pos] == '0' and self.pos + 1 < len(self.code) and self.code[self.pos + 1] in ['x', 'X']:
            self._advance()  # avança o 0
            self._advance()  # avança o x
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

        ## Verifica se o caractere é um dígito octal
        elif (self.code[self.pos] == '&' or ((self.code[self.pos] == '0') and (self.code[self.pos+1] in "1234567" ))):
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
                self.tokens.append(("NUMERO_OCT", lexeme, self.line, start_col))

        ## Verifica se o caractere é um dígito decimal
        else:
            has_dot = False
            while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == "."):
                if self.code[self.pos] == ".":
                    if has_dot:
                        self.tokens.append(("ERROR", "Número real mal formado (ponto duplo)", self.line, start_col))
                        break
                    if self.pos + 1 < len(self.code):
                        next_char = self.code[self.pos + 1]
                        if next_char == ".":
                            break
                        elif next_char.isdigit():
                            pass 
                        elif next_char in (" ", "\n", ";", ")", ","):
                            pass 
                        else:
                            self.tokens.append(("ERROR", "Número real mal formado (caractere inválido após ponto)", self.line, start_col))
                            break
                    has_dot = True
                self._advance()
            
            lexeme = self.code[start_pos:self.pos]

            if has_dot:
                if lexeme.endswith("."):
                    lexeme += "0"
                else:
                    lexeme += "0" 

            tipo = "NUMBER_REAL" if has_dot else "NUMBER_INT"
            self.tokens.append((tipo, lexeme, self.line, start_col))


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
    
    def _relacionais(self):
        """Operadores relacionais e atribuição"""
        start_col = self.col
        dois_char_op = self.code[self.pos:self.pos+2]

        # ==, <=, >=, <>
        if dois_char_op in TIPO_TOKENS["RELACIONAIS"]:
            token_number = TIPO_TOKENS["RELACIONAIS"][dois_char_op]
            self.tokens.append((token_number, dois_char_op, self.line, start_col))
            self._advance()
            self._advance()
        # =, <, >
        elif self.code[self.pos] in TIPO_TOKENS["RELACIONAIS"]:
            token_number = TIPO_TOKENS["RELACIONAIS"][self.code[self.pos]]
            self.tokens.append((token_number, self.code[self.pos], self.line, start_col))
            self._advance()
        # erro
        else:
            self.tokens.append(("ERROR", f"Operador relacional inválido '{self.code[self.pos]}'", self.line, start_col))
            self._advance()


    def _operador_ou_delimitador_(self):
        """Tratamento de operadores e delimitadores"""
        start_col = self.col
        ch = self.code[self.pos]
        two_char_op = self.code[self.pos:self.pos+2]
        if two_char_op in TIPO_TOKENS["OPERADORES"]:
            token_number = TIPO_TOKENS["OPERADORES"][two_char_op]
            self.tokens.append((token_number, two_char_op, self.line, start_col))
            self._advance()
            self._advance()
        elif ch in TIPO_TOKENS["OPERADORES"]:
            token_number = TIPO_TOKENS["OPERADORES"][ch]
            self.tokens.append((token_number, ch, self.line, start_col))
            self._advance()
        elif ch in TIPO_TOKENS["DELIMITADOR"]:
            token_number = TIPO_TOKENS["DELIMITADOR"][ch]
            self.tokens.append((token_number, ch, self.line, start_col))
            self._advance()
        else:
            self.tokens.append(("ERROR", f"Caractere inválido '{ch}'", self.line, start_col))
            self._advance()

class Sintatic:
    def __init__(self, tokens):
        """
        Inicializa o sintatico com a lista de tokens.
        :param tokens: Lista de tokens gerada pelo lexer.
        """
        self.tokens = tokens
        self.current_index = 0

    def token_atual(self):
        """
        Retorna o token atual na lista de tokens.
        :return: Token atual ou None se não houver mais tokens.
        """
        if self.current_index < len(self.tokens):
            return self.tokens[self.current_index]  # Retorna a tupla completa
        return None

    def consumir(self, numero_esperado):
        """
        Consome o token atual se ele corresponder ao número esperado.
        Caso contrário, lança um erro de sintaxe.
        :param numero_esperado: Número que representa o tipo esperado do token.
        """
        token = self.token_atual()
        if token:
            tipo_token, lexeme, linha, coluna = token

            # Verifica se o número do tipo do token corresponde ao esperado
            if int(tipo_token) == int(numero_esperado):
                print(f"Consumindo token: {numero_esperado}, Lexeme: {lexeme}")
                self.current_index += 1
            else:
                raise SyntaxError(f"Esperado '{numero_esperado}', mas encontrado '{tipo_token}' na linha {linha}, coluna {coluna}.")
        else:
            raise SyntaxError("Fim inesperado do arquivo.")

    def analisar_funcao(self):
        """
        Analisa a produção <function*>:
        'program' 'IDENTIFICADOR' ';' <declarations> 'begin' <stmtList> 'end' '.'
        """
        self.consumir(1)  # Consome 'program' (representado pelo número 1 no TIPO_TOKENS)
        self.consumir(44)  # Consome o identificador do programa (representado pelo número 44)
        self.consumir(29)  # Consome ';' (representado pelo número 29)
        self.analisar_declaracoes()
        self.consumir(7)  # Consome 'begin' (representado pelo número 7)
        self.analisar_lista_comandos()
        self.consumir(8)  # Consome 'end' (representado pelo número 8)
        self.consumir(30)  # Consome '.' (representado pelo número 30)

    def analisar_declaracoes(self):
        """
        Analisa a produção <declarations>:
        'var' <declaration> <restoDeclaration>
        """
        if self.token_atual() and int(self.token_atual()[0]) == 2:  # 'var' é representado pelo número 2
            self.consumir(2)  # Consome 'var'
            self.analisar_declaracao()
            while self.token_atual() and int(self.token_atual()[0]) == 44:  # Identificadores são representados pelo número 44
                self.analisar_declaracao()

    def analisar_declaracao(self):
        """
        Analisa a produção <declaration>:
        <listaIdent> ':' <type> ';'
        """
        self.analisar_lista_identificadores()
        self.consumir(34)  # Consome ':' (representado pelo número 34)
        self.analisar_tipo()
        self.consumir(29)  # Consome ';' (representado pelo número 29)

    def analisar_lista_identificadores(self):
        """
        Analisa a produção <listaIdent>:
        'IDENTIFICADOR' <restoIdentList>
        """
        self.consumir(44)  # Consome um identificador
        while self.token_atual() and int(self.token_atual()[0]) == 31:  # ',' é representado pelo número 31
            self.consumir(31)  # Consome ','
            self.consumir(44)  # Consome outro identificador

    def analisar_tipo(self):
        """
        Analisa a produção <type>:
        'integer' | 'real' | 'string'
        """
        token = self.token_atual()
        if token and int(token[0]) in [3, 4, 5]:  # 'integer', 'real', 'string' são representados pelos números 3, 4 e 5
            self.consumir(int(token[0]))
        else:
            raise SyntaxError(f"Tipo inválido encontrado: '{token[1]}'.")

    def analisar_lista_comandos(self):
        """
        Analisa a produção <stmtList>.
        """
        # Aqui você pode implementar a lógica para analisar comandos específicos
        pass

    def analisar(self):
        """
        Inicia a análise sintática a partir da produção principal <function*>.
        """
        self.analisar_funcao()
        print("Parsing concluído com sucesso!")
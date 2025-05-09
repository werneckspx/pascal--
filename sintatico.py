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
        Analisa a produção <stmtList>:
        <stmtList> -> <stmt> <stmtList> | & ;
        """
        token = self.token_atual()
        if token is None:
            return  # lista vazia

        # Verifica se o token atual pode iniciar um <stmt>
        # Tokens que podem iniciar um stmt: for, read, write, readln, writeln, while, if, begin, break, continue, ;, identificador
        token_tipo = int(token[0])
        token_lexema = token[1].lower()

        # Mapear os tokens que iniciam stmt
        tokens_inicio_stmt = {
            9,  # for
            18, # write
            19, # writeln
            20, # read
            21, # readln
            11, # while
            15, # if
            7,  # begin
            13, # break
            14, # continue
            29, # ;
            44   # identificador
        }

        if token_tipo in tokens_inicio_stmt:
            self.analisar_stmt()
            self.analisar_lista_comandos()
        else:
            # Não é um token que inicia stmt, lista vazia
            return

    def analisar_stmt(self):
        """
        Analisa a produção <stmt>:
        <stmt> -> <forStmt> 
           | <ioStmt>
           | <whileStmt>
           | <atrib> ';'
           | <chamada_proc> ';'
           | <ifStmt> 
           | <bloco> 
           | 'break'';'
           | 'continue'';'
           | ';' ;
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar comando.")

        token_tipo = int(token[0])
        token_lexema = token[1].lower()

        if token_tipo == 9:  # for
            self.analisar_forStmt()
        elif token_tipo in {18, 19, 20, 21}:  # ioStmt
            self.analisar_ioStmt()
        elif token_tipo == 11:  # while
            self.analisar_whileStmt()
        elif token_tipo == 44:  # identificador (atrib ou chamada_proc)
            # Verifica se é atribuição ou chamada de procedimento
            next_token = self.tokens[self.current_index + 1] if self.current_index + 1 < len(self.tokens) else None
            if next_token and int(next_token[0]) == 28:  # ':='
                self.analisar_atrib()
                self.consumir(29)  # ';'
            else:
                self.analisar_chamada_proc()
                self.consumir(29)  # ';'
        elif token_tipo == 15:  # if
            self.analisar_ifStmt_sem_ponto_virgula()
            # Não consome ponto e vírgula aqui para evitar conflito com else
        elif token_tipo == 7:  # begin (bloco)
            self.analisar_bloco()
        elif token_tipo == 13:  # break
            self.consumir(13)
            self.consumir(29)
        elif token_tipo == 14:  # continue
            self.consumir(14)
            self.consumir(29)
        elif token_tipo == 29:  # ';'
            self.consumir(29)
        else:
            raise SyntaxError(f"Token inesperado '{token_lexema}' na linha {token[2]}, coluna {token[3]} ao analisar comando.")


    def analisar_ifStmt_sem_ponto_virgula(self):
        """
        Analisa a produção <ifStmt> sem consumir ponto e vírgula no final.
        Usado para evitar conflito com else encadeado.
        """
        self.consumir(15)  # if
        self.analisar_expr()
        self.consumir(17)  # then
        self.analisar_stmt()
        # Consome opcionalmente ';' antes do else
        token = self.token_atual()
        if token and int(token[0]) == 29:  # ';'
            self.consumir(29)
        self.analisar_elsePart()

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt> com consumo do ponto e vírgula no final.
        """
        self.analisar_ifStmt_sem_ponto_virgula()
        # Consome ponto e vírgula opcional após o ifStmt
        token = self.token_atual()
        if token and int(token[0]) == 29:
            self.consumir(29)

    def analisar_forStmt(self):
        """
        Analisa a produção <forStmt>:
        'for' <atrib> 'to' <endFor> 'do' <stmt> ;
        """
        self.consumir(9)  # for
        self.analisar_atrib()
        self.consumir(10)  # to
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar endFor.")
        if int(token[0]) == 44 or int(token[0]) == 45:  # IDENT ou NUMint
            self.consumir(int(token[0]))
        else:
            raise SyntaxError(f"Esperado IDENT ou NUMint em endFor, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")
        self.consumir(12)  # do
        self.analisar_stmt()

    def analisar_ioStmt(self):
        """
        Analisa a produção <ioStmt>:
        'read' '(' 'IDENT' ')' ';' 
        | 'write' '(' <outList> ')' ';' ;
        | 'readln' '(' 'IDENT' ')' ';'
        | 'writeln' '(' <outList> ')' ';' ;
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar ioStmt.")

        token_tipo = int(token[0])

        if token_tipo in {20, 21}:  # read ou readln
            self.consumir(token_tipo)
            self.consumir(32)  # '('
            self.consumir(44)  # IDENT
            self.consumir(33)  # ')'
            self.consumir(29)  # ';'
        elif token_tipo in {18, 19}:  # write ou writeln
            self.consumir(token_tipo)
            self.consumir(32)  # '('
            self.analisar_outList()
            self.consumir(33)  # ')'
            self.consumir(29)  # ';'
        else:
            raise SyntaxError(f"Esperado comando de IO, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")

    def analisar_outList(self):
        """
        Analisa a produção <outList>:
        <out> <restoOutList>
        """
        self.analisar_out()
        self.analisar_restoOutList()

    def analisar_restoOutList(self):
        """
        Analisa a produção <restoOutList>:
        ',' <outList> | &
        """
        token = self.token_atual()
        if token and int(token[0]) == 31:  # ','
            self.consumir(31)
            self.analisar_outList()
        else:
            return

    def analisar_out(self):
        """
        Analisa a produção <out>:
        'STR' | 'IDENT' | 'NUMint' | 'NUMfloat' [ ':' NUMint [ ':' NUMint ] ]
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar out.")

        token_tipo = int(token[0])
        if token_tipo == 49:  # STR
            self.consumir(49)
        elif token_tipo == 44:  # IDENT
            self.consumir(44)
            # Verifica se há formatação :NUMint[:NUMint]
            token = self.token_atual()
            if token and int(token[0]) == 34:  # ':'
                self.consumir(34)
                token = self.token_atual()
                if token and int(token[0]) == 45:  # NUMint
                    self.consumir(45)
                    token = self.token_atual()
                    if token and int(token[0]) == 34:  # ':'
                        self.consumir(34)
                        token = self.token_atual()
                        if token and int(token[0]) == 45:  # NUMint
                            self.consumir(45)
        elif token_tipo == 45:  # NUMint
            self.consumir(45)
            # Verifica se há formatação :NUMint[:NUMint]
            token = self.token_atual()
            if token and int(token[0]) == 34:  # ':'
                self.consumir(34)
                token = self.token_atual()
                if token and int(token[0]) == 45:  # NUMint
                    self.consumir(45)
                    token = self.token_atual()
                    if token and int(token[0]) == 34:  # ':'
                        self.consumir(34)
                        token = self.token_atual()
                        if token and int(token[0]) == 45:  # NUMint
                            self.consumir(45)
        elif token_tipo == 46:  # NUMfloat
            self.consumir(46)
        else:
            raise SyntaxError(f"Esperado STR, IDENT, NUMint ou NUMfloat, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")

    def analisar_whileStmt(self):
        """
        Analisa a produção <whileStmt>:
        'while' <expr> 'do' <stmt> ;
        """
        self.consumir(11)  # while
        self.analisar_expr()
        self.consumir(12)  # do
        self.analisar_stmt()

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt>:
        'if' <expr> 'then' <stmt> [ ';' ] <elsePart> ;
        """
        self.consumir(15)  # if
        self.analisar_expr()
        self.consumir(17)  # then
        self.analisar_stmt()
        # Removido consumo opcional de ';' após ifStmt para evitar conflito com else
        self.analisar_elsePart()

    def analisar_elsePart(self):
        """
        Analisa a produção <elsePart>:
        'else' <stmt> | &
        """
        token = self.token_atual()
        if token and int(token[0]) == 16:  # else
            self.consumir(16)
            # Permitir else if sem ponto e vírgula entre eles
            token_seguinte = self.token_atual()
            if token_seguinte and int(token_seguinte[0]) == 15:  # if
                self.analisar_ifStmt_sem_ponto_virgula()
            else:
                self.analisar_stmt()
        else:
            return

    def analisar_bloco(self):
        """
        Analisa a produção <bloco>:
        'begin' <stmtList> 'end' ';' ;
        """
        self.consumir(7)  # begin
        self.analisar_lista_comandos()
        self.consumir(8)  # end
        self.consumir(29)  # ';'

    def analisar_atrib(self):
        """
        Analisa a produção <atrib>:
        'IDENT' ':=' <expr> ;
        """
        self.consumir(44)  # IDENT
        self.consumir(28)  # ':='
        self.analisar_expr()

    def analisar_expr(self):
        """
        Analisa a produção <expr>:
        <or> ;
        """
        self.analisar_or()

    def analisar_or(self):
        """
        Analisa a produção <or>:
        <and> <restoOr> ;
        """
        self.analisar_and()
        self.analisar_restoOr()

    def analisar_restoOr(self):
        """
        Analisa a produção <restoOr>:
        'or' <and> <restoOr> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == 35:  # or
            self.consumir(35)
            self.analisar_and()
            self.analisar_restoOr()
        else:
            return

    def analisar_and(self):
        """
        Analisa a produção <and>:
        <not> <restoAnd> ;
        """
        self.analisar_not()
        self.analisar_restoAnd()

    def analisar_restoAnd(self):
        """
        Analisa a produção <restoAnd>:
        'and' <not> <restoAnd> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == 36:  # and
            self.consumir(36)
            self.analisar_not()
            self.analisar_restoAnd()
        else:
            return

    def analisar_not(self):
        """
        Analisa a produção <not>:
        'not' <not> | <rel> ;
        """
        token = self.token_atual()
        if token and int(token[0]) == 37:  # not
            self.consumir(37)
            self.analisar_not()
        else:
            self.analisar_rel()

    def analisar_rel(self):
        """
        Analisa a produção <rel>:
        <add> <restoRel> ;
        """
        self.analisar_add()
        self.analisar_restoRel()

    def analisar_restoRel(self):
        """
        Analisa a produção <restoRel>:
        '==' <add> | '<>' <add>
                | '<' <add> | '<=' <add> 
                | '>' <add> | '>=' <add> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) in {38, 39, 40, 42, 41, 43}:
            self.consumir(int(token[0]))
            self.analisar_add()
        else:
            return

    def analisar_add(self):
        """
        Analisa a produção <add>:
        <mult> <restoAdd> ;
        """
        self.analisar_mult()
        self.analisar_restoAdd()

    def analisar_restoAdd(self):
        """
        Analisa a produção <restoAdd>:
        '+' <mult> <restoAdd> 
        | '-' <mult> <restoAdd> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) in {22, 23}:
            self.consumir(int(token[0]))
            self.analisar_mult()
            self.analisar_restoAdd()
        else:
            return

    def analisar_mult(self):
        """
        Analisa a produção <mult>:
        <uno> <restoMult> ;
        """
        self.analisar_uno()
        self.analisar_restoMult()

    def analisar_restoMult(self):
        """
        Analisa a produção <restoMult>:
        '*' <uno> <restoMult>
        |  '/' <uno> <restoMult> 
        |  'mod' <uno> <restoMult> | & ;
        |  'div' <uno> <restoMult> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) in {24, 25, 26, 27}:
            self.consumir(int(token[0]))
            self.analisar_uno()
            self.analisar_restoMult()
        else:
            return

    def analisar_uno(self):
        """
        Analisa a produção <uno>:
        '+' <uno> | '-' <uno> | <fator> ;
        """
        token = self.token_atual()
        if token and int(token[0]) in {22, 23}:
            self.consumir(int(token[0]))
            self.analisar_uno()
        else:
            self.analisar_fator()

    def analisar_fator(self):
        """
        Analisa a produção <fator>:
        'NUMint' | 'NUMfloat' 
        | 'IDENT'  | '(' <expr> ')' | 'STR' ;
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar fator.")

        token_tipo = int(token[0])
        if token_tipo in {45, 46, 44, 49}:
            self.consumir(token_tipo)
        elif token_tipo == 32:  # '('
            self.consumir(32)
            self.analisar_expr()
            self.consumir(33)
        else:
            raise SyntaxError(f"Token inesperado '{token[1]}' na linha {token[2]}, coluna {token[3]} ao analisar fator.")

    def analisar(self):
        """
        Inicia a análise sintática a partir da produção principal <function*>.
        """
        self.analisar_funcao()
        print("Parsing concluído com sucesso!")

    def analisar_chamada_proc(self):
        """
        Analisa uma chamada de procedimento simples:
        'IDENT' ';'
        """
        self.consumir(44)  # IDENT

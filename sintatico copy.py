from token_types import TIPO_TOKENS

# Dicionários de grupos de tokens para uso em vários lugares
TOKENS_INICIO_STMT = {
    TIPO_TOKENS["PALAVRA-CHAVE"]["for"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["write"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["read"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["readln"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["while"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["if"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["begin"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["break"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["continue"],
    TIPO_TOKENS["DELIMITADOR"][";"],
    TIPO_TOKENS["IDENTIFICADOR"]
}

TOKENS_TIPOS_DECLARACAO = {
    TIPO_TOKENS["PALAVRA-CHAVE"]["integer"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["real"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["string"], 
    TIPO_TOKENS["PALAVRA-CHAVE"]["boolean"]
}


TOKENS_IO = {
    TIPO_TOKENS["PALAVRA-CHAVE"]["write"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["read"],
    TIPO_TOKENS["PALAVRA-CHAVE"]["readln"]
}

TOKENS_OPERADORES_BINARIOS = {
    TIPO_TOKENS["OPERADORES"]["+"],
    TIPO_TOKENS["OPERADORES"]["-"],
    TIPO_TOKENS["OPERADORES"]["*"],
    TIPO_TOKENS["OPERADORES"]["/"],
    TIPO_TOKENS["OPERADORES"]["mod"],
    TIPO_TOKENS["OPERADORES"]["div"]
}

TOKENS_NUMERICOS = {
    TIPO_TOKENS["NUMBER_INT"],
    TIPO_TOKENS["NUMBER_REAL"],
    TIPO_TOKENS["NUMBER_HEX"],
    TIPO_TOKENS["NUMERO_OCT"]
}

TOKENS_FATOR = {
    TIPO_TOKENS["IDENTIFICADOR"],
    TIPO_TOKENS["NUMBER_INT"],
    TIPO_TOKENS["NUMBER_REAL"],
    TIPO_TOKENS["NUMBER_HEX"],
    TIPO_TOKENS["NUMERO_OCT"],
    TIPO_TOKENS["STRING"]
}

class Sintatic:
    def __init__(self, tokens):
        """
        Inicializa o sintatico com a lista de tokens.
        :param tokens: Lista de tokens gerada pelo lexer.
        """
        self.tokens = tokens
        self.current_index = 0

        # Cria dicionário inverso para mapear número do token para lexema
        self.numero_para_lexema = {}

        for categoria, mapeamento in TIPO_TOKENS.items():
            if isinstance(mapeamento, dict):
                for lexema, numero in mapeamento.items():
                    self.numero_para_lexema[numero] = lexema
            else:
                self.numero_para_lexema[mapeamento] = categoria

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
        """
        token = self.token_atual()
        if token:
            tipo_token, lexeme, linha, coluna = token

            # Verifica se o número do tipo do token corresponde ao esperado
            if tipo_token == numero_esperado:
                print(f"Consumindo token: {numero_esperado}, Lexeme: {lexeme}")
                self.current_index += 1
            else:
                lexema_esperado = self.numero_para_lexema.get(numero_esperado, numero_esperado) 
                raise SyntaxError(f"Esperado token '{lexema_esperado}', mas encontrado token '{lexeme}' na linha {linha}, coluna {coluna}.")
        else:
            raise SyntaxError("Fim inesperado do arquivo ao analisar comando.")

    def analisar_funcao(self):
        """
        Analisa a produção <function*>:
        'program' 'IDENTIFICADOR' ';' <declarations> 'begin' <stmtList> 'end' '.'
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["program"])  # Consome 'program'
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # Consome o identificador do programa
        self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # Consome ';'
        self.analisar_declaracoes()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["begin"])  # Consome 'begin'
        self.analisar_lista_comandos()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["end"])  # Consome 'end'
        self.consumir(TIPO_TOKENS["DELIMITADOR"]["."])  # Consome '.'

    def analisar_declaracoes(self):
        """
        Analisa a produção <declarations>:
        'var' <declaration> <restoDeclaration>
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["var"])  # Consome 'var'
        self.analisar_declaracao()
        self.resto_declaration()
        
    def resto_declaration(self):
        """
        Analisa a produção <restoDeclaration>:
        <declaration> <restoDeclaration> | & ;
        """
        self.analisar_declaracao()
        if self.token_atual() and int(self.token_atual()[0]) != TIPO_TOKENS["PALAVRA-CHAVE"]["begin"]:    
            self.resto_declaration()

    def analisar_declaracao(self):
        """
        Analisa a produção <declaration>:
        <listaIdent> ':' <type> ';'
        """
        self.analisar_lista_identificadores()
        self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])  # Consome ':'
        self.analisar_tipo()
        self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # Consome ';'

    def analisar_lista_identificadores(self):
        """
        Analisa a produção <listaIdent>:
        'IDENTIFICADOR' <restoIdentList>
        """
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # Consome um identificador
        self.resto_lista_identificadores()
        
    def resto_lista_identificadores(self):
        """
        Analisa a produção <restoIdentList>:
        ',' 'IDENTIFICADOR' <restoIdentList> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][","]:  # ','
            self.consumir(TIPO_TOKENS["DELIMITADOR"][","])
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
            self.resto_lista_identificadores()
        # senão, faz nada (vazio)

    def analisar_tipo(self):
        """
        Analisa a produção <type>:
        'integer' | 'real' | 'string' | 'boolean'
        """
        token = self.token_atual()
        if token and int(token[0]) in  TOKENS_TIPOS_DECLARACAO:
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

        if token_tipo in TOKENS_INICIO_STMT:
            self.analisar_stmt()
            self.analisar_lista_comandos()
        else:
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

        if token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["for"]:  # for
            self.analisar_forStmt()
        elif token_tipo in TOKENS_IO:  # ioStmt
            self.analisar_ioStmt()
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["while"]:  # while
            self.analisar_whileStmt()
        elif token_tipo ==  TIPO_TOKENS["IDENTIFICADOR"]:  # identificador (atrib ou chamada_proc)
            # Verifica se é atribuição ou chamada de procedimento
            next_token = self.tokens[self.current_index + 1] if self.current_index + 1 < len(self.tokens) else None
            if next_token and int(next_token[0]) ==  TIPO_TOKENS["OPERADORES"][":="]:  # ':='
                self.analisar_atrib()
                self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
            elif next_token and int(next_token[0]) == TIPO_TOKENS["DELIMITADOR"][";"]:  # ';'
                self.analisar_chamada_proc()
                self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';
            else:
                # Erro: identificador não seguido de ':=' ou ';'
                linha = token[2]
                coluna = token[3]
                raise SyntaxError(f"Esperado ':=' ou ';' após identificador, mas encontrado '{next_token[1] if next_token else 'EOF'}' na linha {linha}, coluna {coluna}.")
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["if"]:  # if
            self.analisar_ifStmt()
            # Não consome ponto e vírgula aqui para evitar conflito com else
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["begin"]:  # begin (bloco)
            self.analisar_bloco()
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["break"]:  # break
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["break"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["continue"]:  # continue
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["continue"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        elif token_tipo == TIPO_TOKENS["DELIMITADOR"][";"]:  # ';'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        else:
            raise SyntaxError(f"Token inesperado '{token_lexema}' na linha {token[2]}, coluna {token[3]} ao analisar comando.")

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt> sem consumir ponto e vírgula no final.
        Usado para evitar conflito com else encadeado.
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["if"])  # if
        self.analisar_expr()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["then"])  # then
        self.analisar_stmt()
        # Removido consumo opcional de ';' antes do else para if e else não precisarem de ';'
        self.analisar_elsePart()

    def analisar_forStmt(self):
        """
        Analisa a produção <forStmt>:
        'for' <atrib> 'to' <endFor> 'do' <stmt> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["for"])  # for
        self.analisar_atrib()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["to"])  # to
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar endFor.")
        if int(token[0]) == TIPO_TOKENS["IDENTIFICADOR"] or int(token[0]) == TIPO_TOKENS["NUMBER_INT"]:  # IDENT ou NUMint
            self.consumir(int(token[0]))
        else:
            raise SyntaxError(f"Esperado IDENT ou NUMint em endFor, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["do"])  # do
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

        if token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["read"], TIPO_TOKENS["PALAVRA-CHAVE"]["readln"]}:  # read ou readln
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])  # '('
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])  # ')'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
        elif token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["write"], TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"]}:  # write ou writeln
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])  # '('
            self.analisar_outList()
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])  # ')'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
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
        if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][","]:  # ','
            self.consumir(TIPO_TOKENS["DELIMITADOR"][","])
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
        if token_tipo == TIPO_TOKENS["STRING"]:  # STR
            self.consumir(TIPO_TOKENS["STRING"])
        elif token_tipo == TIPO_TOKENS["IDENTIFICADOR"]:  # IDENT
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
            # Verifica se há formatação :NUMint[:NUMint]
            token = self.token_atual()
            if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][":"]:  # ':'
                self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])
                token = self.token_atual()
                if token and int(token[0]) == TIPO_TOKENS["NUMBER_INT"]:  # NUMint
                    self.consumir(TIPO_TOKENS["NUMBER_INT"])
                    token = self.token_atual()
                    if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][":"]:  # ':'
                        self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])
                        token = self.token_atual()
                        if token and int(token[0]) == TIPO_TOKENS["NUMBER_INT"]:  # NUMint
                            self.consumir(TIPO_TOKENS["NUMBER_INT"])
        elif token_tipo == TIPO_TOKENS["NUMBER_INT"]:  # NUMint
            self.consumir(TIPO_TOKENS["NUMBER_INT"])
            # Verifica se há formatação :NUMint[:NUMint]
            token = self.token_atual()
            if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][":"]:  # ':'
                self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])
                token = self.token_atual()
                if token and int(token[0]) == TIPO_TOKENS["NUMBER_INT"]:  # NUMint
                    self.consumir(TIPO_TOKENS["NUMBER_INT"])
                    token = self.token_atual()
                    if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][":"]:  # ':'
                        self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])
                        token = self.token_atual()
                        if token and int(token[0]) == TIPO_TOKENS["NUMBER_INT"]:  # NUMint
                            self.consumir(TIPO_TOKENS["NUMBER_INT"])
        elif token_tipo == TIPO_TOKENS["NUMBER_REAL"]:  # NUMfloat
            self.consumir(TIPO_TOKENS["NUMBER_REAL"])
        else:
            raise SyntaxError(f"Esperado STR, IDENT, NUMint ou NUMfloat, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")

    def analisar_whileStmt(self):
        """
        Analisa a produção <whileStmt>:
        'while' <expr> 'do' <stmt> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["while"])  # while
        self.analisar_expr()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["do"])  # do
        self.analisar_stmt()

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt>:
        'if' <expr> 'then' <stmt> [ ';' ] <elsePart> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["if"])  # if
        self.analisar_expr()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["then"])  # then
        self.analisar_stmt()
        # Removido consumo opcional de ';' após ifStmt para evitar conflito com else
        self.analisar_elsePart()

    def analisar_elsePart(self):
        """
        Analisa a produção <elsePart>:
        'else' <stmt> | &
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["PALAVRA-CHAVE"]["else"]:  # else
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["else"])
            # Permitir else if sem ponto e vírgula entre eles
            token_seguinte = self.token_atual()
            if token_seguinte and int(token_seguinte[0]) == TIPO_TOKENS["PALAVRA-CHAVE"]["if"]:  # if
                self.analisar_ifStmt()
            else:
                self.analisar_stmt()
        else:
            return

    def analisar_bloco(self):
        """
        Analisa a produção <bloco>:
        'begin' <stmtList> 'end' ';' ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["begin"])  # begin
        self.analisar_lista_comandos()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["end"])  # end
        self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'

    def analisar_atrib(self):
        """
        Analisa a produção <atrib>:
        'IDENT' ':=' <expr> ;
        """
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
        self.consumir(TIPO_TOKENS["OPERADORES"][":="])  # ':='
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
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["or"]:  # or
            self.consumir(TIPO_TOKENS["LOGICOS"]["or"])
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
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["and"]:  # and
            self.consumir(TIPO_TOKENS["LOGICOS"]["and"])
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
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["not"]:  # not
            self.consumir(TIPO_TOKENS["LOGICOS"]["not"])
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
        if token and int(token[0]) in {TIPO_TOKENS["RELACIONAIS"]["=="], TIPO_TOKENS["RELACIONAIS"]["<>"], TIPO_TOKENS["RELACIONAIS"]["<"], TIPO_TOKENS["RELACIONAIS"]["<="], TIPO_TOKENS["RELACIONAIS"][">"], TIPO_TOKENS["RELACIONAIS"][">="]}:
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
        if token and int(token[0]) in {TIPO_TOKENS["OPERADORES"]["+"], TIPO_TOKENS["OPERADORES"]["-"]}:  # '+' ou '-'
            op_token = token
            self.consumir(int(token[0]))
            next_token = self.token_atual()
            # Verifica se o próximo token é outro operador binário (+, -, *, /, mod, div)
            if next_token and int(next_token[0]) in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
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
        if token and int(token[0]) in  {TIPO_TOKENS["OPERADORES"]["*"], TIPO_TOKENS["OPERADORES"]["/"], TIPO_TOKENS["OPERADORES"]["mod"], TIPO_TOKENS["OPERADORES"]["div"]}:  # '*', '/', 'mod', 'div'
            op_token = token
            self.consumir(int(token[0]))
            next_token = self.token_atual()
            # Verifica se o próximo token é outro operador binário
            if next_token and int(next_token[0]) in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
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
        if token and int(token[0]) in {TIPO_TOKENS["OPERADORES"]["+"], TIPO_TOKENS["OPERADORES"]["-"]}:
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
        if token_tipo in TOKENS_FATOR:
            self.consumir(token_tipo)
        elif token_tipo == TIPO_TOKENS["DELIMITADOR"]["("]:  # '('
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])
            self.analisar_expr()
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])
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
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
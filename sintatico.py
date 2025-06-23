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

class GeradorAux:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0

    def nova_temp(self):
        nome = f"t{self.temp_count}"
        self.temp_count += 1
        return nome

    def novo_label(self):
        nome = f"L{self.label_count}"
        self.label_count += 1
        return nome

class Sintatic:
    def __init__(self, tokens):
        """
        Inicializa o sintatico com a lista de tokens.
        :param tokens: Lista de tokens gerada pelo lexer.
        """
        self.tokens = tokens
        self.current_index = 0
        self.gerador_aux = GeradorAux()  # Inicializa o gerador auxiliar
        self.codigos_intermediarios = []  # Lista para armazenar os códigos intermediários
        self.pilha_labels_fim_laco = []  # Pilha para armazenar labels de fim de laço para break
        
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
        
        if self.token_atual() and int(self.token_atual()[0]) != TIPO_TOKENS["PALAVRA-CHAVE"]["begin"]:    
            self.analisar_declaracao()
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
            codigos = self.analisar_ioStmt()
            self.codigos_intermediarios.extend(codigos)  # Adiciona os códigos intermediários gerados
            #self.analisar_ioStmt()
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
            if not self.pilha_labels_fim_laco:
                raise SyntaxError("Comando 'break' fora de laço não permitido.")
            label_fim = self.pilha_labels_fim_laco[-1]
            self.codigos_intermediarios.append(('Jump', label_fim, None, None))
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["break"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        elif token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["continue"]:  # continue
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["continue"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        elif token_tipo == TIPO_TOKENS["DELIMITADOR"][";"]:  # ';'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        else:
            raise SyntaxError(f"Token inesperado '{token_lexema}' na linha {token[2]}, coluna {token[3]} ao analisar comando.")

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
        codigos=[]
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar ioStmt.")

        token_tipo = int(token[0])

        if token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["read"], TIPO_TOKENS["PALAVRA-CHAVE"]["readln"]}:  # read ou readln
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])  # '('
            ident_token = self.token_atual()
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])  # ')'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
            codigos.append(('call', self.numero_para_lexema[token_tipo], ident_token[1], None))
        elif token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["write"], TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"]}:  # write ou writeln
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])  # '('
            out_codigos = self.analisar_outList()
            #self.analisar_outList()
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])  # ')'
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
            for arg in out_codigos:
                codigos.append(('call', self.numero_para_lexema[token_tipo], arg, None))
        else:
            raise SyntaxError(f"Esperado comando de IO, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")
        return codigos
    
    def analisar_outList(self):
        """
        Analisa a produção <outList>:
        <out> <restoOutList>
        """
        args = []
        arg = self.analisar_out()
        args.append(arg)
        args.extend(self.analisar_restoOutList())
        return args

    def analisar_restoOutList(self):
        """
        Analisa a produção <restoOutList>:
        ',' <outList> | &
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["DELIMITADOR"][","]:  # ','
            self.consumir(TIPO_TOKENS["DELIMITADOR"][","])
            return self.analisar_outList()
        else:
            return []

    def analisar_out(self):
        """
        Analisa a produção <out>:
        'STR' | 'IDENT' | 'NUMint' | 'NUMfloat' [ ':' NUMint [ ':' NUMint ] ]
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar out.")

        token_tipo = int(token[0])
        valor = None
        if token_tipo == TIPO_TOKENS["STRING"]:  # STR
            valor = token[1]  # Captura o valor da string
            self.consumir(TIPO_TOKENS["STRING"])
        elif token_tipo == TIPO_TOKENS["IDENTIFICADOR"]:  # IDENT
            valor = token[1]  # Captura o valor do identificador
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
            valor = token[1]  # Captura o valor do número inteiro
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
            valor = token[1]  # Captura o valor do número real
            self.consumir(TIPO_TOKENS["NUMBER_REAL"])
        else:
            raise SyntaxError(f"Esperado STR, IDENT, NUMint ou NUMfloat, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")
        return valor  # Retorna o valor do out analisado
    
    def analisar_whileStmt(self):
        """
        Analisa a produção <whileStmt>:
        'while' <expr> 'do' <stmt> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["while"])  # while

        label_inicio = self.gerador_aux.novo_label()
        label_verdadeiro = self.gerador_aux.novo_label()
        label_falso = self.gerador_aux.novo_label()

        # empilha o label de fim do laço
        self.pilha_labels_fim_laco.append(label_falso)

        # label do início do loop
        self.codigos_intermediarios.append(('Label', label_inicio, None, None))

        resultado, codigos = self.analisar_expr()
        self.codigos_intermediarios.extend(codigos)

        # salto condicional baseado na expressão
        self.codigos_intermediarios.append(('If', resultado, label_verdadeiro, label_falso))

        # label para o bloco verdadeiro (corpo do while)
        self.codigos_intermediarios.append(('Label', label_verdadeiro, None, None))

        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["do"])  # do
        self.analisar_stmt()

        # salto incondicional para o início do loop
        self.codigos_intermediarios.append(('Jump', label_inicio, None, None))

        # label para o bloco falso (fim do loop)
        self.codigos_intermediarios.append(('Label', label_falso, None, None))

        # desempilha o label de fim do laço após o laço
        self.pilha_labels_fim_laco.pop()

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt>:
        'if' <expr> 'then' <stmt> [ ';' ] <elsePart> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["if"])  # if
        resultado, codigos = self.analisar_expr()
        self.codigos_intermediarios.extend(codigos)
        temp_cond = resultado
        label_true = self.gerador_aux.novo_label()
        label_false = self.gerador_aux.novo_label()
        label_fim = self.gerador_aux.novo_label()
        # gera código intermediário para o salto condicional
        self.codigos_intermediarios.append(('If', temp_cond, label_true, label_false))
        
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["then"])  # then
        
        # label para o bloco verdadeiro
        self.codigos_intermediarios.append(('Label', label_true, None, None))
        self.analisar_stmt()
        # salto incondicional para o fim do if para pular o else
        self.codigos_intermediarios.append(('Jump', label_fim, None, None))
        
        # label para o bloco falso (else)
        self.codigos_intermediarios.append(('Label', label_false, None, None))
        self.analisar_elsePart()
        # label para o fim do if-else
        self.codigos_intermediarios.append(('Label', label_fim, None, None))

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
        ident_token = self.token_atual()
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
        self.consumir(TIPO_TOKENS["OPERADORES"][":="])  # ':='
        resultado, codigos_expr = self.analisar_add()
        self.codigos_intermediarios.extend(codigos_expr)  # Adiciona os códigos intermediários gerados
        self.codigos_intermediarios.append(('att', ident_token[1], resultado, None))  # Adiciona a atribuição

    def analisar_expr(self):
        """
        Analisa a produção <expr>:
        <or> ;
        """
        return self.analisar_or()

    def analisar_or(self):
        """
        Analisa a produção <or>:
        <and> <restoOr> ;
        """
        resultado, codigos = self.analisar_and()
        return self.analisar_restoOr(resultado, codigos)

    def analisar_restoOr(self, resultado_esq, codigos_esq):
        """
        Analisa a produção <restoOr>:
        'or' <and> <restoOr> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["or"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["or"])
            resultado_dir, codigos_dir = self.analisar_and()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('or', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoOr(temp, codigos)
        else:
            return resultado_esq, codigos_esq

    def analisar_and(self):
        """
        Analisa a produção <and>:
        <not> <restoAnd> ;
        """
        resultado, codigos = self.analisar_not()
        return self.analisar_restoAnd(resultado, codigos)

    def analisar_restoAnd(self, resultado_esq, codigos_esq):
        """
        Analisa a produção <restoAnd>:
        'and' <not> <restoAnd> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["and"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["and"])
            resultado_dir, codigos_dir = self.analisar_not()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('and', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAnd(temp, codigos)
        else:
            return resultado_esq, codigos_esq

    def analisar_not(self):
        """
        Analisa a produção <not>:
        'not' <not> | <rel> ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["LOGICOS"]["not"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["not"])
            resultado, codigos = self.analisar_not()
            temp = self.gerador_aux.nova_temp()
            codigos.append(('not', temp, resultado, None))
            return temp, codigos
        else:
            return self.analisar_rel()

    def analisar_rel(self):
        """
        Analisa a produção <rel>:
        <add> <restoRel> ;
        """
        resultado_esq, codigos_esq = self.analisar_add()
        return self.analisar_restoRel(resultado_esq, codigos_esq)

    def analisar_restoRel(self, resultado_esq, codigos_esq):
        """
        Analisa a produção <restoRel>:
        '==' <add> | '<>' <add> | '<' <add> | '<=' <add> | '>' <add> | '>=' <add> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) in {
            TIPO_TOKENS["RELACIONAIS"]["=="], TIPO_TOKENS["RELACIONAIS"]["<>"],
            TIPO_TOKENS["RELACIONAIS"]["<"], TIPO_TOKENS["RELACIONAIS"]["<="],
            TIPO_TOKENS["RELACIONAIS"][">"], TIPO_TOKENS["RELACIONAIS"][">="]
        }:
            op = self.numero_para_lexema[int(token[0])]
            self.consumir(int(token[0]))
            resultado_dir, codigos_dir = self.analisar_add()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [(op, temp, resultado_esq, resultado_dir)]
            return temp, codigos
        else:
            return resultado_esq, codigos_esq
        
    def analisar_add(self):
        """
        Analisa a produção <add>:
        <mult> <restoAdd> ;
        """
        resultado, codigos = self.analisar_mult()
        return self.analisar_restoAdd(resultado, codigos)

    def analisar_restoAdd(self, resultado_esq, codigos_esq):
        """
        Analisa a produção <restoAdd>:
        '+' <mult> <restoAdd> 
        | '-' <mult> <restoAdd> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["+"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["+"])
            resultado_dir, codigos_dir = self.analisar_mult()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('add', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAdd(temp, codigos)
        elif token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["-"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["-"])
            resultado_dir, codigos_dir = self.analisar_mult()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('sub', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAdd(temp, codigos)
        else:
            return resultado_esq, codigos_esq

    def analisar_mult(self):
        """
        Analisa a produção <mult>:
        <uno> <restoMult> ;
        """
        resultado, codigos = self.analisar_uno()
        return self.analisar_restoMult(resultado, codigos)

    def analisar_restoMult(self, resultado_esq, codigos_esq):
        """
        Analisa a produção <restoMult>:
        '*' <uno> <restoMult>
        |  '/' <uno> <restoMult> 
        |  'mod' <uno> <restoMult> | & ;
        |  'div' <uno> <restoMult> | & ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["*"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["*"])
            resultado_dir, codigos_dir = self.analisar_uno()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('mult', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos)
        elif token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["/"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["/"])
            resultado_dir, codigos_dir = self.analisar_uno()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('div', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos)
        elif token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["mod"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["mod"])
            resultado_dir, codigos_dir = self.analisar_uno()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('mod', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos)
        elif token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["div"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["div"])
            resultado_dir, codigos_dir = self.analisar_uno()
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('idiv', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos)
        else:
            return resultado_esq, codigos_esq

    def analisar_uno(self):
        """
        Analisa a produção <uno>:
        '+' <uno> | '-' <uno> | <fator> ;
        """
        token = self.token_atual()
        if token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["-"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["-"])
            resultado, codigos = self.analisar_uno()
            temp = self.gerador_aux.nova_temp()
            codigos.append(('sub', temp, 0, resultado))
            return temp, codigos
        elif token and int(token[0]) == TIPO_TOKENS["OPERADORES"]["+"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["+"])
            return self.analisar_uno()
        else:
            return self.analisar_fator()
        
    def analisar_fator(self):
        """
        Analisa a produção <fator>:
        'NUMint' | 'NUMfloat' | 'IDENT'  | '(' <expr> ')' | 'STR' ;
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar fator.")

        token_tipo = int(token[0])
        if token_tipo in {TIPO_TOKENS["IDENTIFICADOR"], TIPO_TOKENS["NUMBER_INT"], TIPO_TOKENS["NUMBER_REAL"]}:
            self.consumir(token_tipo)
            return token[1], []
        elif token_tipo == TIPO_TOKENS["DELIMITADOR"]["("]:
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])
            resultado, codigos = self.analisar_expr() # Analisar expressão dentro dos parênteses
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])
            return resultado, codigos
        else:
            raise SyntaxError(f"Token inesperado '{token[1]}' na linha {token[2]}, coluna {token[3]} ao analisar fator.")
    def analisar(self):
        """
        Inicia a análise sintática a partir da produção principal <function*>.
        """
        self.analisar_funcao()
        print("Parsing concluído com sucesso!")
        print("Códigos intermediários gerados:")
        for codigo in self.codigos_intermediarios:
            print(codigo)

    def analisar_chamada_proc(self):
        """
        Analisa uma chamada de procedimento simples:
        'IDENT' ';'
        """
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
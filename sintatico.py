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

TOKENS_FATOR = {
    TIPO_TOKENS["IDENTIFICADOR"],
    TIPO_TOKENS["NUMBER_INT"],
    TIPO_TOKENS["NUMBER_REAL"],
    TIPO_TOKENS["NUMBER_HEX"],
    TIPO_TOKENS["NUMERO_OCT"],
    TIPO_TOKENS["STRING"]
}

OPERADORES_RELACIONAIS_SIMBOLOS = {
    TIPO_TOKENS["RELACIONAIS"]["=="]: "eq",
    TIPO_TOKENS["RELACIONAIS"]["="]: "eq",
    TIPO_TOKENS["RELACIONAIS"]["<>"]: "neq",
    TIPO_TOKENS["RELACIONAIS"]["<"]: "less",
    TIPO_TOKENS["RELACIONAIS"]["<="]: "leq",
    TIPO_TOKENS["RELACIONAIS"][">"]: "gret",
    TIPO_TOKENS["RELACIONAIS"][">="]: "geq",
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
        self.tabela_tipos = {} 
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
                #print(f"Consumindo token: {numero_esperado}, Lexeme: {lexeme}")
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
        
        if self.token_atual() and self.token_atual()[0] != TIPO_TOKENS["PALAVRA-CHAVE"]["begin"]:    
            self.analisar_declaracao()
            self.resto_declaration()

    def analisar_declaracao(self):
        """
        Analisa a produção <declaration>:
        <listaIdent> ':' <type> ';'
        Gera código intermediário para atribuição inicial das variáveis.
        """
        idents = []
        token = self.token_atual()
        idents.append(token[1])
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
        while True:
            token = self.token_atual()
            if token and token[0] == TIPO_TOKENS["DELIMITADOR"][","]:
                self.consumir(TIPO_TOKENS["DELIMITADOR"][","])
                token = self.token_atual()
                idents.append(token[1])
                self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
            else:
                break
        self.consumir(TIPO_TOKENS["DELIMITADOR"][":"])  # Consome ':'
        token = self.token_atual()
        if token and token[0] in TOKENS_TIPOS_DECLARACAO:
            tipo = token[1].lower()
            self.consumir(token[0])
        else:
            raise SyntaxError(f"Tipo inválido encontrado: '{token[1]}'.")
        self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # Consome ';'

        # Valor padrão conforme o tipo
        if tipo in ("integer", "real", "boolean"):
            valor_inicial = "0"
        elif tipo == "string":
            valor_inicial = '""'
        else:
            valor_inicial = "0"  # fallback

        # Gera código intermediário de atribuição inicial
        for ident in idents:
            if ident in self.tabela_tipos:
                raise SyntaxError(f"Variável '{ident}' já declarada anteriormente.")
            # Verifica se é palavra reservada
            if ident.lower() in TIPO_TOKENS["PALAVRA-CHAVE"]:
                raise SyntaxError(f"Nome de variável '{ident}' é uma palavra reservada.")
            self.tabela_tipos[ident] = tipo
            self.codigos_intermediarios.append(('att', ident, valor_inicial, tipo))

    def analisar_lista_identificadores(self):
        """
        Analisa a produção <listaIdent>:
        'IDENTIFICADOR' <restoIdentList>
        (Agora apenas consome tokens, lógica de coleta está em analisar_declaracao)
        """
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
        self.resto_lista_identificadores()

    def resto_lista_identificadores(self):
        """
        Analisa a produção <restoIdentList>:
        ',' 'IDENTIFICADOR' <restoIdentList> | & ;
        (Agora apenas consome tokens, lógica de coleta está em analisar_declaracao)
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["DELIMITADOR"][","]:
            self.consumir(TIPO_TOKENS["DELIMITADOR"][","])
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
            self.resto_lista_identificadores()
        # senão, faz nada (vazio)

    def analisar_tipo(self):
        """
        Analisa a produção <type>:
        'integer' | 'real' | 'string' | 'boolean'
        (Agora apenas consome token, lógica de coleta está em analisar_declaracao)
        """
        token = self.token_atual()
        if token and token[0] in TOKENS_TIPOS_DECLARACAO:
            self.consumir(token[0])
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
        token_tipo = token[0]
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

        token_tipo = token[0]
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
            if next_token and next_token[0] ==  TIPO_TOKENS["OPERADORES"][":="]:  # ':='
                self.analisar_atrib()
                self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])  # ';'
            elif next_token and next_token[0] == TIPO_TOKENS["DELIMITADOR"][";"]:  # ';'
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
            if not self.pilha_labels_fim_laco or len(self.pilha_labels_fim_laco) < 2:
                raise SyntaxError("Comando 'continue' fora de laço não permitido.")
            label_inicio = self.pilha_labels_fim_laco[-2]  # Usar o label do início do laço para continue
            if label_inicio is None:
                raise SyntaxError("Label de início do laço não encontrado para comando 'continue'.")
            self.codigos_intermediarios.append(('Jump', label_inicio, None, None))
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["continue"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
        else:
            raise SyntaxError(f"Token inesperado '{token_lexema}' na linha {token[2]}, coluna {token[3]} ao analisar comando.")

    def analisar_forStmt(self):
        """
        Analisa a produção <forStmt>:
        'for' <atrib> 'to' <endFor> 'do' <stmt> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["for"]) 

        # Captura o nome da variável de controle do laço for na atribuição inicial
        ident_token = self.token_atual()
        if ident_token[0] != TIPO_TOKENS["IDENTIFICADOR"]:
            raise SyntaxError("Esperado identificador na atribuição inicial do for.")
        var_for = ident_token[1]

        self.analisar_atrib()
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["to"])

        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar endFor")
        if token[0] == TIPO_TOKENS["IDENTIFICADOR"] or token[0] == TIPO_TOKENS["NUMBER_INT"]:
            limite_final = token[1]
            self.consumir(token[0])
        else:
            raise SyntaxError(f"Esperado IDENT ou NUMint em endFor, mas encontrado '{token[1]}' na linha {token[2]}, coluna {token[3]}.")
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["do"])

        label_inicio = self.gerador_aux.novo_label()
        label_verdadeiro = self.gerador_aux.novo_label()
        label_falso = self.gerador_aux.novo_label()

        # empilha labels para controle de break e continue
        self.pilha_labels_fim_laco.append(label_falso)
        self.pilha_labels_fim_laco.append(label_inicio)

        self.codigos_intermediarios.append(('Label', label_inicio, None, None))

        temp_cond = self.gerador_aux.nova_temp()
        self.codigos_intermediarios.append(('less', temp_cond, var_for, limite_final)) #<

        # salto condicional para corpo do laço ou fim do laço
        self.codigos_intermediarios.append(('If', temp_cond, label_verdadeiro, label_falso))

        # label para corpo do laço
        self.codigos_intermediarios.append(('Label', label_verdadeiro, None, None))

        # self.analisar_stmt()
        self.analisar_lista_comandos()

        # incrementa a variável do for 
        self.codigos_intermediarios.append(('add', var_for, var_for, '1'))

        # salto incondicional para início do laço
        self.codigos_intermediarios.append(('Jump', label_inicio, None, None))

        # label para fim do laço
        self.codigos_intermediarios.append(('Label', label_falso, None, None))

        self.pilha_labels_fim_laco.pop()
        self.pilha_labels_fim_laco.pop()



    def analisar_ioStmt(self):
        """
        Analisa a produção <ioStmt>:
        'read' '(' 'IDENT' ')' ';' 
        | 'write' '(' <outList> ')' ';'
        | 'readln' '(' 'IDENT' ')' ';'
        | 'writeln' '(' <outList> ')' ';'
        """
        codigos = []
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar ioStmt.")

        token_tipo = token[0]
        #lexema_op = self.numero_para_lexema[token_tipo]

        if token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["read"], TIPO_TOKENS["PALAVRA-CHAVE"]["readln"]}:
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])
            ident_token = self.token_atual()
            self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])
            tipo = self.tabela_tipos.get(ident_token[1], None)
            codigos.append(('call', 'read', ident_token[1], tipo))
            
            # Se for readln, adiciona quebra de linha
            if token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["readln"]:
                codigos.append(('call', 'write', '"\n"', "string"))

        elif token_tipo in {TIPO_TOKENS["PALAVRA-CHAVE"]["write"], TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"]}:
            self.consumir(token_tipo)
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])
            out_codigos = self.analisar_outList()
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])
            self.consumir(TIPO_TOKENS["DELIMITADOR"][";"])

            for arg in out_codigos:
                if isinstance(arg, str):
                    if arg in self.tabela_tipos:
                        tipo = self.tabela_tipos[arg]
                    elif arg.startswith('"') and arg.endswith('"'):
                        tipo = "string"
                    elif arg.replace('.', '', 1).isdigit():
                        tipo = "real" if '.' in arg else "integer"
                    elif arg.lower() in ("true", "false"):
                        tipo = "boolean"
                    else:
                        tipo = None
                else:
                    tipo = None
                codigos.append(('call', 'write', arg, tipo))
            
            # Se for writeln, adiciona quebra de linha
            if token_tipo == TIPO_TOKENS["PALAVRA-CHAVE"]["writeln"]:
                codigos.append(('call', 'write', '"\n"', "string"))

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
        if token and token[0] == TIPO_TOKENS["DELIMITADOR"][","]:  # ','
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
                valor = token[1]
                self.consumir(TIPO_TOKENS["STRING"])
                valor = f'"{valor}"'
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

        # empilha o label de início e fim do laço para controle de break e continue
        self.pilha_labels_fim_laco.append(label_inicio)
        self.pilha_labels_fim_laco.append(label_falso)

        # label do início do loop
        self.codigos_intermediarios.append(('Label', label_inicio, None, None))
        resultado, codigos, tipo = self.analisar_expr()
        self.codigos_intermediarios.extend(codigos)

        # salto condicional baseado na expressão
        self.codigos_intermediarios.append(('If', resultado, label_verdadeiro, label_falso))

        # label para o bloco verdadeiro (corpo do while)
        self.codigos_intermediarios.append(('Label', label_verdadeiro, None, None))
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["do"])  # do
        # self.analisar_stmt()
        self.analisar_lista_comandos()

        # salto incondicional para o início do loop
        self.codigos_intermediarios.append(('Jump', label_inicio, None, None))

        # label para o bloco falso (fim do loop)
        self.codigos_intermediarios.append(('Label', label_falso, None, None))

        # desempilha os labels de início e fim do laço após o laço
        self.pilha_labels_fim_laco.pop()
        self.pilha_labels_fim_laco.pop()

    def analisar_ifStmt(self):
        """
        Analisa a produção <ifStmt>:
        'if' <expr> 'then' <stmt> [ ';' ] <elsePart> ;
        """
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["if"])  # if
        resultado, codigos, tipo = self.analisar_expr()
        self.codigos_intermediarios.extend(codigos)
        temp_cond = resultado
        label_true = self.gerador_aux.novo_label()
        label_false = self.gerador_aux.novo_label()
        label_fim = self.gerador_aux.novo_label()
        
        self.codigos_intermediarios.append(('If', temp_cond, label_true, label_false))
        self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["then"])  # then
        
        # label para o bloco verdadeiro
        self.codigos_intermediarios.append(('Label', label_true, None, None))
        # self.analisar_stmt()
        self.analisar_lista_comandos()
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
        if token and token[0] == TIPO_TOKENS["PALAVRA-CHAVE"]["else"]:  # else
            self.consumir(TIPO_TOKENS["PALAVRA-CHAVE"]["else"])
            # Permitir else if sem ponto e vírgula entre eles
            token_seguinte = self.token_atual()
            if token_seguinte and token_seguinte[0] == TIPO_TOKENS["PALAVRA-CHAVE"]["if"]:  # if
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
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])
        self.consumir(TIPO_TOKENS["OPERADORES"][":="])
        resultado, codigos, tipo_expr = self.analisar_expr()
        tipo_var = self.tabela_tipos.get(ident_token[1], None)
        if tipo_var is None:
            raise SyntaxError(f"Variável '{ident_token[1]}' não declarada.")
        # Permite atribuição real->integer (truncar no interpretador), ou igual
        if not (tipo_var == tipo_expr or (tipo_var == "integer" and tipo_expr == "real")):
            raise SyntaxError(f"Tipo incompatível na atribuição: variável '{ident_token[1]}' é '{tipo_var}' e expressão é '{tipo_expr}'.")
        self.codigos_intermediarios.extend(codigos)
        if tipo_var == "string":
            if not (resultado.startswith('"') and resultado.endswith('"')) and resultado not in self.tabela_tipos and not resultado.startswith("t"):
                resultado = f'"{resultado}"'
        if tipo_var == "boolean":
            # Se não for variável booleana, converte para "true"/"false" com aspas
            if resultado.lower() in ("true", "false") and not (resultado.startswith('"') and resultado.endswith('"')):
                resultado = f'"{resultado.lower()}"'
        
        self.codigos_intermediarios.append(('att', ident_token[1], resultado, tipo_var))

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
        resultado, codigos, tipo = self.analisar_and()
        return self.analisar_restoOr(resultado, codigos, tipo)

    def analisar_restoOr(self, resultado_esq, codigos_esq, tipo_esq):
        """
        Analisa a produção <restoOr>:
        'or' <and> <restoOr> | & ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["LOGICOS"]["or"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["or"])
            resultado_dir, codigos_dir, tipo_dir = self.analisar_and()
            if tipo_esq != "boolean" or tipo_dir != "boolean":
                raise SyntaxError("Operador 'or' só pode ser usado com booleanos.")
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('or', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoOr(temp, codigos, "boolean")
        else:
            return resultado_esq, codigos_esq, tipo_esq

    def analisar_and(self):
        """
        Analisa a produção <and>:
        <not> <restoAnd> ;
        """
        resultado, codigos, tipo = self.analisar_not()
        return self.analisar_restoAnd(resultado, codigos, tipo)

    def analisar_restoAnd(self, resultado_esq, codigos_esq, tipo_esq):
        """
        Analisa a produção <restoAnd>:
        'and' <not> <restoAnd> | & ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["LOGICOS"]["and"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["and"])
            resultado_dir, codigos_dir, tipo_dir = self.analisar_not()
            if tipo_esq != "boolean" or tipo_dir != "boolean":
                raise SyntaxError("Operador 'and' só pode ser usado com booleanos.")
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('and', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAnd(temp, codigos, "boolean")
        else:
            return resultado_esq, codigos_esq, tipo_esq

    def analisar_not(self):
        """
        Analisa a produção <not>:
        'not' <not> | <rel> ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["LOGICOS"]["not"]:
            self.consumir(TIPO_TOKENS["LOGICOS"]["not"])
            resultado, codigos, tipo = self.analisar_not()
            if tipo != "boolean":
                raise SyntaxError("Operador 'not' só pode ser usado com booleanos.")
            temp = self.gerador_aux.nova_temp()
            codigos.append(('not', temp, resultado, None))
            return temp, codigos, "boolean"
        else:
            return self.analisar_rel()

    def analisar_rel(self):
        """
        Analisa a produção <rel>:
        <add> <restoRel> ;
        """
        resultado_esq, codigos_esq, tipo_esq = self.analisar_add()
        return self.analisar_restoRel(resultado_esq, codigos_esq, tipo_esq)

    def analisar_restoRel(self, resultado_esq, codigos_esq, tipo_esq):
        token = self.token_atual()
        if token and token[0] in {
            TIPO_TOKENS["RELACIONAIS"]["=="], TIPO_TOKENS["RELACIONAIS"]["<>"],
            TIPO_TOKENS["RELACIONAIS"]["<"], TIPO_TOKENS["RELACIONAIS"]["<="],
            TIPO_TOKENS["RELACIONAIS"][">"], TIPO_TOKENS["RELACIONAIS"][">="]
        }:
            op = OPERADORES_RELACIONAIS_SIMBOLOS[token[0]] #self.numero_para_lexema[token[0]]
            self.consumir(token[0])
            resultado_dir, codigos_dir, tipo_dir = self.analisar_add()
            # Permite comparações entre integer e real
            if (tipo_esq in ("integer", "real") and tipo_dir in ("integer", "real")):
                tipo_cmp = "real"
            elif tipo_esq == tipo_dir:
                tipo_cmp = tipo_esq
            else:
                raise SyntaxError(f"Operação relacional entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}'.")
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [(op, temp, resultado_esq, resultado_dir)]
            return temp, codigos, "boolean"
        else:
            return resultado_esq, codigos_esq, tipo_esq
            
    def analisar_add(self):
        """
        Analisa a produção <add>:
        <mult> <restoAdd> ;
        """
        resultado, codigos, tipo = self.analisar_mult()
        return self.analisar_restoAdd(resultado, codigos, tipo)

    def analisar_restoAdd(self, resultado_esq, codigos_esq, tipo_esq):
        """
        Analisa a produção <restoAdd>:
        '+' <mult> <restoAdd> 
        | '-' <mult> <restoAdd> 
        | & ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["OPERADORES"]["+"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["+"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_mult()
            # Permite integer + real, real + integer, real + real, integer + integer, string + string
            if (tipo_esq in ("integer", "real") and tipo_dir in ("integer", "real")):
                tipo_result = "real" if "real" in (tipo_esq, tipo_dir) else "integer"
            elif tipo_esq == tipo_dir == "string":
                # Garante que literais estejam entre aspas
                if resultado_esq not in self.tabela_tipos and not resultado_esq.startswith('"'):
                    resultado_esq = f'"{resultado_esq}"'
                if resultado_dir not in self.tabela_tipos and not resultado_dir.startswith('"'):
                    resultado_dir = f'"{resultado_dir}"'
                tipo_result = "string"
            else:
                raise SyntaxError(
                    f"Operação '+' entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('add', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAdd(temp, codigos, tipo_result)
        elif token and token[0] == TIPO_TOKENS["OPERADORES"]["-"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["-"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_mult()
            if (tipo_esq in ("integer", "real") and tipo_dir in ("integer", "real")):
                tipo_result = "real" if "real" in (tipo_esq, tipo_dir) else "integer"
            else:
                raise SyntaxError(
                    f"Operação '-' entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('sub', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoAdd(temp, codigos, tipo_result)
        else:
            return resultado_esq, codigos_esq, tipo_esq

    def analisar_mult(self):
        """
        Analisa a produção <mult>:
        <uno> <restoMult> ;
        """
        resultado, codigos, tipo = self.analisar_uno()
        return self.analisar_restoMult(resultado, codigos, tipo)


    def analisar_restoMult(self, resultado_esq, codigos_esq, tipo_esq):
        """
        Analisa a produção <restoMult>:
        '*' <uno> <restoMult>
        |  '/' <uno> <restoMult> 
        |  'mod' <uno> <restoMult> | & ;
        |  'div' <uno> <restoMult> | & ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["OPERADORES"]["*"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["*"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_uno()
            if (tipo_esq in ("integer", "real") and tipo_dir in ("integer", "real")):
                tipo_result = "real" if "real" in (tipo_esq, tipo_dir) else "integer"
            else:
                raise SyntaxError(
                    f"Operação '*' entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('mult', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos, tipo_result)
        elif token and token[0] == TIPO_TOKENS["OPERADORES"]["/"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["/"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_uno()
            # Em Pascal, divisão '/' sempre resulta em real
            if (tipo_esq in ("integer", "real") and tipo_dir in ("integer", "real")):
                tipo_result = "real"
            else:
                raise SyntaxError(
                    f"Operação '/' entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('div', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos, tipo_result)
        elif token and token[0] == TIPO_TOKENS["OPERADORES"]["mod"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["mod"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_uno()
            if tipo_esq == tipo_dir == "integer":
                tipo_result = "integer"
            else:
                raise SyntaxError(
                    f"Operação 'mod' só pode ser usada entre inteiros. Encontrado: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('mod', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos, tipo_result)
        elif token and token[0] == TIPO_TOKENS["OPERADORES"]["div"]:
            op_token = token
            self.consumir(TIPO_TOKENS["OPERADORES"]["div"])
            next_token = self.token_atual()
            if next_token and next_token[0] in TOKENS_OPERADORES_BINARIOS:
                raise SyntaxError(
                    f"Dois operadores aritméticos seguidos ('{op_token[1]}{next_token[1]}') na linha {op_token[2]}, coluna {op_token[3]}."
                )
            resultado_dir, codigos_dir, tipo_dir = self.analisar_uno()
            if tipo_esq == tipo_dir == "integer":
                tipo_result = "integer"
            else:
                raise SyntaxError(
                    f"Operação 'div' só pode ser usada entre inteiros. Encontrado: '{tipo_esq}' e '{tipo_dir}' na linha {op_token[2]}, coluna {op_token[3]}"
                )
            temp = self.gerador_aux.nova_temp()
            codigos = codigos_esq + codigos_dir + [('idiv', temp, resultado_esq, resultado_dir)]
            return self.analisar_restoMult(temp, codigos, tipo_result)
        else:
            return resultado_esq, codigos_esq, tipo_esq
        
    def analisar_uno(self):
        """
        Analisa a produção <uno>:
        '+' <uno> | '-' <uno> | <fator> ;
        """
        token = self.token_atual()
        if token and token[0] == TIPO_TOKENS["OPERADORES"]["-"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["-"])
            resultado, codigos, tipo = self.analisar_uno()
            if tipo not in ("integer", "real"):
                raise SyntaxError("Operador unário '-' só pode ser aplicado a inteiros ou reais.")
            temp = self.gerador_aux.nova_temp()
            codigos.append(('sub', temp, 0, resultado))
            return temp, codigos, tipo
        elif token and token[0] == TIPO_TOKENS["OPERADORES"]["+"]:
            self.consumir(TIPO_TOKENS["OPERADORES"]["+"])
            return self.analisar_uno()
        else:
            return self.analisar_fator()
        
    def analisar_fator(self):
        """
        Analisa a produção <fator>:
        'NUMint' | 'NUMfloat' | 'IDENT'  | '(' <expr> ')' | 'STR' | HEX | OCT ;
        """
        token = self.token_atual()
        if token is None:
            raise SyntaxError("Fim inesperado do arquivo ao analisar fator.")

        token_tipo = token[0]
        if token_tipo in TOKENS_FATOR:
            self.consumir(token_tipo)
            if token_tipo == TIPO_TOKENS["IDENTIFICADOR"]:
                # Trata true/false como boolean
                if token[1].lower() in ("true", "false"):
                    tipo = "boolean"
                else:
                    tipo = self.tabela_tipos.get(token[1], None)
                    if tipo is None:
                        raise SyntaxError(f"Identificador '{token[1]}' não declarado.")
                return token[1], [], tipo
            elif token_tipo == TIPO_TOKENS["NUMBER_INT"]:
                tipo = "integer"
                return token[1], [], tipo
            elif token_tipo == TIPO_TOKENS["NUMBER_REAL"]:
                tipo = "real"
                return token[1], [], tipo
            elif token_tipo == TIPO_TOKENS["STRING"]:
                tipo = "string"
                return token[1], [], tipo
            elif token_tipo == TIPO_TOKENS["NUMBER_HEX"]:
                tipo = "integer"
                valor_convertido = str(int(token[1][1:], 16))  # Mantém como string para o pipeline
                return valor_convertido, [], tipo
            elif token_tipo == TIPO_TOKENS["NUMERO_OCT"]:
                tipo = "integer"
                valor_convertido = str(int(token[1][1:], 8))   # Mantém como string para o pipeline
                return valor_convertido, [], tipo
            else:
                tipo = None
                return token[1], [], tipo
        elif token_tipo == TIPO_TOKENS["DELIMITADOR"]["("]:
            self.consumir(TIPO_TOKENS["DELIMITADOR"]["("])
            resultado, codigos, tipo = self.analisar_expr()
            self.consumir(TIPO_TOKENS["DELIMITADOR"][")"])
            return resultado, codigos, tipo
        else:
            raise SyntaxError(f"Token inesperado '{token[1]}' na linha {token[2]}, coluna {token[3]} ao analisar fator.")

    def analisar(self):
        """
        Inicia a análise sintática a partir da produção principal <function*>.
        """
        self.analisar_funcao()
        print("Parsing concluído com sucesso!")
        print("Códigos intermediários gerados:")
        with open("codigo_intermediario.txt", "w", encoding="utf-8") as arquivo:
            for codigo in self.codigos_intermediarios:
                print(codigo)  # mantém o print no terminal
                arquivo.write(str(codigo) + "\n")  # escreve no arquivo

    def analisar_chamada_proc(self):
        """
        Analisa uma chamada de procedimento simples:
        'IDENT' ';'
        """
        ident_token = self.token_atual()
        nome_ident = ident_token[1]
        # Verifica se o identificador foi declarado
        if nome_ident not in self.tabela_tipos:
            raise SyntaxError(f"Identificador '{nome_ident}' não declarado na linha {ident_token[2]}, coluna {ident_token[3]}.")
        self.consumir(TIPO_TOKENS["IDENTIFICADOR"])  # IDENT
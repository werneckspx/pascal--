def compilador_codigo_intermediario(caminho_arquivo):
    memoria = {}
    instrucoes = []
    labels = {}

    # Passo 1: leitura e parsing com eval seguro
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            try:
                instr = eval(linha)  # transforma a string ('att', 'a', '0', 'integer') em tupla real
                instrucoes.append(list(instr))
            except Exception as e:
                print(f"[ERRO] Linha inválida no arquivo: {linha}\nDetalhes: {e}")
                continue

    # Passo 2: mapear labels
    for idx, instr in enumerate(instrucoes):
        if instr[0].upper() == 'LABEL':
            labels[instr[1]] = idx

    # Função para pegar valor da memória ou literal
    def val(x):
        if isinstance(x, str):
            if x.lstrip('-').replace('.', '', 1).isdigit():
                return float(x) if '.' in x else int(x)
            if x.startswith('"') and x.endswith('"'):
                return x[1:-1]  # Retorna o conteúdo da string literal
            return memoria.get(x, 0)
        return x

    # Passo 3: execução
    pc = 0
    while pc < len(instrucoes):
        instr = instrucoes[pc] + [''] * (4 - len(instrucoes[pc]))  # garantir 4 argumentos
        op, arg1, arg2, arg3 = [x.upper() if i == 0 else x for i, x in enumerate(instr)]

        if op == 'ATT':
            if arg3 == "string" and isinstance(arg2, str) and arg2.startswith('"') and arg2.endswith('"'):
                memoria[arg1] = arg2[1:-1]
            elif arg3 == "integer":
                memoria[arg1] = int(val(arg2))
            elif arg3 == "real":
                memoria[arg1] = float(val(arg2))
            elif arg3 == "boolean":
                # Trata "true"/"false" (com ou sem aspas) corretamente
                if isinstance(arg2, str):
                    valor = arg2.strip('"').lower()
                    if valor == "true":
                        memoria[arg1] = True
                    elif valor == "false":
                        memoria[arg1] = False
                    else:
                        memoria[arg1] = bool(val(arg2))
                else:
                    memoria[arg1] = bool(val(arg2))

        elif op == 'ADD':
            memoria[arg1] = val(arg2) + val(arg3)

        elif op == 'SUB':
            memoria[arg1] = val(arg2) - val(arg3)

        elif op == 'MULT':
            memoria[arg1] = val(arg2) * val(arg3)
        
        elif op == 'DIV':
            if val(arg3) == 0:
                print(f"[ERRO] Divisão por zero (linha {pc})")
                break
            memoria[arg1] = (val(arg2)) / (val(arg3))
        elif op == 'IDIV':
            if val(arg3) == 0:
                print(f"[ERRO] Divisão inteira por zero (linha {pc})")
                break
            memoria[arg1] = int(val(arg2)) // int(val(arg3))
        elif op == 'MOD':
            if val(arg3) == 0:
                print(f"[ERRO] Módulo por zero (linha {pc})")
                break
            memoria[arg1] = int(val(arg2)) % int(val(arg3))

        elif op in ['EQ', '=', '==']:
            memoria[arg1] = int(val(arg2) == val(arg3))

        elif op in ['NEQ', '<>']:
            memoria[arg1] = int(val(arg2) != val(arg3))

        elif op in ['GRET', '>']:
            memoria[arg1] = int(val(arg2) > val(arg3))

        elif op in ['LESS', '<']:
            memoria[arg1] = int(val(arg2) < val(arg3))

        elif op in ['LEQ', '<=']:
            memoria[arg1] = int(val(arg2) <= val(arg3))

        elif op in ['GEQ', '>=']:
            memoria[arg1] = int(val(arg2) >= val(arg3))

        elif op == 'AND':
            memoria[arg1] = int(val(arg2) and val(arg3))

        elif op == 'OR':
            memoria[arg1] = int(val(arg2) or val(arg3))

        elif op == 'NOT':
            memoria[arg1] = int(not val(arg2))

        elif op == 'CALL':
            if arg1.lower() in ['read', 'readln']:
                prompt_text = arg2 if isinstance(arg2, str) else str(arg2)
                entrada = input()
                tipo = (arg3 or '').lower()
                try:
                    if tipo == "integer":
                        print(f"arg2: {arg2}, tipo: {tipo}")
                        memoria[arg2] = int(entrada)
                    elif tipo == "real":
                        memoria[arg2] = float(entrada)
                    elif tipo == "hex":
                        memoria[arg2] = int(entrada, 16)
                    elif tipo == "oct":
                        memoria[arg2] = int(entrada, 8)
                    elif tipo == "string":
                        memoria[arg2] = entrada
                    elif tipo == "boolean":
                        memoria[arg2] = entrada.lower() in ['true', '1']
                    else:
                        print(f"[ERRO] Tipo inválido: {tipo} (linha {pc})")
                        break
                except Exception as e:
                    print(f"[ERRO] na leitura: {e}")
                    break

            elif arg1.lower() in ['write', 'writeln']:
                if isinstance(arg2, str) and arg2.startswith('"') and arg2.endswith('"'):
                    texto = arg2[1:-1]
                    print(texto, end='' if arg1.lower() == 'write' else '\n')
                else:
                    print(val(arg2), end='' if arg1.lower() == 'write' else '\n')


        elif op == 'JUMP':
            if arg1 not in labels:
                print(f"[ERRO] Label '{arg1}' não encontrado (linha {pc})")
                break
            pc = labels[arg1]
            continue

        elif op == 'IF':
            cond = val(arg1)
            destino = arg2 if cond else arg3
            if destino not in labels:
                print(f"[ERRO] Label '{destino}' não encontrado (linha {pc})")
                break
            pc = labels[destino]
            continue

        pc += 1

# compilador_codigo_intermediario('codigo_intermediario.txt')
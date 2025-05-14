from lexer import Lexer
from sintatico import Sintatic

def read_pascal_file(filename):
    with open(filename, "r") as file:
        return file.read()

def main():

    filename = input("Digite o caminho do arquivo Pascal: ") #listax/EXSy.pas #
    try:
        source_code = read_pascal_file(filename)
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        print("=== TOKENS ===")
        has_lexical_error = False
        for token in tokens:
            if token[0] == "ERROR":
                print(f"[ERRO] {token[1]} na linha {token[2]}, coluna {token[3]}")
                has_lexical_error = True
                break
            else:
                print(token)
        print("\n")
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{filename}' não encontrado.")
        return
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")
        return

    if has_lexical_error:
        print("Erro léxico detectado. Análise sintática não será executada.")
        return

    sintatico = Sintatic(tokens)
    print("=== ANÁLISE SINTÁTICA ===")
    try:
        sintatico.analisar()
        print("Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"[ERRO SINTÁTICO] {e}")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
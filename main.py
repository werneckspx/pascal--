
from lexer import Lexer

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
        for token in tokens:
            if token[0] == "ERROR":
                print(f"[ERRO] {token[1]} na linha {token[2]}, coluna {token[3]}")
                break
            else:
                print(token)
        print("\n")
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

"""
import os
import sys
from lexer import Lexer

def read_pascal_file(filename):
    with open(filename, "r") as file:
        return file.read()

def process_files():
    output_file = "tokens_output.txt"
    directories = ["lista1", "lista2", "lista3"]
    file_count = 25

    with open(output_file, "w") as out:
        for directory in directories:
            for i in range(1, file_count + 1):
                filename = os.path.join(directory, f"EXS{i}.pas")
                if os.path.exists(filename):
                    source_code = read_pascal_file(filename)
                    lexer = Lexer(source_code)
                    tokens = lexer.tokenize()

                    # Escreve o cabeçalho com o nome da pasta e do arquivo
                    out.write(f"=== Pasta: {directory} \t | \t Arquivo: {filename} ===\n\n ===TOKENS=== \n")
                    for token in tokens:
                        if token[0] == "ERROR":
                            # Escreve o erro no arquivo e encerra o programa
                            error_message = f"[ERRO] {token[1]} na linha {token[2]}, coluna {token[3]}"
                            out.write(error_message + "\n")
                            out.write("=" * 100 + "\n\n")
                            sys.exit(error_message)  # Encerra o programa com a mensagem de erro
                        else:
                            out.write(f"{token}\n")
                    # Adiciona separador após o arquivo
                    out.write("=" * 100 + "\n\n")
                else:
                    out.write(f"[ERRO] Arquivo não encontrado: {filename}\n")
                    out.write("=" * 100 + "\n")


if __name__ == "__main__":
    process_files()
"""
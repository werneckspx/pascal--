from lexer import Lexer

def read_pascal_file(filename):
    with open(filename, "r") as file:
        return file.read()

def main():
    source_code = read_pascal_file("example.pas")
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    print("=== TOKENS ===")
    for token in tokens:
        if token[0] == "ERROR":
            print(f"[ERRO] {token[1]} na linha {token[2]}, coluna {token[3]}")
            break
        else:
            print(token)

    #print("\n=== SAÍDA SIMULADA (Pascal) ===")
    #output = lexer.simulate_output()
    #for line in output:
    #    print(line)

    print("\n=== ERROS ===")
    for token in tokens:
        if token[0] == "ERROR":
            print(f"[ERRO] {token[1]} na linha {token[2]}, coluna {token[3]}")


if __name__ == "__main__":
    main()

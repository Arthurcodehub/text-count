num_linhas = 0
num_palavras = 0
print("=== CONTADOR DE PALAVRAS E LINHAS ===")

try:
    caminho = input("Digite o caminho do arquivo: ").strip().strip('"')
    with open(caminho, "r" , encoding="utf-8") as a:
        for linha in a:
            num_linhas += 1
            num_palavras += len(linha.split())
    print(f"Esse arquivo possui {num_linhas} linhas no total")
    print(f"Esse arquivo possui {num_palavras} palavras no total")
except OSError as erro:
    print(f"Não foi possível abrir o arquivo: {erro}")
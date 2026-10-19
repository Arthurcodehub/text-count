print("=== CONTADOR DE PALAVRAS E LINHAS ===")

caminho = input("Digite o caminho do arquivo: ").strip().strip('"')

num_linhas = 0
num_palavras = 0

try:
    
    with open(caminho, "r" , encoding="utf-8") as arquivo:
        for linha in arquivo:
            num_linhas += 1
            num_palavras += len(linha.split())
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
except PermissionError:
    print("Sem permissão para ler este arquivo.")
except UnicodeDecodeError:
    print("Não foi possível ler o arquivo como UTF-8. Ele pode ser binário ou estar em outra codificação.")
except OSError as erro:
    print(f"Não foi possível abrir o arquivo: {erro}")
else:
    print(f"Esse arquivo possui {num_linhas} linhas no total")
    print(f"Esse arquivo possui {num_palavras} palavras no total")
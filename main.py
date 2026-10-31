def contar_palavras_e_linhas(caminho: str):
    num_linhas = 0
    num_palavras = 0

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                num_linhas += 1
                num_palavras += len(linha.split())
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
        return
    except PermissionError:
        print("Sem permissão para ler este arquivo.")
        return
    except UnicodeDecodeError:
        print("Não foi possível ler o arquivo como UTF-8. Ele pode ser binário ou estar em outra codificação.")
        return
    except OSError as erro:
        print(f"Não foi possível abrir o arquivo: {erro}")
        return

    print(f"Esse arquivo possui {num_linhas} linhas no total")
    print(f"Esse arquivo possui {num_palavras} palavras no total")


if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo: ").strip().strip("'\"")
    contar_palavras_e_linhas(caminho)
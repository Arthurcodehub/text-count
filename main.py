class ContadorTexto:
    def __init__(self, caminho):
        self.caminho = caminho
        self.num_linhas = self.num_palavras = 0

    def contar(self):
        self.num_linhas = self.num_palavras = 0

        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                self.num_linhas += 1
                self.num_palavras += len(linha.split())

    def exibir_resultado(self):
        print(f"Esse arquivo possui {self.num_linhas} linhas no total.")
        print(f"Esse arquivo possui {self.num_palavras} palavras no total.")


if __name__ == "__main__":
    print("=== Text-Count ===")
    caminho = input("Digite o caminho do arquivo: ").strip().strip("'\"")
    contador = ContadorTexto(caminho)

    try:
        contador.contar()
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
    except PermissionError:
        print("Sem permissão para ler este arquivo.")
    except UnicodeDecodeError:
        print("Não foi possível ler o arquivo como UTF-8. Ele pode ser binário ou estar em outra codificação.")
    except OSError as erro:
        print(f"Não foi possível abrir o arquivo: {erro}")
    else:
        contador.exibir_resultado()
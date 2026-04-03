class Livro:
    def __init__(self, nome, sinopse):
        self.nome = nome
        self.sinopse = sinopse

class Biblioteca:
    def __init__(self, nome:str, livros:list):
        self.nome = nome
        self.livros = livros

    def adicionar_livro(self, livro:Livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            print("Insira um valor valido")

    def remover_livro(self, remocao:str):

        for livro in self.livros:
            if livro.nome == remocao:
                self.livros.remove(livro)
                break

        print("Livro não encontrado")

    def listar_livros(self):
        for livro in self.livros:
            print(livro.nome)

livro1 = Livro("Peter pan", "Historia do Peter pan")
livro2 = Livro("Hobbit", "Historia do Hobbit")
livro3 = Livro("Cronicas de Narnia", "Historia das Cronicas de Narnia")
lista_de_livros = [livro1, livro2, livro3]

biblioteca = Biblioteca("Alexandria", lista_de_livros)

while True:
    resposta = int(input(f"Olá seja bem  vindo a biblioteca {biblioteca.nome}\n"
          "O que deseja fazer?\n"
          "1 - Pegar um livro.\n"
          "2 - Devolver um livro.\n"
          "3 - Listar todos os livros.\n"
          "4 - Adicionar um livro.\n"
          "5 - Remover um livro.\n"
          "6 - Sair\n"))

    match resposta:
        case 1:
            pass
        case 2:
            pass
        case 3:
            biblioteca.listar_livros()
        case 4:
            titulo = input("Qual o titulo do livro?\n")
            sinopse = input("Descrva a sinopse do livro?\n")

            livro = Livro(titulo, sinopse)

            biblioteca.adicionar_livro(livro)
        case 5:
            remocao = input("Qual o nome do livro que você quer remover?\n")

            biblioteca.remover_livro(remocao)
        case 6:
            break
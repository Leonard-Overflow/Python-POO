class Livro:
    def __init__(self, nome:str, sinopse:str):
        self.nome = nome
        self.sinopse = sinopse

class Biblioteca:
    def __init__(self, nome:str, livros:list):
        self.nome = nome
        self.livros = livros

    def listar_livros(self) -> None:
        for livro in self.livros:
            print(livro.nome)

    def adicionar_livro(self, livro:Livro) -> None:
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            print("Insira um valor valido")

    def remover_livro(self, remocao:str) -> None:
        for livro in self.livros:
            if livro.nome == remocao:
                self.livros.remove(livro)
                return

        print("Livro não encontrado")

class Estudante:
    def __init__(self, nome:str, livros_pegos:list):
        self.nome = nome
        self.livros_pegos = livros_pegos

    def pegar_livro(self, nome:str,  biblioteca:Biblioteca) -> None:
        for livro in biblioteca.livros:
            if nome == livro.nome:
                livro_index = biblioteca.livros.index(livro)
                livro_escolhido = biblioteca.livros.pop(livro_index)
                self.livros_pegos.append(livro_escolhido)
                return
        print("A biblioteca não possui o livro em questão")

    def devolver_livro(self, nome:str,  biblioteca:Biblioteca) -> None:
        for livro in self.livros_pegos:
            if nome == livro.nome:
                livro_index = self.livros_pegos.index(livro)
                livro_escolhido = self.livros_pegos.pop(livro_index)
                biblioteca.livros.append(livro_escolhido)
                return
        print(f"O estudante {self.nome} não pegou o livro")

lista_do_estudante = []

gabriel = Estudante("Gabriel", lista_do_estudante)

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
            livro = input("Qual o nome do livro?\n")

            gabriel.pegar_livro(livro, biblioteca)
        case 2:
            livro = input("Qual o livro que você vai devolver?\n")

            gabriel.devolver_livro(livro, biblioteca)
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
        case _:
            print("Insira um valor válido")
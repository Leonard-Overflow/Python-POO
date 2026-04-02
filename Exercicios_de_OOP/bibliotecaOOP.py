class Livro:
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo

class Biblioteca:
    def __init__(self, nome:str, livros:list):
        self.nome = nome
        self.livros = livros

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            print("Insira um valor valido")

    def remover_livro(self, livro):
        i = 0

        while i < len(self.livros):
            if self.livros[i].nome == livro:
                self.livros.remove(self.livros[i])
            else:
                i += 1

        print("O livro em questão não existe nno catalogo da bibloteca")




while True:
    resposta = int(input("Olá seja bem  vindo a biblioteca \n"
          "O que deseja fazer?\n"
          "1 - Pegar um livro.\n"
          "2 - Devolver um livro.\n"
          "3 - Listar todos os livros.\n"
          "4 - Adicionar um livro.\n"
          "5 - Remover um livro.\n"
          "6 - Sair"))

    break
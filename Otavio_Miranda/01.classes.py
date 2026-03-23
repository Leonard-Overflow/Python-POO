class Pessoa:
    def __init__(self, nome:str, idade:int, andando = True): # É possivel definir tipos e valores para os atributos.
        self.nome = nome
        self.idade = idade
        self.andando = andando

    def parar(self):
        self.andando = False

    def retorna_idade(self) -> int: # É possível declara o tipo de retorno do método.
        return self.idade

    def esta_andando(self):
        print(self.andando)
        return

pessoa = Pessoa("Leonardo", 17)
pessoa.parar()
pessoa.esta_andando()
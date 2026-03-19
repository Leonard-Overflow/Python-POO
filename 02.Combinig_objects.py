class Dog:
    def __init__(self, nome, raca, dono):
        self.nome = nome
        self.raca = raca
        self.dono = dono

    def latido(self):
        print("AU AU")

    def exibir(self):
        print(self.nome)
        print(self.raca)

class Dono:
    def __init__(self, nome, endereco, numero_de_contato):
        self.nome = nome
        self.endereco = endereco
        self.numero_de_contato = numero_de_contato

dono1 = Dono("Daniel", "Rua Fortaleza, 317", "(21)14567-1922")
cachorro1 = Dog("Bolt", "Labrador", dono1)

print(cachorro1.dono.numero_de_contato)
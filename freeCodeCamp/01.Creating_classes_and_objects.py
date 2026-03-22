class Dog:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latido(self):
        print("AU AU")

    def exibir(self):
        print(self.nome)
        print(self.raca)

# Instanciando um obejtode um classe
cachorro1 = Dog("Bolt", "Labrador")

# Chamando um método da classe
cachorro1.latido()
cachorro1.exibir()


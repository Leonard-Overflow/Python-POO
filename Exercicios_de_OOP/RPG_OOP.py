class Pessoa:
    def __init__(self, arma):
        self.arma = arma

    def atacar(self):
        if self.arma == None:
            print("Soco")
        else:
            print(f"Ataque com {self.arma}")

class Guerreiro(Pessoa):
    def __init__(self, escudo:str):
        super().__init__(arma="Espada")
        self.escudo = escudo

    def atacar(self):
        print(f"Ataque com {self.arma}")

    def defender(self):
        if self.escudo != None:
            print("Defesa!")
        else:
            print("Sem escudo para defender")

class Arqueiro(Pessoa):
    def __init__(self, flechas:int):
        super().__init__(arma="Arco")
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
            print(f"Ataque com {self.arma}")
            self.flechas -= 1
        else:
            print("Sem flechas para atacar")

    def sinalizar(self):
        if self.flechas > 0:
            print("Sinalizacao!")
            self.flechas -= 1
        else:
            print("Sem flechas para sinalizar")

class Mago(Pessoa):
    def __init__(self, barreira:bool):
        super().__init__(arma="Cajado")
        self.barreira = barreira

    def atacar(self):
        print("Missil arcano")

    def impedir(self):
        if self.barreira != 0:
            print("YOU SHALL NOT PASS!!!")
        else:
            print("Sem barreira para impedir")

class Artiice(Pessoa):
    def __init__(self, municao:int):
        super().__init__(arma=["Espingarda", "Escopeta"])
        self.municao = municao

    def atacar(self):
            print("bang")
            self.municao -= 1

    def buckshot(self):
            print("boom")
            self.municao -= 3

    def ataque(self):
        while True:
            arma = input("Qual arma voce quer usar?")

            if arma == "espingarda" and self.municao != 0:
                self.atacar()
                break
            elif arma == "escopeta" and self.municao != 0:
                self.buckshot()
                break
            elif self.municao == 0:
                print("Sem municao para atacar")
                break
            else:
                print("Escolha uma opcao valida")

humano = Pessoa(None)
warrior = Guerreiro("escudo")
archer = Arqueiro(2)
mage = Mago(1)
artificer = Artiice(4)

lista = [humano, warrior, archer, mage]

for item in lista:
    item.atacar()

warrior.defender()
archer.sinalizar()
archer.sinalizar() # Para o else do sinalizar
mage.impedir()
artificer.ataque() # Para a espingarda
artificer.ataque() # Para a escopeta
artificer.ataque() # Para a falta de municao e o else

warrior.escudo = None
mage.barreira = False

for item in lista:
    item.atacar()

warrior.defender()
mage.impedir()

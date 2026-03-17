from datetime import datetime
import math

class Pessoa:
    def __init__(self, nome, idade, alutra, peso, hobby):
        self.nome = nome
        self.idade = idade
        self.alutra = alutra
        self.peso = peso
        self.hobby = hobby

    def ano_nascimento(self):
        ano_atual = datetime.today().year
        print(ano_atual - self.idade)

    def imc(self):
        imc = float(self.peso) / (float(self.alutra)**2)
        print(round(imc))

    def maioridade(self):
        if self.idade > 18:
            print("maior de idade")
        else:
            print("menor de idade")


carlos = Pessoa("carlos", 17, 1.75, 70, "video game")

carlos.ano_nascimento()
carlos.imc()
carlos.maioridade()
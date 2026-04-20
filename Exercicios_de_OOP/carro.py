class Motor:
    def __init__(self, combustivel:str, potencia:int,  limite:int):

        if combustivel in ("eletrico", "gasolina"):
            self.combustivel = combustivel
        else:
            raise ValueError("Combustivel invalido. Apenas gasolina ou eletrico")

        self.potencia = potencia
        self.estado = 0
        self.velocidade = 0.0
        self.limite = limite

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def acelerar(self):
        if self.estado:
            tempo = 0
            while self.velocidade < self.limite:
                self.velocidade += self.potencia
                tempo += 1

            print(tempo) # Quanto tempo levou para acelerar(Quantas iteracoes no caso)

    def verificar_combustivel(self):
        if self.combustivel == "gasolina":
            print(f"{self.combustivel}L de gasolina")
        else:
            print(f"{self.combustivel}J de energia")

class Transmissao:
    def __init__(self, tipo:str, n_de_marchas:list[str]):
        if tipo in ("manual", "automatica"):
            self.tipo = tipo
        else:
            raise ValueError("Tipo de transsissao invalido. Apenas manual ou automatica")

        self.n_de_marchas = n_de_marchas

        self.marcha = n_de_marchas[0]

    def mudar_marcha(self):
        while True:
            print("Para qual marcha você quer mudar?\n")
            print(*[marcha for marcha in self.n_de_marchas if marcha != self.marcha_atual], sep="\n")
            escolha = input("")

            if escolha in [marcha for marcha in self.n_de_marchas if marcha != self.marcha_atual]:
                self.marcha_atual = escolha
            else:
                continue
            break

class Roda:
    def __init__(self, aro:int, pressao:float):
        self.aro = aro
        self.pressao = pressao

    def verificar_pressao(self):
        if 30 < self.pressao < 35:
            print("OK")
        elif self.pressao < 30:
            print("O pneu esta com pouco ar")
        else:
            print("O pneu esta com muito ar")

class Chassi:
    def __init__(self, cor:str, modelo:str, ):
        self.cor = cor
        self.modelo = modelo

    def pintar(self):
        while True:
            cor = input("Qual sera a nova cor? ")

            if isinstance(cor, str):
                self.cor = cor
                break
            else:
                print("Opcao invalida")

class Carro(Motor, Transmissao, Chassi):
    def __init__(self, motor:Motor, transmissao:Transmissao, rodas:list[Roda], chassi:Chassi):
        self.motor = motor
        self.transmissao = transmissao
        self.roda = rodas
        self.chassi = chassi

    def informacoes_do_carro(self):
        if self.motor.estado:
            print("INFORMACOES DO MOTOR\n"
                  f"TIPO DE COMBUSTIVEL: {self.motor.combustivel}\n"
                  f"POTENCIA: {self.motor.potencia}\n"
                  f"LIMITE DE VELOCIDADE: {self.motor.velocidade}\n\n"
                  "INFORMACOES DA TRANSMISSAO\n"
                  f"TIPO DE TRANSMISSAO: {self.transmissao}\n"
                  f"QUANTIDADE DE MARCHAS: {self.transmissao.n_de_marchas}\n"
                  "INFORMACOES DO CHASSI\n"
                  f"COR DO CARRO: {self.chassi.cor}\n"
                  f"MODELO: {self.chassi.modelo}\n"
                  "INFORMACOES DAS RODAS\n"
            )

            for roda in self.rodas:
                print(f"ARO: {roda.aro}\n"
                      f"PRESSAO: {roda.presao}\n")

lista_de_marchas = ["1", "2", "3", "4", "5", "R"]

motor = Motor("energia", 50, 500)
transmissao = Transmissao("manual", lista_de_marchas)
roda1 = Roda(16, 30)
roda2 = Roda(16, 30)
roda3 = Roda(16, 30)
roda4 = Roda(16, 30)
lista_de_rodas = [roda1, roda2, roda3, roda4]
chassi = Chassi("Vermelho", "SUV")

carro = Carro(motor, transmissao, lista_de_rodas, chassi)

# Testes do motor
carro.ligar()
print(carro.estado)
carro.desligar()
print(carro.estado)
carro.acelerar()
print(carro.velocidade)
carro.verificar_combustivel()

# Testes da transmissao
carro.mudar_de_marcha()
print(carro.marcha_atual)

# Testes do chassi
carro.pintar()
print(carro.cor)

# Testes das rodas
for roda in carro.rodas:
    roda.verificar_pressao()

carro.informacoes_do_carro()
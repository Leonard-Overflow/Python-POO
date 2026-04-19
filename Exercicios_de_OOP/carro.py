class Motor:
    def __init__(self, combustivel:str, potencia:int, estado:bool, limite:int):

        if combustivel in ("eletrico", "gasolina"):
            self.combustivel = combustivel
        else:
            raise ValueError("Combustivel invalido. Apenas gasolina ou eletrico")

        self.potencia = potencia
        self.estado = estado
        self.velocidade = 0.0
        self.limite = limite

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def acelerar(self):
        if self.estado:
            while self.velocidade < self.limite:
                self.velocidade += self.potencia

    def verificar_combustivel(self):
        if self.combustivel == "gasolina":
            print(f"{self.combustivel}L de gasolina")
        else:
            print(f"{self.combustivel}J de energia")

class Transmissao:
    def __init__(self, tipo:str, n_de_marchas:list, marcha_atual:str):
        if tipo in ("manual", "automatica"):
            self.tipo = tipo
        else:
            raise ValueError("Tipo de transsissao invalido. Apenas manual ou automatica")

        self.n_de_marchas = n_de_marchas

        if marcha_atual in n_de_marchas:
            self.marcha_atual = marcha_atual
        else:
            raise ValueError("Marcha a marcha escolhida nao existe")

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
                self.cor = int(cor)
                break
            else:
                print("Opcao invalida")

class Carro:
    def __init__(self, motor:Motor, transmissao:Transmissao, rodas:list[Roda], chassi:Chassi):
        self.motor = motor
        self.transmissao = transmissao
        self.roda = rodas
        self.chassi = chassi

    def informacoes_do_carro(self):
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
              "INFORMACOES DAS RODAS"
        )

        for roda in self.rodas:
            print(f"ARO: {roda.aro}\n"
                  f"PRESSAO: {roda.presao}\n")
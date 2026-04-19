class Motor:
    def __init__(self, combustivel:str, potencia:int, estado:bool, velocidade:float, limite:int):

        if combustivel in ("eletrico", "gasolina"):
            self.combustivel = combustivel
        else:
            raise ValueError("Combustivel invalido. Apenas gasolina ou eletrico")

        self.potencia = potencia
        self.estado = estado
        self.velocidade = velocidade
        self.limite = limite

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def acelerar(self, limite):
        if self.estado:
            while self.velocidade < limite:
                self.velocidade += self.potencia

    def verificar_combustivel(self):
        if self.combustivel == "eletrico":
            print(f"{self.combustivel}L de gasolina")
        else:
            print(f"{self.combustivel}J de energia")

class Transmissao:
    def __init__(self, tipo:str, n_de_marchas:list, marcha_atual:int):
        if tipo in ("manual", "automatica"):
            self.tipo = tipo
        else:
            raise ValueError("Tipo de transsissao invalido. Apenas manual ou automatica")

        self.n_de_marchas = n_de_marchas

        if marcha_atual in n_de_marchas:
            self.marcha_atual = marcha_atual
        else:
            raise ValueError("Marcha a marcha escolhida nao existe")

class Roda:
    def __init__(self, aro:int, pressao:float):
        self.aro = aro
        self.pressao = pressao

class Chassi:
    def __init__(self, cor, modelo, ):
        self.cor = cor
        self.modelo = modelo
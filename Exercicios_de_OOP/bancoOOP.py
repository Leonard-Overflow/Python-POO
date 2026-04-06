from datetime import date

class Documento:
    def __init__(self, nome:str, numero:int, data_nascimento:date):
        self.nome = nome
        self.numero = numero
        self.data_nascimento = data_nascimento

class Carteira:
    def __init__(self, lista_de_documentos:list, dinheiro:float):

class Pessoa:
    def __init__(self, nome:str, idade:int, carteira:Carteira):
        self.nome = nome
        self.idade = idade
        self.carteira = carteira

class Conta:
    def __init__(self, id:str, saldo:float, dono:Pessoa):
        self.id = id
        self.saldo = saldo
        self.dono = dono

class Banco:
    def __init__(self, nome:str, contas:list):
        self.nome = nome
        self.contas = contas
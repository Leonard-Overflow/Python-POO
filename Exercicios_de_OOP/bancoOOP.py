from __future__ import annotations
import datetime

class Documento:
    def __init__(self, nome:str, numero:str, data_nascimento:datetime.date):
        self.nome = nome
        self.numero = numero
        self.data_nascimento = data_nascimento

class Carteira:
    def __init__(self, lista_de_documentos:list, dinheiro:float):
        self.lista_de_documentos = lista_de_documentos
        self.dinheiro = dinheiro

class Pessoa:
    def __init__(self, carteira:Carteira):
        self.nome = carteira.lista_de_documentos[0].nome
        self.idade = datetime.date.today().year - carteira.lista_de_documentos[0].data_nascimento.year
        self.carteira = carteira

class Banco:
    def __init__(self, nome:str):
        self.nome = nome
        self.contas = list[Conta] = []

    def adicionar_conta(self, conta:Conta) -> None:
        self.contas.append(conta)

    def remover_conta(self, conta:Conta) -> None:
        self.contas.remove(conta)

    def listar_contas(self) -> None:
        for conta in self.contas:
            print(conta.conta_id, conta.nome, conta.dono)

class Conta:
    def __init__(self, banco:Banco, conta_id:str, saldo:float, dono:Pessoa):
        self.conta_id = conta_id
        self.saldo = saldo
        self.dono = dono
        self.banco = banco

# CPF do Gabriel
nome = "Gabriel"
numero = "123.456.789-01"
data_nascimento = datetime.date(2001, 9, 17)

cpf = Documento(nome, numero, data_nascimento)

# RG do Gabriel
nome = "Gabriel"
numero = "12.345.678-9"
data_nascimento = datetime.date(2001, 9, 17)

rg = Documento(nome, numero, data_nascimento)

# Carteira do Gabriel
lista_de_documentos = [cpf, rg]
dinheiro = 0

carteira_do_gabriel = Carteira(lista_de_documentos, dinheiro)

# Pessoa(o próprio Gabriel)
gabriel = Pessoa(carteira_do_gabriel)

# Banco onde o Gabriel tem conta
nome = "Python Bank"

banco = Banco(nome)

# Conta bancária do Gabriel
conta_id = "00001"
saldo = 3000

conta_do_gabriel = Conta(banco, conta_id, saldo, gabriel)
banco.adicionar_conta(conta_do_gabriel)

while True:

    resposta = input("Escolha uma opcao:\n"
                     "1 - ")
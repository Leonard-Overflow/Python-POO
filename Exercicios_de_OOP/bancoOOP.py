from __future__ import annotations
import datetime

class Documento:
    def __init__(self, nome:str, numero:str, data_nascimento:datetime.date):
        self.nome = nome
        self.numero = numero
        self.data_nascimento = data_nascimento

class Pessoa:
    def __init__(self, dinheiro:float, documentos:list):
        self.nome = documentos[0].nome
        self.idade = datetime.date.today().year - documentos[0].data_nascimento.year
        self.documentos = documentos
        self.dinheiro = dinheiro

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

while True:

    resposta = input(f"\n\nBem-vindo ao banco {banco.nome}.\n"
                     "Escolha uma opcao:\n"
                     "1 - Sacar dinheiro\n"
                     "2 - Depositar dinheiro\n"
                     "3 - Listar as contas do banco\n"
                     "4 - Adicionar uma nova conta\n"
                     "5 - Remover uma conta\n"
                     "6 - Verifiar sua carteira\n"
                     "7 - Ver sua conta bancária\n"
                     "8 - Adicionar cliente\n"
                     "9 - Sair\n\n")

    match resposta:
        case "1":
            pass
        case "2":
            pass
        case "3":
            banco.listar_contas()
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            break
        case _:
            print("Insira uma opcao valida!")
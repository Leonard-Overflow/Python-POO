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
        self.contas: list[Conta] = []
        self.clientes: list[Pessoa] = []

    def adicionar_cliente(self) -> None:
        lista_de_documentos = []
        cliente = None

        while True:
            resposta = input("Voce tem acesso aos documentos desse cliente?[sim/nao]: ")
            resposta = resposta.lower().strip()
            if resposta == "sim":
                nome = input("Digite o nome do cliente: ")
                numero = input("Digite o numero do documento do cliente: ")
                data_nascimento = input("Digite o data de nascimento do cliente: ")

                data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y').date()

                documento = Documento(nome, numero, data_nascimento)
                lista_de_documentos.append(documento)

                outros_documentos = input("O cliente tem outros docuementos?[sim/nao]: ")
                outros_documentos = outros_documentos.lower().strip()

                if outros_documentos == "sim":
                    continue
                elif outros_documentos == "nao":
                    dinheiro = 0
                    while True:
                        try:
                            dinheiro = float(input("Quanto dinheiro o cliente tem?: "))
                            break
                        except ValueError:
                            print("Insira uma opcao valida!")

                    cliente = Pessoa(dinheiro, lista_de_documentos)

                else:
                    print("Insira uma opcao valida!")

            elif resposta == "nao":
                print("Busque o documento entao")
            else:
                print("Insira uma opcao valida!")

            conta_id = input("Digite o id da conta do cliente?: ")
            while True:
                try:
                    saldo = float(input("Digite o saldo do cliente: "))
                    break
                except ValueError:
                    print("Insira uma opcao valida!")

            conta = Conta(self, conta_id, saldo, cliente)
            self.contas.append(conta)
            self.clientes.append(cliente)
            print("Cliente adicionado com sucesso!")
            break

    def remover_cliente(self) -> None:
        remocao = input("Qual o nome do cliente?: ")

        cliente = next((cliente for cliente in self.clientes if cliente.nome == remocao), None)

        if cliente is None:
            print("Cliente nao encontrado")
        else:
            self.contas = [ conta for conta in self.contas if conta.dono.nome != remocao]
            self.clientes.remove(cliente)
            print("Cliente removido com sucesso!")

        print("Cliente nao encontrado")

    def listar_contas(self) -> None:
        for conta in self.contas:
            print(conta.conta_id + "|" + conta.dono.nome)

class Conta:
    def __init__(self, banco:Banco, conta_id:str, saldo:float, dono:Pessoa):
        self.conta_id = conta_id
        self.saldo = saldo
        self.dono = dono
        self.banco = banco

banco = Banco("Python Bank")

while True:

    resposta = input(f"\n\nBem-vindo ao banco.\n"
                     "Escolha uma opcao:\n"
                     "1 - Sacar dinheiro\n"
                     "2 - Depositar dinheiro\n"
                     "3 - Listar as contas do banco\n"
                     "4 - Adicionar uma nova conta\n"
                     "5 - Ver uma conta bancaria\n"
                     "6 - Verifiar uma carteira\n"
                     "7 - Remover uma cliente\n"
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
            banco.remover_cliente()
        case "8":
            banco.adicionar_cliente()
        case "9":
            break
        case _:
            print("Insira uma opcao valida!")
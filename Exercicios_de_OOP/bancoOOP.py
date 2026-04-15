from __future__ import annotations
import datetime

class Documento:
    def __init__(self, nome:str, numero:str, data_nascimento:datetime.date):
        self.nome = nome.lower().strip()
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

                if datetime.date.today().year - data_nascimento.year < 18:
                    print("O cleinte é menor de idade, nao podemos aceita-lo")
                    break

                documento = Documento(nome, numero, data_nascimento)
                lista_de_documentos.append(documento)

                outros_documentos = input("O cliente tem outros docuementos?[sim/nao]: ")
                outros_documentos = outros_documentos.lower().strip()

                if outros_documentos == "sim":
                    continue
                elif outros_documentos == "nao":
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
                    print("Insira um saldo valido!")

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
            self.contas = [conta for conta in self.contas if conta.dono.nome != remocao]
            self.clientes.remove(cliente)
            print("Cliente removido com sucesso!")

    def listar_contas(self) -> None:
        for conta in self.contas:
            print(conta.conta_id + "|" + conta.dono.nome)

    def verificar_carteira(self) -> None:
        nome = input("Digite seu nome: ").lower().strip()
        cliente = next((cliente for cliente in self.clientes if cliente.nome.lower().strip() == nome), None)

        if cliente is not None:
            numero = 1
            for conta in self.contas:
                if conta.dono.nome.lower().strip() == nome:
                    print(f"Saldo da conta {numero}: {conta.saldo}")
                    numero += 1
        else:
            print("Cliente não encontrado")

    def adicionar_conta(self) -> None:
        while True:
            while True:
                nome = input("Digite seu nome: ").lower().strip()

                if nome.replace(" ", "").isalpha():
                    break
                else:
                    print("Insira um nome valido")

            cliente = next((cliente for cliente in self.clientes if cliente.nome == nome), None)

            if cliente is not None:
                conta_id = input("Insira um id para a conta: ")
                while True:
                    try:
                        saldo = float(input("Insira o saldo da conta: "))
                        if cliente.dinheiro >= saldo and saldo > 0:
                            cliente.dinheiro -= saldo
                            conta = Conta(self, conta_id, saldo, cliente)
                            self.contas.append(conta)
                            return
                        else:
                            print("Saldo invalido")
                    except ValueError:
                        print("Insira um saldo valido")
            else:
                print("Cliente nao encontrado")

    def sacar_dinheiro(self) -> None:
        nome = input("Qual o seu nome?\n")
        cliente = next((cliente for cliente in self.clientes if cliente.nome == nome), None)

        if cliente is None:
            print("Cliente nao encontrado")
            return

        while True:
            try:
                montante = float(input("Quanto voce deseja sacar?\n"))
                if montante < 0:
                    print("Insira um valor valido")
                elif montante >= cliente.dinheiro:
                    print("O cliente nao pode depositar essa quantia")
                else:
                    break
            except ValueError:
                print("Insira um valor valido")

        contas = [conta for conta in self.contas if conta.dono.nome == nome and conta.saldo >= montante]

        if not contas:
            print("Nenhuma conta foi encontrada")
            return

        while True:

            try:

                print("Qual conta deseja sacar o dinhiro?\n")

                i = 1
                for conta in contas:
                    print(f"Conta {i}: {conta.saldo}")
                    i += 1

                resposta = input("")

                resposta = int(resposta)
                break
            except ValueError:
                print("Insira um valor valido")

        try:
            contas[resposta - 1].saldo -= montante
            cliente.dinheiro += montante
        except IndexError:
            print("Escolha uma conta existente")

    def depositar_dinheiro(self) -> None:
        nome = input("Qual o seu nome?\n")
        cliente = next((cliente for cliente in self.clientes if cliente.nome == nome), None)

        if cliente is None:
            print("Cliente nao encontrado")
            return

        while True:
            try:
                montante = float(input("Quanto voce deseja depositar?\n"))
                if montante < 0:
                    print("Insira um valor valido")
                elif montante >= cliente.dinheiro:
                    print("O cliente nao pode depositar essa quantia")
                else:
                    break
            except ValueError:
                print("Insira um valor valido")

        contas = [conta for conta in self.contas if conta.dono.nome == nome]

        if not contas:
            print("Nenhuma conta foi encontrada")
            return

        while True:

            try:

                print("Em qual conta voce deseja depositar o dinhiro?\n")

                i = 1
                for conta in contas:
                    print(f"Conta {i}: {conta.saldo}")
                    i += 1

                resposta = input("")

                resposta = int(resposta)
                break
            except ValueError:
                print("Insira um valor valido")

        try:
            contas[resposta - 1].saldo += montante
            cliente.dinheiro -= montante
        except IndexError:
            print("Escolha uma conta existente")

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
                     "6 - Remover uma cliente\n"
                     "7 - Adicionar cliente\n"
                     "8 - Sair\n\n")

    match resposta:
        case "1":
            banco.sacar_dinheiro()
        case "2":
            banco.depositar_dinheiro()
        case "3":
            banco.listar_contas()
        case "4":
            banco.adicionar_conta()
        case "5":
            banco.verificar_carteira()
        case "6":
            banco.remover_cliente()
        case "7":
            banco.adicionar_cliente()
        case "8":
            break
        case _:
            print("Insira uma opcao valida!")
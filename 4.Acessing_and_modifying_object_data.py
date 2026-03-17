class User:
    def __init__(self, username, email, senha):
        self._username = username # colocar um underline deixa o atributo privado. Não podera ser acessado por metodos de fora da classe.
        self.email = email
        self._senha = senha

    def saudacao(self, user):
        print(f"Mandando mensagem para o usuario {user.username}, olá {user.username} aqui é o {self.username}")

    def pega_senha(self):
        print(self._senha)

carlos = User("Carlos", "carlos@email.com", "1234")
jose = User("Jose", "jose@email.com", "1235")

carlos.pega_senha()


class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self._email = email
        self.senha = senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if len(email) == 0:
            raise ValueError("O email não pode ser vazio")
        elif "@" not in email:
            raise SyntaxError("O email precisa de um domínio")
        self._email = email

user  = User("Carlos", "carlos@email.com", "123")
email = user.email
print(email)
user.email = "carlos@gmail"
print(user.email)
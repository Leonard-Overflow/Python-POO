class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self._email = email # protegido
        self.senha = senha

    def get_email(self):
        return self._email

    def set_email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError("O email deve ser um string")
        elif "@" not in novo_email:
            raise TypeError("O email deve ter um domínio")
        elif len(novo_email) < 0:
            raise TypeError("O email não pode ser vazio")

user1 = User("Carlos", "carlos@email.com", "12345")


print(user1._email) # Não se usa, pois não pdoemos acessar o email(pelo menos não devemos)
print(user1.get_email()) # Pode acessar o email de um jeito seguro e correto


user1.set_email("carlos123@email.com")
print(user1.get_email())
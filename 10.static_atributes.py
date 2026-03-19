class User:
    user_count = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        User.user_count += 1

    def disply_user(self):
        print(f'Nome: {self.nome}, Email: {self.email}')

usuario = User("Carlos", "carlos@email.com")
usuario2 = User("Ana", "ana@email.com")

usuario.disply_user()
usuario2.disply_user()

print(usuario.user_count)
print(usuario2.user_count)

# O user_count aumenta representa o número de usuarios criados
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome # Convencionalmente privado, é possível acessa-lo, mas o dev deixou claro que é pra ser um atributo privado.
        self.__idade = idade # O python muda o nome do atributo dentro do sistema dificultando que ele seja usado fora da classe.

# Funcionam normalmente, mas não deve ser feito.
pessoa1 = Pessoa("Pedro", "12")
print(pessoa1._nome)
pessoa1.nome = "Ana"
print(pessoa1.nome)

# Difuculta que o acesso devido ao name mangling
#print(pessoa1.__idade) AttributeError

print(pessoa1._Pessoa__idade) # exibe o valor, pois o python renomeou o valor para _Pessoa__idade
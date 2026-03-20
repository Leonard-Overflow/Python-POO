class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    # metodo público
    def exibe_nome(self):
        print(self.nome)

    # metodo protgido
    def _exibe_idade(self):
        print(self.idade)

    # metodo privado
    def __exibe_cpf(self):
        print(self.cpf)

    def usa_o_privado(self):
        self.__exibe_cpf()


carlos = Pessoa("Carlos", 19, "123.456.789-10")

carlos.exibe_nome() # Exibe normal
carlos._exibe_idade() # Exibe normal(mas não deve-se fazer isso
carlos._Pessoa__exibe_cpf() # Exibe normal devido ao name mangling
carlos.usa_o_privado() # Exibe normal, pois é um metodo público usando um metodo privado
carlos.__exibe_cpf() # Da erro
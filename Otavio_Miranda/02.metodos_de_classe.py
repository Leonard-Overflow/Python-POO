class Pessoa:
    ano_atual = 2026 # Variavel de classe

    def __init__(self, nome, ano_nascimeno):
        self.nome = nome
        self.ano_nascimento = ano_nascimeno

    def idade(self):
        return self.ano_atual - self.ano_nascimento

    @classmethod
    def idade_por_ano(cls, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return idade
    # Quando for um class method é necessario passar os argumentos manualmente, pois não possui o self do objeto para pegar os atributos do objeto.

leonardo = Pessoa("Leonardo", 2007)
print(Pessoa.idade_por_ano(2007)) # Não é o ideal usar o objeto para chamar o class method, mas é possível

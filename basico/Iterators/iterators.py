class Contador():
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.limite:
            raise StopIteration
        valor = self.contador
        self.contador += 1
        return valor

class Lista():
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return Contador(self.limite)

lista = Lista(10)

for item in lista:
    print(item)
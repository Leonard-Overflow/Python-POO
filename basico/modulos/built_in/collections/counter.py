from collections import Counter

frase = "python collections"
lista_de_pedidos = ["frango", "bacon com cheddar", "peperoni",
                    "calabresa", "calabresa", "frango",
                    "frango", "bacon com cheddar", "frango"]

letras = Counter(frase)
pedidos = Counter(lista_de_pedidos)
print(letras)
print(pedidos)

# Métodos

print(pedidos.most_common(2))
print(list(pedidos.elements()))
print(letras)
letras.update("fox")
print(letras)
letras.subtract("over")
print(letras)
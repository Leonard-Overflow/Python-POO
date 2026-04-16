class Pato:
    def falar(self):
        print("QUACK!")

class Ganso:
    def falar(self):
        print("HONK!")

    def avisar(self):
        print("Mess with the honk\n"
              "YOU GET THE BONK")

def executar_falar(obj):
    obj.falar()

def executar_o_aviso(obj):
    obj.avisar()

# Se fala como um pato entao é um pato!
# executar_falar(Pato())
# executar_falar(Ganso())

# Se não avisa como um ganso não é um ganso!
executar_o_aviso(Ganso())
executar_o_aviso(Pato())
def fct_importada():
    print("Texto generico")

if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) > 1:
        nome = sys.argv[1]
        os.makedirs("arquivos", exist_ok=True)
        caminho = os.path.join("arquivos", nome)
        with open(caminho, 'w') as f:
            f.write("Arquivo criado com sucesso")
        print(f"Arquivo {nome} foi criado")
    else:
        print("Para executar o arquivo você deve passar 1 argumento depois do nome do arquivo")
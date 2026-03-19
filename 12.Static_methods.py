class ContaBancaria:
    def __init__(self, usuario, saldo, taxa_de_juros):
        self.usuario = usuario
        self.saldo = saldo

        if self.taxa_valida(taxa_de_juros):
            self.taxa_de_juros = taxa_de_juros
        else:
            raise ValueError("A taxa de juros deve ser um valor entre 0 e 100")

    @staticmethod
    def taxa_valida(taxa):
        if isinstance(taxa, (int, float)) and 0 <= taxa <= 100:
            return True
        return False


conta = ContaBancaria("Carlos", 1000, 100)


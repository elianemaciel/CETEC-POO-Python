class Conta:
    def __init__(self, cliente, saldo=0, numero="001", tipo="C"):
        self.saldo = saldo
        self.cliente = cliente
        self.numero = numero
        self.tipo = tipo

    def resumo(self):
        print(f"CC Número: {self.numero} \n\
            Saldo: {self.saldo} \n Cliente:\
                {self.cliente.nome}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Parabéns! Saque realizado com sucesso.")
            print("Seu saldo atual é: R${}".format(self.saldo))
        else:
            print("Você não possui saldo suficiente.")
    def deposito(self, valor):
        pass 

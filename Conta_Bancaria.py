class Conta:
    def __init__(self,numero,titular,saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def debitar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -=valor
    def creditar(self, valor):
        self.saldo += valor

    def extrair_saldo(self):
        return self.saldo
    

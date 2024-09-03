class Conta:
    #Construtor da Classe
    def __init__(self,numero,titular,saldo = 0, saldo_devedor = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.saldo_devedor = saldo_devedor
     
    #Realiza o Saque da conta do usuário
     
    def debitar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -=valor
    
    #Realiza deposito na conta do usuário
    
    def creditar(self, valor):
        self.saldo += valor
    #Retorna o saldo da conta
    def extrair_saldo(self):
        return self.saldo
    #Retorna o saldo devedor do usuário
    def extrair_saldo_devedor(self):
        return self.saldo_devedor
    def poupanca(self,tempo_em_meses,taxa):
        retorno = self.saldo
        for x in range (tempo_em_meses):
            retorno +=  (self.saldo * taxa)
        return retorno

    #Realiza um acrescimo na conta do usuário e incrementa o saldo Devedor 
    def emprestimo(self, valor):
        self.saldo_devedor =  valor + (valor * 0.2)
        self.creditar(valor)
    #Realiza a dedução do saldo devedor do usuário    
    def pagar_saldo_devedor(self, valor):
        self.saldo_devedor -= valor
    #Faz um estimativa de retorno sobre valor investido
    def investimento(self, valor,taxa, tempo_em_meses):
        retorno = valor
        for x in range (tempo_em_meses):
            retorno +=  (valor * taxa)
        return retorno


x = Conta(1,"agamenon")

print(x.investimento(10000,0.01,120))
    

class Cliente:
    #construtor
    def __init__(self,nome,servico):
        self.nome    = nome
        self.servico = servico
    
c1 = Cliente("agamenon", "site")
print(c1.nome)

class User:
    #construtor
    def __init__(self,nome,email,senha,endereco,servico):
        self.nome     = nome
        self.email    = email
        self.senha    = senha
        self.endereco = endereco
        self.servico  = servico
    
User1 = Cliente("agamenon", "site@site.com","12345","Bairro","Dev")
print(User1.nome)

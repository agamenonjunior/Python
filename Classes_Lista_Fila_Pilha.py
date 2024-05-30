# 1°
class No:
    def __init__(self,inidado):
        self.dado = inidado
        self.proximo = None
    def pegaDado(self):
        return self.dado
    def pegaProximo(self):
        return self.proximo
    def botaDado(self,novoDado):
        self.dado = novoDado
    def botaProximo(self,novoProximo):
        self.proximo = novoProximo
        
class ListaNaoOrdenada:
    def __init__(self):
        self.inicio = None
    def Vazia(self):
        return self.inicio == None
    def Inserir(self,item):
        temp = No(item)
        temp.botaProximo(self.inicio)
        self.inicio = temp
    def Buscar(self,item):
        atual = self.inicio
        encontrou = False
        while atual!= None and not encontrou:
            if atual.pegaDado() == item:
                encontrou = True
            else:
                atual = atual.pegaProximo()
        return encontrou
    
    def Tamanho(self):
        atual = self.inicio
        conta = 0
        while atual != None:
            conta += 1
            atual = atual.pegaProximo()
        return conta
    
    def Imprimir(self):
        atual = self.inicio
        while atual != None:
            print(str(atual.pegaDado()))
            atual = atual.pegaProximo()

    def Remover(self,item):
        atual = self.inicio
        previo = None
        encontrou = False
        while atual != None and not encontrou:
            if atual.pegaDado() == item:
                encontrou = True
            else:
                previo = atual
                atual = atual.pegaProximo()
        if previo == None:
            self.inicio = atual.pegaProximo()
        elif atual != None:
            previo.botaProximo(atual.pegaProximo())
        return encontrou

    def MultiplicaImpar(self):
        atual = self.inicio
        soma = 0
        while atual != None:
            if atual.pegaDado() %2 == 0:
                soma += atual.pegaDado()
                atual = atual.pegaProximo()
            else:
                atual = atual.pegaProximo()
        return soma

    def Menor(self):
        atual = self.inicio
        menor = atual.pegaDado()
        while atual != None:
            if atual.pegaDado() < menor:
                menor = atual.pegaDado()
                atual = atual.pegaProximo()
            else:
                atual = atual.pegaProximo()
        return menor
                
            
LN = ListaNaoOrdenada()
LN.Inserir(2)
LN.Inserir(4)
LN.Inserir(5)
LN.Inserir(7)
print(LN.MultiplicaImpar()) 

# 2°
class Fila:
    def __init__(self):
        self.items = []
    def Vazia(self):
        return self.items ==[]
    def Enfileirar(self,item):
        self.items.insert(0,item)
    def Desenfileirar(self):
        return self.items.pop()
    def Frente(self):
        return self.items[-1]
    def Tamanho(self):
        return len(self.items)
    def Imprimir(self):
        print(self.items)

class Pilha:
    def __init__(self):
        self.items = []
    def Vazia(self):
        return self.items ==[]
    def Empilhar(self,item):
        self.items.append(item)
    def Desempilhar(self):
        return self.items.pop()
    def Topo(self):
        return self.items[len(self.items)-1]
    def Tamanho(self):
        return len(self.items)
    def Imprimir(self):
        print(self.items)
    def Soma(self):
        soma = 0
        while not p.Vazia():
            valor = p.Desempilhar()
            soma += valor
        return soma
        
P = Pilha()
P.Empilhar(11)
P.Empilhar(12)
P.Empilhar(23)
P.Empilhar(14)
P.Empilhar(25)
P.Empilhar(50)
P.Empilhar(8)
P.Empilhar(18)
P.Empilhar(29)
P.Empilhar(10)
#P.Imprimir()
F = Fila()
while not P.Vazia():
    F.Enfileirar(P.Desempilhar())
print("fila")    
F.Imprimir()
while not F.Vazia():
    P.Empilhar(F.Desenfileirar())
print("Pilha")    
P.Imprimir()

#1 - F
#2 - F
#3 - V
#4 - V
#5 - V


# 3°
class Aeroporto:
    def __init__(self):
        self.items = []
    def Vazia(self):
        return self.items ==[]
    def Adicionar(self,aviao):
        self.items.insert(0,aviao)
    def Autorizar(self):
        return self.items.pop()
    def Primeiro(self):
        return self.items[-1]
    def Tamanho(self):
        return len(self.items)
    def Imprimir(self):
        print(self.items)
A = Aeroporto()
A.Adicionar(('A1',123))
A.Adicionar(('A2',563))
A.Adicionar(('A3',187))
print('TOTAL NA FILA DE ESPERA:',A.Tamanho())
print('Autorizado:',A.Autorizar())
A.Adicionar(('4',187))
A.Imprimir()
print('Primeira da Fila:',A.Primeiro())

# 4°

p = Pilha()
p.Empilhar(3)
p.Empilhar(40)
p.Desempilhar()
p.Empilhar(11)
p.Empilhar(4)
p.Empilhar(7)
p.Desempilhar()
p.Desempilhar()
print(p.Topo()) #11
print(p.Soma()) #14

# 5°
Lista_M = ListaNaoOrdenada()
Lista_M.Inserir(2)
Lista_M.Inserir(40)
Lista_M.Inserir(5)
Lista_M.Inserir(1)
print(Lista_M.Menor())

# 6°
class Listaencadeada:
    def __init__(self):
        self.inicio = None
    def Vazia(self):
        return self.inicio == None
    def Inserir(self,item):
        atual  = self.inicio
        previo = None
        parar  = False
        while atual !=None and not parar:
            if atual.pegaDado() > item:
                parar = True
            else:
                previo = atual
                atual = atual.pegaProximo()
        temp = No(item)
        if previo ==None:
            temp.botaProximo(self.inicio)
            self.inicio = temp
        else:
            temp.botaProximo(atual)
            previo.botaProximo(temp)

    
    def Tamanho(self):
        atual = self.inicio
        conta = 0
        while atual != None:
            conta += 1
            atual = atual.pegaProximo()
        return conta
    
    def Imprimir(self):
        atual = self.inicio
        while atual != None:
            print(str(atual.pegaDado()))
            atual = atual.pegaProximo()

    def Remover(self,item):
        atual = self.inicio
        previo = None
        encontrou = False
        while atual != None and not encontrou:
            if atual.pegaDado() == item:
                encontrou = True
            else:
                previo = atual
                atual = atual.pegaProximo()
        if previo == None:
            self.inicio = atual.pegaProximo()
        elif atual != None:
            previo.botaProximo(atual.pegaProximo())
        return encontrou
    
    def uniao(self,B):
        C = Listaencadeada()
        atual = self.inicio
        aux = B.inicio
        while atual!=None:            
            C.Inserir(atual.pegaDado())
            atual = atual.pegaProximo()
        while aux!=None:            
            C.Inserir(aux.pegaDado())
            aux = aux.pegaProximo()
        C.Imprimir()

        
    def intersecao(self,B):
        C = Listaencadeada()
        atual = self.inicio
        aux = B.inicio
        while atual!=None:
            if atual.pegaDado()== aux.pegaDado():
                C.Inserir(atual.pegaDado())
                atual = atual.pegaProximo()
                aux = aux.pegaProximo()                
            else:
                 atual = atual.pegaProximo()     
        C.Imprimir()
    def diferenca(self,B):
        C = Listaencadeada()
        atual = self.inicio
        aux = B.inicio
        while atual!=None:
            if atual.pegaDado()!= aux.pegaDado():
                C.Inserir(atual.pegaDado())
                atual = atual.pegaProximo()
                                
            else:
                 atual = atual.pegaProximo()
                 aux = aux.pegaProximo()
        C.Imprimir()

    def repetidos(self):
        atual = self.inicio
        while atual!=None and atual.pegaProximo()!=None:
            if atual.pegaDado() == atual.pegaProximo().pegaDado():
                self.Remover(atual.pegaDado())
                self.Remover(atual.pegaDado())
                atual = atual.pegaProximo()
            else:
                 atual = atual.pegaProximo()
        
        

A = Listaencadeada()
A.Inserir(1)
A.Inserir(2)
A.Inserir(3)
A.Inserir(6)
A.Inserir(5)
B = Listaencadeada()
B.Inserir(5)
B.Inserir(6)
B.Inserir(3)
A.Imprimir()
B.Imprimir()
A.uniao(B)
A.intersecao(B)
A.diferenca(B)


# 7°
R = Listaencadeada()
R.Inserir(1)
R.Inserir(2)
R.Inserir(2)
R.Inserir(6)
R.Inserir(5)
R.Imprimir()
R.repetidos()
print("sem repetidos")
R.Imprimir()

# 8°
class No_Arvore:
    def __init__(self,dado):
        self.esq = None
        self.dir = None
        self.dado = dado
class Arvore:
    def __init__(self):
        self.raiz = None
    def PegaRaiz(self):
        return self.raiz
    def Inserir(self,val):
        if(self.raiz ==None):
            self.raiz = No_Arvore(val)
        else:
            self._Inserir(val, self.raiz)
    def _Inserir(self,val , node):
        if(val < node.dado):
            if(node.esq !=None):
                self._Inserir(val,node.esq)
            else:
                node.esq = No_Arvore(val)
        else:
            if(node.dir !=None):
                self._Inserir(val,node.dir)
            else:
                node.dir = No_Arvore(val)
    def Imprimir(self):
        if(self.raiz !=None):
            self._Imprimir(self.raiz)
    def _Imprimir(self,node):
        if(node !=None):
            self._Imprimir(node.esq)
            self._Imprimir(node.dir)
            print (str(node.dado) + ' ')

    def Maior(self):
        maior = 0
        if(self.raiz !=None):            
            return self._Maior(self.raiz,maior)
        
    def _Maior(self,node,maior):
        if(node !=None):
            self._Maior(node.esq,maior)
            self._Maior(node.dir,maior)
            if node.dado > maior:
                maior = node.dado
                return self._Maior(node.dir,maior)
                
        return maior
            
            
            
    def Pares(self):
        L = []
        if(self.raiz !=None):
            return (self._pares(self.raiz,L))
            
    def _pares(self,node,L):
        if(node!=None):
            self._pares(node.esq,L)
            self._pares(node.dir,L)
            if(node.dado %2==0):
                L.append(node.dado)
        return(L)


    def EmOrdem(self):
        L = []
        if(self.raiz !=None):
            return (self._EmOrdem(self.raiz,L))
            
    def _EmOrdem(self,node,L):
        if(node!=None):
            self._EmOrdem(node.esq,L)
            #print(node.dado)
            L.append(node.dado)            
            self._EmOrdem(node.dir,L)            
        return(L)    

            
Max = Arvore()
Max.Inserir(2)
Max.Inserir(120)
Max.Inserir(20)
print(Max.Maior())

# 9°
ORDEM =  Arvore()
ORDEM.Inserir(8)
ORDEM.Inserir(4)
ORDEM.Inserir(9)
ORDEM.Inserir(2)
ORDEM.Inserir(7)
print(ORDEM.EmOrdem())

# 10°
A =  Arvore()
A.Inserir(2)
A.Inserir(1)
A.Inserir(4)
A.Inserir(5)
print(A.Pares())







    

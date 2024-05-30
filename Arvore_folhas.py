class No:
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
            self.raiz = No(val)
        else:
            self._Inserir(val, self.raiz)
    def _Inserir(self,val , node):
        if(val < node.dado):
            if(node.esq !=None):
                self._Inserir(val,node.esq)
            else:
                node.esq = No(val)
        else:
            if(node.dir !=None):
                self._Inserir(val,node.dir)
            else:
                node.dir = No(val)
    def Imprimir(self):
        if(self.raiz !=None):
            self._Imprimir(self.raiz)
    def _Imprimir(self,node):
        if(node !=None):
            self._Imprimir(node.esq)
            self._Imprimir(node.dir)
            print (str(node.dado) + ' ')
    def Folha(self):
        if(self.raiz !=None):
            return self._Folha(self.raiz)
            
    def _Folha(self,node):
        if(node.esq != None):
            self._Folha(node.esq)
        if(node.dir !=None):
            self._Folha(node.dir)
        if(node.esq == None  and node.dir ==None):
            print(str(node.dado))
        
            
            


A = Arvore()
A.Inserir(6)
A.Inserir(4)
A.Inserir(1)
A.Inserir(5)
A.Inserir(9)
A.Inserir(8)
A.Inserir(10)
A.Folha()

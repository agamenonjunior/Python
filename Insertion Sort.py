lista = [1,3,2,4,6,5]
#insert Sort
for i in range( 1, len(lista)):
    aux = lista[i]
    k  = i
#Compara atual < proximo
    while k > 0 and aux < lista[k - 1]:
        lista[k] = lista[k - 1] 
        k -= 1 #condicao de parada
        lista[k] = aux
print(lista)

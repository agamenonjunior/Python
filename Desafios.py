#1º. Desafio:

minha_lista = ["Fhash",100, "oi", False, [],-1,100]

#a) Inserir “comida” e 100 no final da lista.
minha_lista.extend(["comida", 100])
#b) Inserir “cachorro” na posição de índice 2.
minha_lista.insert(2,"cachorro")
#c) Inserir 99 no início da lista.
minha_lista.insert(0,99)
#d) Encontrar o índice de “oi”.
minha_lista.index("oi")
#e)  Contar o número de ocorrências de 100 na lista.
minha_lista.count(100)
#f)  Remover a primeira ocorrência do número 100 da lista.
minha_lista.remove(100)

#2º. Desafio:
def  calcula_minimo_2(L):
    L2=[] 
    soma = 0
    for num in (L):
       min1=min(L)
       if num != min1:
          L2.append(num)
          min2 = min(L2)
       soma = min1 + min2
    return (soma)

print(calcula_minimo_2([4,3,6,1,2]))

#3º. Desafio: 

def soma_quadrados(L): 
    soma = 0
    for i in L:
        soma = soma + i ** 2
    return (soma)
print(soma_quadrados([2, 3, 4]))

#4º. Desafio:
def seleciona_alunos(L):
    L2 = [ ]
    for nota in L:
       if  nota[1] >= 7:
          L2.append(nota)
    return (L2)

L = [['Pedro', 8], ['Joao', 6.5 ], ['Antonio', 9.5 ]]
print(seleciona_alunos(L))


#5º. Desafio: 
def espelho(L):
    texto = L
    L = [ ]
    L2 = [ ]
    for str1 in texto:
        L.append(str1)
        L2 = L + L[::-1]
    return(L2)

print(espelho(['a','b','c']))

#6º. Desafio: 

def quatidade_palavras_5(L):
    contador = 0
    for palavra in (L):
        if len(palavra) == 5:
           	contador +=1
    return contador

print(quatidade_palavras_5(['Brasil','peralta','mesa','lance','teste']))

#7º. Desafio:

def radical (rad, L):
    radical = rad
    x = len(radical)
    soma = 0
    for item in L:
        if item[0:x] == radical:
            soma += 1
    return(soma)

print(radical('part', ['partiu','parceiro','mesa','partida','parente']))


#8º. Desafio:


def palavras_inicio_fim_iguais(L):
    aux = 0
    for palavra in L:
        x = len(palavra)
        if x >= 2 and palavra[0] == palavra[-1]:
           	aux +=1
    return (aux)
print(palavras_inicio_fim_iguais(['aba', 'xyz', 'aa', 'x', 'bbb']))




#9º. Desafio:

def tripla():
    for a in range(1,500):
        for b in range(a+1, 500):
            for c in range(b+1,500):
                if (a**2 + (b**2) == (c**2)):
                    print(a,b,c)

tripla()



#10º. Desafio:

def troca(str1,velho,novo):
    str1 = str1.split()
    retorno =''
    for palavra in str1:
        if palavra[0:5] == velho:
          retorno +=novo+' '
        else:
          retorno +=palavra+' '

    return(retorno)
print(troca('um aluno, dois alunos, tres alunos.','aluno','estudante'))


#11º. Desafio:

def soma_impares(L):
    soma=0
    for i in L:
        if i%2 != 0:
            soma = soma + i
    return (soma)

print(soma_impares([11,20,36,41,55,6]))

                    

#12º. Desafio:

def quantidade_negativos(L):
    aux = 0
    for i in L:
        if i < 0:
            aux += 1
    return (aux)

print(quantidade_negativos([-1,-2,3,4,-5,-6]))


#13º. Desafio:

#a) 'Python'[1]
print('Python'[1])

#b) 'Strings são sequências de caracteres.'[5]

print('Strings sao sequencias de caracteres.'[5])

#c) len('maravilhoso')

print(len('maravilhoso'))

#d) 'Misterio'[:4]
print('Misterio'[:4])

#e) 'p' in 'Pineapple
print('p' in 'Pineapple')

#f) 'apple' in 'Pineapple
print('apple' in 'Pineapple')

#g) 'pear' not in 'Pineapple
print('pear' not in 'Pineapple')

#h) 'apple' > 'pineapple'
print('apple' > 'pineapple')

#i) 'pineapple' < 'Peach'

print('pineapple' < 'Peach')


#14º. Desafio:


def nao_eh_ruim(str1):
    retorno = ''
    for texto in str1:
        retorno = str1.replace("nao","eh bom")
        retorno = retorno.replace("eh tao ruim","")
    return(retorno)

print(nao_eh_ruim('Figado nao eh tao ruim'))




#15º. Desafio:

i = 0
soma = 0
qtermo = int(input("informe a quantidade de termos :"))
Dicionario = {}
while i<qtermo :
    soma +=((((-1)**i)*4)/(2*i+1))
    i+=1
    Dicionario[i] = soma
    
print(Dicionario)















import random
import timeit
import matplotlib.pyplot as plt


def generate_numbers_size(list, init_num, lenght):
    for i in range(1, lenght+ 1,1):
        if i != 1:
            i = i * 20
        elif i >= 2:
            i = i * 2
        num = init_num * i
        lista.append(num)

lista = []
num_elementos = []
generate_numbers_size(num_elementos, 100, 10)
tempo = []
tempo_ordena = []
  
def ger_aleatorios(tamanho):
    random.seed()
    global lista
    lista=[]
    i = 0
    while i < l:
        x  = random.randint(1,10*l)
        if x not in lista: 
            lista.append(x)
            i += 1   
    return lista

def selection_sort(tamanho):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1,len(lista)):
            if(lista[j] < lista[menor]):
                menor = j
        lista[i],lista[menor] = lista[menor],lista[i]
    return lista


for i in num_elementos:
    l = i
    tempo.append(timeit.timeit("ger_aleatorios({})".format(i), setup="from __main__ import ger_aleatorios",number=1))
    tempo_ordena.append(timeit.timeit("selection_sort({})".format(i), setup="from __main__ import selection_sort",number=1))
    print(i)
 
 
 
plt.plot(num_elementos, tempo, '*-', label='Tempo de Geração')
plt.plot(num_elementos, tempo_ordena, 'o-', label='Tempo de Ordenação')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade de elementos')
plt.show()

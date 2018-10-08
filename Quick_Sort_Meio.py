# -*- coding: UTF-8 -*-

import sys
import time
  
# Realiza procedimento de partição, chama recursivamente a função dividindo a lista 
def quick_sort(elements, esq, dir):
  i = esq
  j = dir
  i, j, elements = partition(elements, esq, dir, i, j)
  
  if esq < j:
    elements = quick_sort(elements, esq, j)
  if i < dir:
    elements = quick_sort(elements, i, dir) 

  return elements

# Escolhe um pivô sendo o valor do meio da lista, passa os valores menores que o pivô para sua esquerda e os maiores para direita  
def partition(elements, esq, dir, i, j):
  x = int(elements[(i+j)/2]) #Pivô
  while True:
    while(x > int(elements[i])): i+=1
    while(x < int(elements[j])): j-=1
    if i <= j:
      w = int(elements[i])
      elements[i] = int(elements[j])
      elements[j] = w
      i+=1
      j-=1

    if i > j: break
  return (i, j, elements)

  
# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Quick_Meio: %s\n" % value)

# Recebe valores por passagem de parametros na chamada do programa em linha de comando
try:
  arquivo = sys.argv[1]
except IndexError:
  arquivo = 'texto'

# Abre o arquivo do diretório informado
elements = open(arquivo+".txt", "r")

# Lê os registros do arquivo
linhas = elements.readlines()  

# Inicia a contagem do tempo
tempoi = time.time()
# Chama a função de ordenação
quick_sort(linhas, 0, len(linhas)-1)
# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
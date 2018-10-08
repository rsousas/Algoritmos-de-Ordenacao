# -*- coding: UTF-8 -*-

import sys
import time

# Seleciona o menor item da lista e troca com a o valor da primeira posição, incrementando o marcador de inicio da lista
def selection_sort(elements, n):  
  for i in range(0, n-1):
    min_index = i
    for j in range(i+1, n):
      if int(elements[min_index]) > int(elements[j]):
        min_index = j
    temp = int(elements[i])
    elements[i] = int(elements[min_index])
    elements[min_index] = temp
  

# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Selection: %s\n" % value)

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
selection_sort(linhas, len(linhas))
# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
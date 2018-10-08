# -*- coding: UTF-8 -*-

import sys
import time

def shell_sort(elements, n):
  h = n
  while True:
    h /= 2 # Define um valor de h
    for i in range(h, n):
      x = int(elements[i])
      j = i
      while int(elements[j-h]) > x: # Realiza comparações com distancia h entre os valores do vetor
        elements[j] = int(elements[j - h])
        j -= h
        if j < h: 
          break
      elements[j] = x
    if h == 1: # Finaliza o algoritmo quando a distancia entre os valores for de 1
      break

  
# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Shell: %s\n" % value)

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
shell_sort(linhas, len(linhas))

# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
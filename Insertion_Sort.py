# -*- coding: UTF-8 -*-

import sys
import time

# Compara o valor x com todos seus antecessores, até achar sua devida posição, começando do 2 registro da lista
def insertion_sort(elements, n):  
  for i in range(1, n):
    x = int(elements[i])
    j = i-1
    while x < int(elements[j]) and j >=0:
      elements[j+1] = int(elements[j])
      elements[j] = x
      j-=1
  
  
# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Insertion: %s\n" % value)

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
insertion_sort(linhas, len(linhas))
# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
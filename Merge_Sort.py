# -*- coding: UTF-8 -*-

import sys
import time

# Quebra a lista ao meio recursivamente até que fique apenas 1 elemento, volta a recursão comparando os elementos
def merge_sort(elements):
  resultado = []
  if len(elements) == 1:
    return elements
  
  meio = len(elements) / 2
  listaA = merge_sort(elements[:meio])
  listaB = merge_sort(elements[meio:])
  
  while (listaA ) and (listaB):
    if int(listaA[0]) <= int(listaB[0]):
      resultado.append(int(listaA[0]))
      del listaA[0]
    else:
      resultado.append(int(listaB[0]))
      del listaB[0]
  
  if listaA:
    for i in listaA:
      resultado.append(i)
  if listaB:
    for i in listaB:
      resultado.append(i)

  return resultado

  
# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Merge: %s\n" % value)

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
merge_sort(linhas)
# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
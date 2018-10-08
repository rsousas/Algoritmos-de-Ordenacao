# -*- coding: UTF-8 -*-

import sys
import time

def troca(a, i, j):
  a[i], a[j] = a[j], a[i]
  
def is_heap(a):
  n = 0
  m = 0
  while True:
    for i in [0, 1]:
      m += 1
      if m >= len(a):
        return True
      if a[m] > a[n]:
        return False
    n += 1
    
# Transforma a arvore em heap maxima com chamadas incrementais da raiz à folha
def max_heapify(a, n, max):
  while True:
    maior = n
    l = 2*n + 1
    r = l + 1
    for i in [l, r]:
      if i < max and a[i] > a[maior]:
        maior = i
    if maior == n:
      return
    troca(a, n, maior)
    n = maior

# Chamadas incrementais do nó pai mais baixo da heap para a raiz
def heapify(a):
  raiz = len(a) / 2 - 1
  max = len(a)
  while raiz >= 0:
    max_heapify(a, raiz, max)
    raiz -= 1

# Chama as demais funções do algoritmo e troca o valor da primeira posição com a ultima
def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j >= 0:
    troca(a, 0, j)
    max_heapify(a, 0, j)
    j -= 1
  
  
# Salva o resultado em arquivo
def save_arq(value):
  with open('Results.txt', 'a+') as f: f.write(arquivo+"_|_Heap: %s\n" % value)
  
# Recebe valores por passagem de parametros na chamada do programa em linha de comando  
try:
  arquivo = sys.argv[1]
except IndexError:
  arquivo = 'texto'

# Abre o arquivo do diretório informado
elements = open(arquivo+".txt", "r")

# Lê os registros do arquivo
linhas = elements.readlines()
# Convete os valores para inteiro
linhas = [int(i) for i in linhas]

# Inicia a contagem do tempo
tempoi = time.time()
# Chama a função de ordenação
heapsort(linhas)
# Finaliza a contagem do tempo
tempof = time.time()

# Chama a função que salva o resultado
save_arq(tempof-tempoi)
# Algoritmo que carrega um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor.

nomes = []
for i in range(10):
    nomes.append(str(input('Insira um nome: ')))
for i in range(2):
  lista = input('Confira se seu nome está na lista: ')
  if lista in nomes:
    print('Seu nome está na lista!')
  else:
    print('Nome não encontrado.')

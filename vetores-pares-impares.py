# Algoritmo que recebe dez números inteiros e armazene-os em um vetor e classifique os números em dois vetores, um com números pares e o outra com os ímpares.

vet_inteiros = []
pares = []
impares = []
for i in range(10):
  vet_inteiros.append(int(input('Digite um número: ')))
  if (vet_inteiros[i]%2) == 0:
    pares.append(vet_inteiros[i])
  else:
    impares.append(vet_inteiros[i])
print('Números pares:',pares)
print('Números ímpares:',impares)

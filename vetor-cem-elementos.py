# Algoritmo que receba dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. 
# Observação: percentual = quantidade contada * 100 / quantidade total.

cem = []
pares = 0
soma = 0
for i in range(10):
  cem.append(int(input('Digite um número: ')))
  soma = soma + cem[i]
  if i == 0:
      maior = cem[i]
      menor = cem[i]
  if cem[i] > maior:
      maior = cem[i]
  if cem[i] < menor:
      menor = cem[i]
  if (cem[i]%2) == 0:
    pares = pares + 1
percentual = (pares * 100) / len(cem)
media = soma / len(cem)
print('O percentual de número pares é de:',percentual)
print('A média dos elementos é de: ',media)

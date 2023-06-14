# Algoritmo que preenche um vetor com dez números reais
# Calcula e mostra a quantidade de números negativos; a soma dos números positivos desse vetor.

numeros = []
negativos = 0
positivos = 0
soma = 0
for y in range(10):
  numeros.append(float(input('Digite um número: ')))
  if numeros[y] >= 0:
    positivos = positivos + 1
    soma = soma + numeros[y]
  else:
    negativos = negativos + 1
print('Quantidade de números negativos:',negativos)
print('Soma dos números positivos:',soma)

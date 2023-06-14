# Algoritmo que preenche um vetor com seis elementos numéricos inteiros.
# Calcula e mostra todos os números pares; a quantidade de números pares; todos os números ímpares; a quantidade de números ímpares

vet_inteiros = []
pares = []
impares = []
quant_pares = 0
quant_impares = 0
for i in range(6):
  vet_inteiros.append(int(input('Insira um número: ')))
  if (vet_inteiros[i]%2) == 0:
    quant_pares = quant_pares + 1
    pares.append (vet_inteiros[i])
  else:
    quant_impares = quant_impares + 1
    impares.append (vet_inteiros[i])
print('Quantidade de números pares:',quant_pares)
print('Quantidade de números ímpares:',quant_impares)
print('Números pares:',pares)
print('Números ímpares:',impares)

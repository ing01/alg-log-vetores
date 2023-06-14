# Algoritmo que carrega um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições. 

vet_elementos = []
numeros_pares = []
for i in range(8):
  vet_elementos.append(int(input('Digite um valor numérico inteiro: ')))
  if (vet_elementos[i]%2) == 0:
   numeros_pares.append (vet_elementos[i])
   print('Número par adicionado',numeros_pares,'na posição',i)
print('Os números pares são:',numeros_pares)

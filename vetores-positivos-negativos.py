# Algoritmo que a crie dois vetores que receberão os elementos positivos e negativos de outro vetor e ao final apresente-os. 

inteiros = []
negativos = []
positivos = []
for i in range(5):
  inteiros.append(int(input('Digite um número: ')))
for i in range(len(inteiros)):
  if inteiros[i] >= 0:
    positivos.append (inteiros[i])
  else:
    negativos.append (inteiros[i])
print('Os números positivos são: ',positivos)
print('Os números negativos são: ',negativos)

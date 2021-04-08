##Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores que receberão os elementos positivos e negativos e ao final apresente-os. 
##Não use nenhuma função pronta da linguagem Python.

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

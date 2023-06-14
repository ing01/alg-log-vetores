# Algoritmo que calcule e apresente a média de alturas superior a 1,80. Informe também quantos e quais (índice/posição) são os alunos. 

altura = []
total = 0
cont = 0
for i in range(5):
  altura.append(float(input('Digite a altura: ')))
  if altura[i] > 1.80:
    total = total + altura[i]
    cont = cont + 1
    print('A pessoa',i,'tem',altura[i],'de altura.')
print('Total de pessoas com altura superior a 1.80:',cont)
print('A média de altura entre as pessoa é de',total/cont)

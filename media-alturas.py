# Algoritmo que calcula e apresenta a média de alturas de uma sala de 35 alunos. 
# Informe também quantos alunos e quais (índice/posição) são os que  possuem idade superior a 25 anos. 
# Usando dois vetores, um para altura e outro para idade. 

vet_altura = []
vet_idade = []
soma_alturas = 0
for i in range(5):
    vet_altura.append(float(input('Informe a altura: ')))
    vet_idade.append(int(input('Informe a idade: ')))
    soma_alturas = soma_alturas + vet_altura[i]
media = soma_alturas / len(vet_altura)
print('A média de alturas é', media)
cont = 0
for i in range( len(vet_idade) ):
    if vet_idade[i] > 25:
        cont = cont + 1 
        print('O aluno numero',i, 'possui',vet_idade[i],' anos')
print('Quantidade de pessoas com mais de 25 anos: ',cont)

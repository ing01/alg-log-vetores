##Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala.

vet_nota = []
soma_nota = 0
abaixo_media = 0
acima_media = 0
for i in range(5):
   vet_nota.append(float(input('Insira a média do aluno: ')))
   soma_nota = soma_nota + vet_nota[i]
media = soma_nota / len(vet_nota)
for i in range( len(vet_nota) ):
    if vet_nota[i] < media:
        abaixo_media = abaixo_media + 1  #incrementar
    else:
        acima_media = acima_media + 1 # incrementar
print('A média da sala é:',media)
print('Alunos abaixo da média:',abaixo_media)
print('Alunos acima da média:',acima_media)

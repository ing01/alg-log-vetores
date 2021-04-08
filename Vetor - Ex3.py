##Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a pessoa mais gorda e mais magra e 
##apresente o nome o peso das mesmas. Use dois vetores, um para peso e outro para nome. Não use nenhuma função pronta da linguagem Python.

vet_nome = []
vet_peso = []
for i in range(5):
    vet_nome.append(str(input('Digite o nome: ')))
    vet_peso.append(float(input('Digite o peso: ')))
    if i == 0:
        peso_maior = vet_peso[i]
        peso_menor = vet_peso[i]
        nome_gordo = vet_nome[i]
        nome_magro = vet_nome[i]
    if vet_peso[i] > peso_maior:
        peso_maior = vet_peso[i]
        nome_gordo = vet_nome[i]
    if vet_peso[i] < peso_menor:
        peso_menor = vet_peso[i]
        nome_magro = vet_nome[i]
print(nome_gordo, 'possui o maior peso, com', peso_maior, 'quilos.')
print(nome_magro, 'possui o maior peso, com', peso_menor, 'quilos.')

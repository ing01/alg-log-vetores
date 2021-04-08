##Um vetor é palíndromo se ele não se alterar quando o mesmo for invertido. Escreva um programa que verifique se um vetor é palíndromo, fazendo comparação 
##de índice/posição por índice/posição do vetor original (vo) com o vetor invertido (vi). Não use nenhuma função pronta da linguagem Python. 
##O tamanho do vetor pode ser da sua escolha.

veto = []
for i in range (5):
    veto.append(str(input("Digite  numero "+str(i) + ": ")))
    vetinvert = veto[::-1]
if veto == vetinvert:
    print("O conjunto {} é palíndromo de {}.".format(veto, vetinvert))
else:
    print("O conjunto {} não é palíndromo de {}.".format(veto, vetinvert))

nome = 'Pedro Henrique'
altura = 1.80
peso = 89
imc = peso / altura ** 2

"f-strings"
linha_1  = f'{nome} tem {altura:.2f} de altura'  #:.2f coloca quantas casas decimais eu quero, o número condiz a quantidade que quero

linha_2 = f'pesa {peso} quilos e seu imc é,'

linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)




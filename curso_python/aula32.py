"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero = int(numero_str)
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print('Não é um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite a hora em números inteiros: ')

try:
    hora = int(hora_str)
    if (hora >= 0 and hora <= 11):
        print('Bom dia')
    elif (hora >= 12 and hora <= 17):
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Não é um número')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
qtd_letras = len(nome)

if qtd_letras <= 4:
    print('Seu nome é curto')
elif (qtd_letras > 4 and qtd_letras <=6):
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
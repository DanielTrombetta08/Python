# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicador(2, 4, 6, 8)
print(multiplicacao)
print(2*4*6*8)

# Crie uma função que retorna se um numero é par ou impar

def par_impar(x):
    return 'Par' if x % 2 == 0 else 'Impar'

num_par_impar = par_impar(15)
print(num_par_impar)


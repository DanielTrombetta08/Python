"""
Iterando strings com while
"""
#       012345678910
nome = 'Daniel Trombetta'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

contador = 0
nova_string = ''

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador +=1


print(nova_string)
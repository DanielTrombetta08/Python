"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))



for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

    """
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
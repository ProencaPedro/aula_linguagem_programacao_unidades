'''
1. Crie uma lista com os quadrados dos números pares de 1 a 10.
'''
quadrados_pares = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(quadrados_pares)

'''
2. Converta a lista [1, 2, 3] em uma tupla e imprima osegundo valor.
'''
tupla = (1, 2, 3)
print(tupla[1])

'''
3. Crie um dicionário com 3 pares chave-valor e imprima seus valores.
'''
faculdade = {
    'primeiro_semestre': 'concluido.',
    'segundo_semestre': 'em andamento..',
    'terceiro_semestre': 'aguardando...'
}

print(faculdade['primeiro_semestre'])
print(faculdade['segundo_semestre'])
print(faculdade['terceiro_semestre'])

'''
4. Dado {1, 2, 3} e {3, 4, 5}, mostre a união e a interseção.
'''
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)

'''
5. Crie uma matriz 2x2 com NumPy e imprima sua transposta.
'''
import numpy as np 
a = np.array([[1,2], [3, 4]])
print(np.transpose(a))








import numpy as np
from numpy.linalg import cholesky


def print__matrix(M):
    for line in M:
        for el in line:
            print(f'{round(el.real, 2)}', end=' ')
        print()
    print()


"""
A:
1 1 1 1
1 2 2 2
1 2 3 3
1 2 3 4

B:
4 7 9 10
"""

n = int(input("Размерность n ="))

print("Матрица А:")

A = np.array(list(list(map(int, input().split())) for _ in range(n)))

print(A)

print("Вектор значений B:")

B = [int(a) for a in input().split()]
print(B)

try:
    L = cholesky(A)
    print("Матрицы L и L*, нижнетреугольная и эрмитова к ней сопряжённая")  # A = LL*
    print__matrix(L)
    print__matrix(L.T.conj())
    Y = np.dot(np.linalg.inv(L), B)
    print('Вектор решения W')
    [print(f'{round(z.real, 2)}') for z in Y]
    X = np.dot(np.linalg.inv(L.T.conj()), Y)
    print('Вектор решения X')
    [print(f'{round(z.real, 2)}') for z in X]
except Exception as error:
    print(error)

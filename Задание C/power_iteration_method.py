import numpy as np


def power_iteration(A, b, num_simulations: int):
    b_k = b
    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
        b_k = [round(i, 2) for i in b_k]
        print(b_k)
    b_k = [round(i) for i in b_k]
    return b_k


"""
Данные для тестов:
n
3
A
1 -2 -2
1 4 2
0 -6 -4
b
1 0 0
_________________________________________________________________________
Должно получиться:
максимальное собственное значение: 2.0, а вектор [0, -1, 1] или [0, 1, -1]
"""


print('Введите размерность')

n = int(input('Размерность матрицы - '))

print('Введите матричку А')

A = np.array(list(list(map(float, input().split())) for _ in range(n)))

print('Введите вектор b')

b = np.array(list(map(float, input().split())))

vector_prikol = (power_iteration(A, b, 150))
print(vector_prikol)

eigen_values, eigen_vectors = eigenvectors = np.linalg.eig(A)
eigen_values = [round(i, 2) for i in eigen_values]

print(f"Собственный вектор соответствующий максимальному собственному значению: "
      f"{max(eigen_values)}\nВектор:{vector_prikol}")

"""
________________________________________________________________________________________________________
на случай если похотливому деду понадобятся все собственные вектора раскомментировать это мега гавно
________________________________________________________________________________________________________

print("Все собственные вектора:")
print(eigen_vectors)
___
"""
print("Все собственные значения:")
print(eigen_values)

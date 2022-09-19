import numpy as np


def gauss_seidel(A, b, x, tolerance=0.01, max_iterations=8):  # Tolerance это параметр точности, короче говоря эпсилон,
    # x это инициализирующий вектор решения, короче говоря x0
    iter1 = 0
    # Iterate
    for k in range(max_iterations):
        iter1 = iter1 + 1
        x = np.array(list(float(round(a, 2)) for a in x))
        if iter1 == max_iterations:
            x = np.array(list(float(round(a)) for a in x))
        print("Вектор решения в итерации #", iter1, "это: ", x)
        x_old = x.copy()

        # Луп через строчки полетели
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]

        # Достаточное условие, сравнение с эпсилон нормы

        LnormInf = max(abs((x - x_old))) / max(abs(x_old))
        print("Норма L в итерации #", iter1, "составляет:", LnormInf)
        if LnormInf < tolerance:
            break

    return x


"""
Данные для проверки
_______________________________
n
4
A
5 1 1 2
1 4 0 2
1 0 1 0
2 2 0 2
b
9 7 2 6
x0
1 0 0 0
_______________________________
n
4
A
5 3 1 0
3 3 0 1
1 0 2 3
0 1 3 1
b
14 14 7 5
x0
0 1 0 0
"""


print('Введите размерность')

n = int(input('Размерность матрицы - '))

print('Введите матричку А')

A = np.array(list(list(map(float, input().split())) for _ in range(n)))

print(f"Вы ввели:\n{A}")

print('Введите вектор b')

b = [float(a) for a in input().split()]

print(f"Вы ввели:\n{b}")

print('Введите инициализирующий вектор решений x0')

x = np.array(list(float(a) for a in input().split()))

print(f"Вы ввели:\n{x}")

print('Метод Зейделя:')

gauss_seidel(A, b, x, max_iterations=4)





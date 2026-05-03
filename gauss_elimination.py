def gauss_elimination(A, b):
    n = len(b)

    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]

    x = [0] * n

    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i][j] * x[j]
        x[i] = (b[i] - s) / A[i][i]

    return x


A = [[2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]]
b = [8, 0, -6]

result = gauss_elimination(A, b)
print(result)
def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0[:]

    for _ in range(max_iter):
        x_old = x[:]

        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]

        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x
    return x

A = [[10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]]

b = [6, 25, -11, 15]
x0 = [0, 0, 0, 0]

result = gauss_seidel(A, b, x0)
print(result)
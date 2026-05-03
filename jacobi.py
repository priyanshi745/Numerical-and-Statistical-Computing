def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0[:]
    
    for _ in range(max_iter):
        x_new = [0] * n
        
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x_new[i] = (b[i] - s) / A[i][i]
        
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new
        
        x = x_new[:]
    
    return x

A = [[10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]]

b = [6, 25, -11, 15]
x0 = [0, 0, 0, 0]

result = jacobi(A, b, x0)
print(result)
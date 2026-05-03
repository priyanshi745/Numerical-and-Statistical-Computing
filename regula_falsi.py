def func(x):
    return x**3 - x - 2

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None

    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    
        if abs(f(c)) < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

root = regula_falsi(func, 1, 2)
print(root)
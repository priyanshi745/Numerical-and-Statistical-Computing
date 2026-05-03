def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    return x

root = newton_raphson(f, df, 1.5)
print(root)
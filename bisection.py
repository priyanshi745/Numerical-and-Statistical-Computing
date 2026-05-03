def func(x):
    return x**3 - x - 2

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) should have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        
        if f(c) == 0 or abs(b - a) / 2 < tol:
            print(f"Root found after {i+1} iterations: {c}")
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Maximum iterations reached.")
    return (a + b) / 2

root = bisection_method(func, 1, 2)
print("Approximate root:", root)
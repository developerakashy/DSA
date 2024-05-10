def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

print("Factorial:",fact(4))

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print("Fibonacci:",fibo(10))
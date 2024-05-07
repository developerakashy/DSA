x = int(input("Ente a number:"))
n = int(input("Enter the power of a number:"))

def power(x,n):
    num = 1
    for i in range(n):
        num = num*x

    return num

print("Normal:",power(x,n))


def efficientPower(x,n):
    if n == 1:
        return x
    
    if n % 2 == 0:
        return efficientPower(x,n/2) * efficientPower(x,n/2)
    return efficientPower(x,n-1) * x

print("efficient:",efficientPower(x,n))
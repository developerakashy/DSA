n = int(input("Enter a number: "))

array = []
def divisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            array.append(i)

divisors(n)
print(array)

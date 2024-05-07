x = int(input("Enter a number: "))
n = int(input("enter power of number: "))

bit_array = []
bit_power = []

res = 1
while n > 0:
    if n % 2 != 0:
        res = res*x
        bit_array.append(1)
        bit_power.append(res)
    
    x = x*x
    n = n//2

print(bit_array,bit_power)

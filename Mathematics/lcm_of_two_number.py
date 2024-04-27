def lcm(a, b):

    max_num = max(a,b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        
        max_num += 1

print("Normal: ",lcm(6,4))

#a * b = gcd(a,b) * lcm(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def efficient_lcm(a, b):
    return a * b // gcd(a, b)

print("Efficient: ",efficient_lcm(6,4))
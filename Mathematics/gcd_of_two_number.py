def euclidean_gcd(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a

print("Normal: ",euclidean_gcd(12,15))


def optimised_euclid_gcd(a, b):
    if b == 0:
        return a
    
    return optimised_euclid_gcd(b, a % b)

print("Optimised: ",optimised_euclid_gcd(15, 12))


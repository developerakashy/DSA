n = int(input("Enter a number: "))

original = n
rev = 0

while n > 0:
    x = n % 10
    rev = (rev * 10) + x
    n = n // 10

if original == rev:
    print("Yes, it's a Palindrome")
else:
    print("No, it's not a Palindrome")
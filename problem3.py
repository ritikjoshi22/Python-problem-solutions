#find greatest common factor among two numbers

def gcd(a, b):
    minNum = min(a, b)
    gcd = 1
    for x in range(1, minNum + 1):
        if a % x == 0 and b % x == 0:
            gcd = x
    return gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)

print("The greatest common factor of", num1, "and", num2, "is:", result)


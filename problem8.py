#Read 3 numbers and write all their common divisors

def commonDivisor(a,b,c):
    smallest = min(a,b,c)
    arr = []

    for x in range(1,smallest+1):
        if(a%x == 0 and b%x == 0 and c%x == 0):
            arr.append(x)

    return arr

print(commonDivisor(6,8,36))
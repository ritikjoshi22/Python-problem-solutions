#compute the sum of all even numbrs between integers a and b, where a<b


def sumEven(a,b):
    s = 0
    if a < b:
        for x in range(a+1,b):
            if x % 2 == 0:
                s += x
    else:
        print('a is greater than b')

    return s

print(sumEven(1,9))
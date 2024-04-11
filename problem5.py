#show the fist n terms of the series:5,7,10,14,19,...,n

def result(n):
    a = 5
    i = 2
    while n-1 != 0:
        a += i
        i += 1
        n -= 1

    return a

num = int(input('Enter a number:'))
print('The value of n:',result(num))
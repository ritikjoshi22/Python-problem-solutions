#Check the given number is perfect number or not. Example of 6, since divisors are 1,2,3 and 1+2+3=6

def perfectNum(n):
    s = 0
    for x in range(1,n):
        if(n % x == 0):
            s += x
    
    if(s == n):
        print('Perfect number')
    else:
        print('Not perfect number')

num = int(input('Enter a number:'))
if(num>0):
    perfectNum(num)
else:
    print('Input must be a positive number')
#Calculate the sum: 1+1/2+1/3+1/4+....+1/N

def harmonicSum(n):
    s = 0
    for x in range(1,n+1):
        s += 1/x
    
    print('Sum:',s)

n = int(input('Enter a number:'))
harmonicSum(n)
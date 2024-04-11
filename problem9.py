def sum(n):
    if(n<=0):
        print('invalid input!')
        return
    a = 1
    s = 0
    while a <= n:
        s += pow(a,2)
        a += 1
    
    return s

print(sum(4))
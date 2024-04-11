#find the first value N for which the following sum exxceeds 10000: 1+2+3+4+...+n

def sum():
    n = 0
    s = 0
    while s <= 10000:
        n += 1
        s += n

    print('The value of N is:',n)

sum()
    
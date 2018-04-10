def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (a == b):
        return a
    elif (a % b == 0):
        return b
    elif (b % a == 0):
        return a
    gcd = 1
    if (a < b):
        m = a
    else:
        m = b
    i = 1
    while (i <= m):
        if (b % i == 0 and a % i == 0):
            a = a // i
            b = b // i
            gcd *= i
            i = 1
        i += 1
    return gcd


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    # Your code here
    gcd = 1
    if (a == b):
        return a
    elif (a == 0):
        return b
    elif (b == 0):
        return a
    else:
        if (a < b):
            return gcdRecur(a, b-a)
        else:
            return gcdRecur(a-b, b)


print(gcdIter(153, 108))
print(gcdRecur(4, 8))

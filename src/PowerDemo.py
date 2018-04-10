def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    s = 1
    for i in range(exp):
        s *= base
    return s


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if (exp == 1):
        return base
    else:
        return base*recurPower(base, exp - 1)


print(iterPower(5, 3))
print(recurPower(5, 3))

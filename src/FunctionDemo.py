def funA():
    print('lalalla')


def funB(x=8):
    print('gugugu')
    return x


def funC(x):
    """
    :param x:lalala
    :return: fafafa
    """
    print('gagaga')
    x = x + 1
    return x


# print(funA())
# print(funB(2))
# print(funB(funC(2)))
# print(funC(funB(funA())))
x = 5
print(funC(x))
print(x)
print(funA)
print(funB(x))
print(x)

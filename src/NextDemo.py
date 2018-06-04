def haha():
    i = 1
    while True:
        yield i
        i += 1


a = haha()
print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


def genPrimes():
    def isPrimes(m):
        for i in range(1, m):
            if m % i == 0 and i != 1 and i != m:
                return False
        return True

    prime = 2
    while True:
        yield prime
        prime += 1
        while (not isPrimes(prime)):
            prime += 1


b = genPrimes()
print(b)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

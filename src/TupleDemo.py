def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    b = ()
    for i in range(len(aTup)):
        print(i)
        if (i % 2 == 0):
            print((aTup[i],))
            b += (aTup[i],)
    return b


print(oddTuples(('a', 'baf', 'c', 'd')))

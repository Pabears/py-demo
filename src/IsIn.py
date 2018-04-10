def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if (char == aStr):
        return True
    elif (char == aStr[0]):
        return True
    elif (len(aStr) == 1 or len(aStr) == 0 or len(char) == 0):
        return False
    else:
        return isIn(char, aStr[1:])


print(isIn('a', 'abc'))

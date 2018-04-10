listA = [1, 2, 3, 4]
listB = listA
listC = listA[:]

print('listA', listA)
print('listB', listB)
print('listC', listC)
print('listA == listB', listA == listB)
print('listA == listC', listA == listC)
print('listC.append(0)', listC.append(0))
print('listA == listC', listA == listC)

print('listB.append(0)', listB.append(0))
print('listA == listB', listA == listB)

print('=======================')

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print('aList', aList)
print('bList', bList)
print('aList == bList', aList == bList)
print('aList is bList', aList is bList)

cList = [6, 5, 4, 3, 2]
print('cList', cList)
dList = []
for num in cList:
    dList.append(num)
print('bList', dList)
print('cList == dList', cList == dList)
print('cList is dList', cList is dList)

testList = [1, -4, 8, -9]
a = testList


def timesFive(a):
    return a // 5


def smap(l, fun):
    m = []
    for elt in map(fun, l):
        m.append(elt)
    return m


def applyToEach(testList, funs):
    m = testList[:]
    for f in funs:
        m = smap(m, f)
        testList.clear()
        testList.extend(m)
    return testList


print(testList is a)
print(applyToEach(testList, [abs]))

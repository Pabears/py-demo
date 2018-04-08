# varA = 5
# varB = 6
# if(type(varA)==str or type(varB)==str):
#     print("string involved")
# else:
#     if(varA>varB):
#         print('bigger')
#     elif(varA<varB):
#         print('smaller')
#     elif(varA==varB):
#         print('equal')

# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))


# num = 0
# while num <= 5:
#     print(num)
#     num += 1
#
# print("Outside of loop")
# print(num)


# num = 10
# while num > 3:
#     num -= 1
#     print(num)

# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')

# for i in range(0, 10, 2):
#     print(i)
# print('"Goodbye!"')

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor)
#     print(type(num/divisor))

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#
# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))

# count =0
# i = 0;
# s = 'bobobobobobolalalalallalalala'
# while(i<len(s)):
#     if(s[i:i+3]=='bob'):
#         count +=1
#     i += 1
# print(count)

temp = ''
pre = 'A'
result = ''
s = "zyxwvutsrqponmlkjihgfedcba"
for i in s:
    if (i < pre):
        temp = ''
    else:
        if (len(temp) == 0 and pre != 'A'):
            temp = pre
        temp = temp + i
        if (len(temp) > len(result)):
            result = temp
    pre = i
print("Longest substring in alphabetical order is: "+result)

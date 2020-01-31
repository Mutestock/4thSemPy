
# 1.

############
# A.

import math
names = ["Derp", "Herp", "Cake", "John", "Mark",
         "Hymn", "Hailey", "Neith", "Noth", "Herakles"]

for name in names:
    if(name[:1].upper() == "H"):
        print(name)


############
# B.


powerList = [i**3 for i in range(1, 100)]
# print(powerList)


###########
# C.


tupleList = [(len(name), name) for name in names]
# print(tupleList)


#########
# D


string_to_sort = "daspiufh98saay39p8a3fh8w3f90ahsdf90as70vbsad0ag79803+3i+11u823+912"
string_to_return = ""

for s in string_to_sort:
    if(s.isdigit()):
        string_to_return += str(s)
# print("Nummeric Filtered String: " + string_to_return)


############
# E.


# Sets can only contain unique values. Converted i to string to differentiate between the two.

diceListThing = [set([str(i), j]) for i in range(1, 7)
                 for j in range(1, 7)]
# print(diceListThing)


###############
# 2.
###############
# A.

dictNames = {name: len(name) for name in names}
# print(dictNames)


##############
# B


numList = [123, 124, 12413, 16, 16, 21, 621, 3324, 123, 11, 23, 77171712, 1243]
numDict = {number: math.sqrt(number) for number in numList}
# print(numDict)


##########
# 3.
#########
'''
I am going to assume that the assignment description refers to the sum of the values
There's probably a nicer way of doing this.
'''


def incoming(num):
    res = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if(i+j is num):
                res += 1
    return round(res/36*10000)/100


dictDiceChanceThing = [{i+j: incoming(i+j)}
                       for i in range(1, 7) for j in range(1, 7)]
print(dictDiceChanceThing)

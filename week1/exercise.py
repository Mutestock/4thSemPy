import math

# 1.
# Create 5 list comprehensions to solve the following 5 problems:

############
# A.
# Iterate a list of names to return a list of the names starting with H

names = ["Derp", "Herp", "Cake", "John", "Mark",
         "Hymn", "Hailey", "Neith", "Noth", "Herakles"]

h_name_list = [name for name in names
               if(name[:1].upper() == "H")]
# print(h_name_list)

############
# B.
# In one line create a list of the numbers 1-100 to the power of 3

power_list = [i**3 for i in range(1, 100)]
# print(power_list)


###########
# C.
# Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name

tuple_list = [(len(name), name) for name in names]
# print(tuple_list)


#########
# D
# iterate over each character in a string and get only those that are nummeric

string_to_sort = "daspiufh98saay39p8a3fh8w3f90ahsdf90as70vbsad0ag79803+3i+11u823+912"

sorted_string_list = [s for s in string_to_sort
                      if(s.isdigit())]
# print(sorted_string_list)


############
# E.
# Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice

''' Sets can only contain unique values. Converted i to string to differentiate between the two.'''

dice_list_thing = [set([str(i), j]) for i in range(1, 7)
                   for j in range(1, 7)]
# print(dice_list_thing)


###############
# 2.
# Create 2 dictionary comprehensions to solve the following:
###############
# A.
# Iterate a list of names and create a dictionary where key is the name and value is the length of the name


dict_names = {name: len(name) for name in names}
# print(dict_names)


##############
# B
# Iterate a list of numbers and create a dictionary with (key, value) being (number, squareroot of number)

num_list = [123, 124, 12413, 16, 16, 21,
            621, 3324, 123, 11, 23, 77171712, 1243]
num_dict = {number: math.sqrt(number) for number in num_list}
# print(num_dict)


##########
# 3.
#########

# Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys and their likelyhood in percent as values

'''
I am going to assume that the assignment description refers to the sum of the values
There's probably a nicer way of doing this.
'''


def CalcOdds(num):
    res = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if(i+j is num):
                res += 1
    return round(res/36*10000)/100


dict_dice_chance_thing = [{i+j: CalcOdds(i+j)}
                          for i in range(1, 7) for j in range(1, 7)]
print(dict_dice_chance_thing)

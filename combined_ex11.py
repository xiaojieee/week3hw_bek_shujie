Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 1 hyphen same length as the Belgium String

# print(len(Belgium)) This find out the length of the string is 81
# print('-' * 81)
print('-' * len(Belgium))
# combined the 2 steps into 1 step

# 2 - the string with the comma separators replaced by colons ':'
updated_string = Belgium.replace(",", ":")
print(updated_string)
# prints Belgium:10445852:Brussels:737966:Europe:1830:Euro:Catholicism:Dutch:French:German

# 3 - the population of Belgium (the second field) plus the population of the capital city (the fourth field).
# HINT: the answer should be 11183818
# use split method to split the original string into a list adding comma as separator
Belgium_split = Belgium.split(',')
print(Belgium_split)
# prints:
# ['Belgium', '10445852', 'Brussels', '737966', 'Europe', '1830', 'Euro', 'Catholicism', 'Dutch', 'French', 'German']

# convert to an integer for addition. If left as a string then the two numbers would be concatenated together
# concatenation of strings would result in 10445852737966
# population of Belgium is the second field which is index 1 (starts at 0)
num1 = int(Belgium_split[1])
print(f"The population of Belgium is {num1}")
# prints: The population of Belgium is 10445852

# population of the capital city is the fourth field which is index 3
num2 = int(Belgium_split[3])
print(f"The population of Brussels is {num2}")
# prints: The population of Brussels is 737966

print(f"The population of Belgium and Brussels is {num1 + num2}")
# prints: The population of Belgium and Brussels is 11183818

# ------- Shujie's Method -------

# # 3 work out the total population
#
# pop_bel = int(belgium_colon.split(':')[1])
# pop_bru = int(belgium_colon.split(':')[3])
# # int method - assuming the string value is an integer
# # [1] refers to the place of the field in the list
# # remember it starts from [0]
#
# total_population = pop_bel + pop_bru
# print("'The total population of Belgium:', total_population")
#
# # shorten to one line using an f-string
# print(f"The total population of Belgium: {int(belgium_colon.split(':')[1]) + int(belgium_colon.split(':')[3])}")
#
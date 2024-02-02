Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# EXERCISE: Add code to print:
# a - a line of hyphens the same length as the Belgium string

# prints the whole string
print(Belgium)
# prints: Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German

# calculate the length of the string
string_length = len(Belgium)
# prints the number of characters in the string
print(string_length)
# prints: 81

# b - the string with the comma separators replaced by colons ':'
updated_string = Belgium.replace(",", ":")
print(updated_string)
# prints Belgium:10445852:Brussels:737966:Europe:1830:Euro:Catholicism:Dutch:French:German

# c - the population of Belgium (the second field) plus the population of the capital city (the fourth field).
# HINT: the answer should be 11183818
# use split method to split a string into a list by removing the commas and inserting a space
Belgium_list = Belgium.replace(",", " ")

# split works when words have a space between them. Without previous step it would split the characters rather than separate into words
list_split = Belgium_list.split()
print(list_split)
# prints: ['Belgium', '10445852', 'Brussels', '737966', 'Europe', '1830', 'Euro', 'Catholicism', 'Dutch', 'French', 'German']

# convert to an integer for addition. If left as a string then the two numbers would be concatenated together
# concatenation of strings would result in 10445852737966
# population of Belgium is the second field which is index 1 (starts at 0)
num1 = int(list_split[1])
print(f"The population of Belgium is {num1}")
# prints: The population of Belgium is 10445852

# population of the capital city is the fourth field which is index 3
num2 = int(list_split[3])
print(f"The population of Brussels is {num2}")
# prints: The population of Brussels is 737966

print(f"The population of Belgium and Brussels is {num1 + num2}")
# prints: The population of Belgium and Brussels is 11183818


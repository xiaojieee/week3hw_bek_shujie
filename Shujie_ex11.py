Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 1 hyphen same length as the Belgium String

# print(len(Belgium)) This find out the length of the string is 81
# print('-' * 81)
print('-' * len(Belgium))
# combined the 2 steps into 1 step


# 2 replace the commas to colon in the string

belgium_colon = Belgium.replace(',', ':')
# .replace is a method to replace characters in the string
print(belgium_colon)
print(belgium_colon.split(':'))
# the split() method splits the string into a list
# similarly rsplit() method splits a string into a list, starting from the right


# 3 work out the total population

pop_bel = int(belgium_colon.split(':')[1])
pop_bru = int(belgium_colon.split(':')[3])
# int method - assuming the string value is an integer
# [1] refers to the place of the field in the list
# remember it starts from [0]

total_population = pop_bel + pop_bru
print('The total population of Belgium:', total_population)

# shorten to one line using an f-string
print(f"The total population of Belgium: {int(belgium_colon.split(':')[1]) + int(belgium_colon.split(':')[3])}")

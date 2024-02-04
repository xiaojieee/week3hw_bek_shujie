# //////// LITERAL STRING INTERPOLATION ////////

# ------ Learner Guide -------
# Mistake in learner guide with [3] instead of 2, giving 'Mary as the third member which is wrong?
# Index starts at 0, therefore use index of 2 for the third name in list
names = ['Tom', 'Harry', 'Jane', 'Mary']
# Uses an f-string. Removes excessive concatenation and using .format() method which isn't as clean
# the variable is placed within {} and the index after which is in []
string = f"The third member is {names[2]}"
# print the string
print(string)
# prints: The third member is Jane

# ------ Learner Guide -------
# Not just variable values may be represented
names = ['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1
string = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
print(string)
# prints: 2nd of 4 is Harry

# Can also be combined with raw strings
drive = 'C:'
dir = 'Windows'
path = fr"{drive}\{dir}"
print(path)
# prints: C:\Windows

# ------ My Version -------
shopping_list = ['Bananas', 'Milk', 'Eggs', 'Cheese', 'Bread', 'Washing Powder']
string = f"The fourth item on my shopping list is {shopping_list[3]}"
print(string)
# prints: The fourth item on my shopping list is Cheese


# ------ Learner Guide -------
# Slicing a String
# Slice by start and end position
text = "Remarkable bird, the Norwegian Blue"
# counts from left to right, starts at index 11 which is the 12th character and up to (but not including) index 14
print(text[11:14])
# prints: bir

# counts from right to left starting index 7 from the end to 1 from the end
print(text[-7:-1])
# prints: an Blu

# counts from the start up to, but not including, index 14
print(text[:14])
# prints: Remarkable bir

# counts -7 from the end up to the end of the string
print(text[-7:])
# prints: an Blue

# the third value is the 'step'
# print every other (2nd) character starting at index 5 and ending at (but not including) index 15
text = "Now that's what I call a dead parrot."
print(text[5:15:2])
# prints htswa

# name[::-1] reverses the string. ':' indicates start/end of slice. Left empty so defaults to entire string
# -1 is the step, moving backwards one character at a time through the string
# .upper() method converts all lowercase letters to uppercase
name = "david bowie"
print(name[::-1].upper())
# prints: EIWOB DIVAD

# ------ My Version -------

# Full code = print(', '.join(name.split()[::-1]).title())
# Breakdown line by line...
# name.split() method splits the string into a list based on whitespace, therefore gives each name as a list item
print(name.split())
# prints: ['david', 'bowie']

# [::-1] from exercise example reverses the 'list' rather than characters
print(name.split()[::-1])
# prints: ['bowie', 'david']

# .join() method joins the elements of the list into a string with specified separator of a comma and space
print(', '.join(name.split()[::-1]))
# prints: bowie, david

# .title() method converts the first letter of each word to uppercase
print(', '.join(name.split()[::-1]).title())
# prints: Bowie, David

# ------ Learner Guide -------
# String Methods - Split and Join
line = 'root::0:superuser:/root:/bin/sh'
elems = line.split(':')

elems[0] = 'avatar'
elems[4] = 'The super-user (zero)'
line = ':'.join(elems)
print(line)
# prints: avatar::0:superuser:The super-user (zero):/bin/sh


# Nick Cave Into My Arms

# Researching using most_common() method to find the most common element (word in my usage) in a collection
# most_common() is typically used with collections.Counter class
# import Counter from collections module to count objects eg word occurrence
from collections import Counter

lyrics = (
"I don't believe in an interventionist God\nBut I know darling that you do\nBut if I did I would kneel down and ask Him"
"\nNot to intervene when it came to you\nNot to touch a hair on your head\nTo leave you as you are\n"
"And if He felt He had to direct you\nThen direct you into my arms"
)
print(lyrics)
# prints lyrics as written above

print("-------- Word count --------")

# .lower() converts all characters to lowercase
# .split() splits string into list of words using whitespace as separator
words = lyrics.lower().split()
# print the list
print(words)
# use Counter on the list 'words' to count occurrence of each word and store in new 'word_count' variable
word_count = Counter(words)
# prints as a dictionary with each key (word) and value (occurrence)
# print(word_count)
# use .most_common() method to show the top 10 words in order of highest occurrence
print(word_count.most_common(10))

# -------- Version 2 (Slice) --------

print("-------- String Split Method --------")
# split the original lines of the lyrics string into a list
# .split('\n') method splits the strings in the lyrics variable by the newline separator and returns a list of strings
lyric_lines = lyrics.split('\n')
# print to verify split worked
print(lyric_lines)

# create an empty list to store the sliced lyrics
sliced_lyrics = []
# enumerate() function used as iterating over an iterable - provides both index and value of each item in the list
# therefore the for loop iterates over the list of lyric lines with index AND the line
for index, line in enumerate(lyric_lines):
    # if statement used to apply slice operation to individual lines based on index position
    # for first line (index 0) append the last 3 characters of the line to sliced_lyrics list
    if index == 0:
        sliced_lyrics.append(line[-3:])
    # for second line (index 1) append the last 6 characters of the line to sliced_lyrics list
    elif index == 1:
        sliced_lyrics.append(line[-6:])
    # for third line (index 2) append characters from position 21 to 23 of the line to sliced_lyrics list etc...
    elif index == 2:
        sliced_lyrics.append(line[21:31])
    elif index == 3:
        sliced_lyrics.append(line[4:16])
    elif index == 4:
        sliced_lyrics.append(line[4:12])
    elif index == 5:
        sliced_lyrics.append(line[:8])
    elif index == 6:
        sliced_lyrics.append(line[:3])
    elif index == 7:
        sliced_lyrics.append(line[5:11])
# print the list
print(sliced_lyrics)

# use .join() method to join list items into a string, separating with a space
# .lower() converts the entire string to lowercase
new_lyrics = ' '.join(sliced_lyrics).lower()
# print the string
# .capitalize() converts the first letter/character of the sentence to a capital
print((new_lyrics).capitalize())
# prints: God you do kneel down to intervene to touch to leave and direct

# -------- Version 1 (Slice) --------

line1 = "I don't believe in an interventionist God"
line2 = "But I know darling that you do"
line3 = "But if I did I would kneel down and ask Him"
line4 = "Not to intervene when it came to you"
line5 = "Not to touch a hair on your head"
line6 = "To leave you as you are"
line7 = "And if He felt He had to direct you"
line8 = "Then direct you into my arms"

sliced_lyrics = []
sliced_lyrics.append(line1[-3:])
sliced_lyrics.append(line2[-6:])
sliced_lyrics.append(line3[21:31])
sliced_lyrics.append(line4[4:16])
sliced_lyrics.append(line5[4:12])
sliced_lyrics.append(line6[:8])
sliced_lyrics.append(line7[:3])
sliced_lyrics.append(line8[5:11])

new_lyrics = ' '.join(sliced_lyrics).lower()
print((new_lyrics).capitalize())

# -------- NOTES --------
'''
Using enumerate in a for loop allows us to loop over an iterable and, at the same time, keep track of the index of the 
current item. Using a counter variable, on the other hand, requires us to manually increment the variable inside the 
loop and keep track of the index ourselves.
'''

# basic syntax of the enumerate() function:
# iterable: The iterable you want to loop through while enumerating its elements.
# start (optional): An optional argument that specifies the starting index value for enumeration. By default, it starts from 0.
# enumerate(iterable, start=0)

# fruits = ["apple", "banana", "cherry", "pear"]
#
# for index, fruit in enumerate(fruits):
#     print(f"Index {index}: {fruit}")
# # prints:
# # Index 0: apple
# # Index 1: banana
# # Index 2: cherry
# # Index 3: date
#
# # Or specify a starting index:
# for index, fruit in enumerate(fruits, start=1):
#     print(f"Index {index}: {fruit}")
# # Index 1: apple
# # Index 2: banana
# # Index 3: cherry
# # Index 4: date




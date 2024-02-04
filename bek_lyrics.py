# Nick Cave Into My Arms
# import Counter from collections module to count objects eg word occurrence
from collections import Counter

lyrics = (
"I don't believe in an interventionist God\nBut I know darling that you do\nBut if I did I would kneel down and ask Him"
"\nNot to intervene when it came to you\nNot to touch a hair on your head\nTo leave you as you are\n"
"And if He felt He had to direct you\nThen direct you into my arms"
)
print(lyrics)
# prints lyrics as written above

print("Word count:")

# converts all words to lowercase and splits into list items
words = lyrics.lower().split()
# print the list
print(words)
# use Counter on the list 'words' to count occurrence of each word and store in new 'word_count' variable
word_count = Counter(words)
# use .most_common() method to show the top 10 words in order of highest occurrence
print(word_count.most_common(10))

# -----------------------------------------------------

print("Using split method to rework lyrics:")
# split the original lyrics string into a list of lines
# each line is separated by the newline character '\n'
lyric_lines = lyrics.split('\n')
# print to verify split worked
print(lyric_lines)

# create an empty list to store the sliced lyrics
sliced_lyrics = []
# for loop iterates over each line
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




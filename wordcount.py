"""
Exercise 06
Text Parsing Mark Twain / Fun with Dictionaries
"""

twain = open('twain.txt')
lines = []

for line in twain:
    lines.append(line.lower())

words = []

# in this for loop we split the text by whitespace and dumped it in a list called words
for i in range(len(lines)):
    words.extend(lines[i].split())

# strip the leading and trailing punctuation from the text
def clean_text(words):
    dirty_words = words
    for item in range(len(dirty_words)):
        dirty_words[item] = dirty_words[item].strip('-,.:;!?"')
    return dirty_words

text = clean_text(words)

word_counts = dict()

# create a dictionary with unique words as keys and counts as their values
for w in range(len(text)):
    clean_word = text[w]
    if word_counts.get(text[w]):
        word_counts[clean_word] +=1
    else:
        word_counts[clean_word] = 1

print word_counts

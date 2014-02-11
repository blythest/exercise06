"""
Exercise 06
Text Parsing Mark Twain / Fun with Dictionaries
"""

from sys import argv
import operator

script, filename = argv

myfile = open(filename, "r")
lines = []

for line in myfile:
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

# for key, value in word_counts.iteritems():
#     print key, value

# sorting dictionary by word_frequency (values)
sorted_word_frequencies = sorted(word_counts.iteritems(), key=operator.itemgetter(1), reverse=True)
# print sorted_word_frequencies

new_dict = dict()
# create a new dictionary with frequency as key and words as values in a list
for key, value in word_counts.iteritems():
    new_key = value
    new_value = key
    if new_dict.get(new_key):
        # print new_scores[new_key]
        new_dict[new_key].append(new_value)
    else:
        new_dict[new_key] = [new_value]

# sort the each value in the dictionary new_dict alphabetically
for key, value in new_dict.iteritems():
    new_dict[key] = sorted(new_dict[key])

for key in sorted(new_dict.iterkeys()):
     print "%s: %s" % (key, new_dict[key])
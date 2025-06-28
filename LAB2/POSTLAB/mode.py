"""
File: mode.py
Prints the mode of a set of words in a file using stats.py.
"""

from stats import mode

fileName = input("Enter the file name: ")
with open(fileName, 'r') as f:
    # Input the text, convert words to uppercase, and add to list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())

# Convert words to a frequency countable format
# mode() expects numbers, so you need a custom version for words
# Let's define a simple word-mode logic directly for now:
if not words:
    print("The mode is 0")
else:
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    max_freq = max(word_counts.values())
    for key in word_counts:
        if word_counts[key] == max_freq:
            print("The mode is", key)
            break

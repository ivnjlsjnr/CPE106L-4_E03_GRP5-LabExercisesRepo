"""
File: median.py
Prints the median of a set of numbers in a file using stats.py.
"""

from stats import median

fileName = input("Enter the file name: ")
with open(fileName, 'r') as f:
    # Read numbers from the file into a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

# Use the imported function
print("The median is", median(numbers))

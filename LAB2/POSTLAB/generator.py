"""
Program: generator.py
Author: Ken (Modified)
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random from external text files.
"""

import random
import os

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    if not os.path.exists(filename):
        print(f"[Error] File not found: {filename}")
        return ()
    with open(filename, 'r') as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return tuple(words)

# Load vocabulary from files in the same directory
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    if not all((articles, nouns, verbs, prepositions)):
        print("[Program terminated] One or more vocabulary files are missing or empty.")
        return

    try:
        number = int(input("Enter the number of sentences: "))
        print("\nGenerated Sentences:\n")
        for count in range(number):
            print(f"{count + 1}. {sentence().capitalize()}.")
    except ValueError:
        print("[Error] Please enter a valid number.")

# Entry point for program execution
if __name__ == "__main__":
    main()

"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    # Comparison methods
    def __eq__(self, other):
        """Returns True if names are equal."""
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if this student's name is less than the other's."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns True if this student's name is greater than or equal to the other's."""
        return self.name >= other.name

def main():
    # Create multiple students with different names and scores
    students = [
        Student("Charlie", 3),
        Student("Alice", 3),
        Student("Eve", 3),
        Student("Bob", 3)
    ]

    # Set sample scores
    for student in students:
        student.setScore(1, 90)
        student.setScore(2, 85)
        student.setScore(3, 88)

    print("Original list:")
    for s in students:
        print(s)
        print("-" * 30)

    # Shuffle the list
    random.shuffle(students)
    print("Shuffled list:")
    for s in students:
        print(s)
        print("-" * 30)

    # Sort the list
    students.sort()
    print("Sorted list:")
    for s in students:
        print(s)
        print("-" * 30)

if __name__ == "__main__":
    main()

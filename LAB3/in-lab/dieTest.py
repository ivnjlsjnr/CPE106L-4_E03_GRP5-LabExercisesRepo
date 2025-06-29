from die import Die

def main():
    # Create a Die object
    my_die = Die()

    print("Initial die value:", my_die.getValue())

    # Roll the die 5 times
    print("Rolling the die 5 times...")
    for i in range(5):
        my_die.roll()
        print(f"Roll {i + 1}: {my_die.getValue()}")

if __name__ == "__main__":
    main()

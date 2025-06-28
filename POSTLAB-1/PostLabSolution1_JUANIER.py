# file_navigator.py

def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return

    num_lines = len(lines)
    print(f"\nThe file '{filename}' has {num_lines} lines.")

    while True:
        try:
            line_number = int(input(f"\nEnter a line number between 1 and {num_lines} (0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if line_number == 0:
            print("Exiting program.")
            break
        elif 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
        else:
            print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")

if __name__ == "__main__":
    main()

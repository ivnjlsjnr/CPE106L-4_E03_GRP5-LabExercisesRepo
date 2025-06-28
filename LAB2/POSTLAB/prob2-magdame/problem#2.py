def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    if not lines:
        print("The file is empty.")
        return

    while True:
        print(f"\nThe file has {len(lines)} lines.")
        try:
            line_num = int(input(f"Enter a line number (1-{len(lines)}) or 0 to quit: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if line_num == 0:
            print("Exiting.")
            break
        elif 1 <= line_num <= len(lines):
            print(f"Line {line_num}: {lines[line_num - 1].rstrip()}")
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    main()
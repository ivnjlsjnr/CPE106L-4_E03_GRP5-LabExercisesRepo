def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    # If every value appears only once, return the first one as mode
    return modes[0]

def main():
    data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

if __name__ == "__main__":
    main()
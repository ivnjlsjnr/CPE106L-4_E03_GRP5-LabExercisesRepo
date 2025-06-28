def mean(numbers):
    """Return the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the median of a list of numbers."""
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
    """Return the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    if len(modes) == 1:
        return modes[0]
    return min(modes)  # Return the smallest mode in case of multiple


def main():
    """Test the statistical functions with a sample list."""
    test_data = [1, 2, 3, 4, 4, 5, 5, 5, 6]
    print("Data:", test_data)
    print("Mean:", mean(test_data))
    print("Median:", median(test_data))
    print("Mode:", mode(test_data))


if __name__ == "__main__":
    main()

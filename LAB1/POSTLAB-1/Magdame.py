def mean(numbers):
    """Return the mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the median of a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def mode(numbers):
    """Return the mode of a list of numbers. If multiple modes, returns the smallest one."""
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    return min(modes)

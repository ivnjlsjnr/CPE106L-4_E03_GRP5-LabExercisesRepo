# stats.py

def mean(numbers):
    """Returns the mean (average) of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def median(numbers):
    """Returns the median of a list of numbers."""
    if not numbers:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def mode(numbers):
    """Returns the mode of a list of numbers. If multiple modes, returns the smallest one."""
    if not numbers:
        return None
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]

    return min(modes)  # Return the smallest mode if multiple

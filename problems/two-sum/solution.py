def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Given a list of integers `numbers` and a target integer `target`, returns a list of the indices of the two numbers that add up to `target`.

    :param numbers: A list of integers to search through.
    :type numbers: list[int]
    :param target: An integer that the two numbers should add up to.
    :type target: int
    :return: A list of two integers representing the indices of the two numbers in `numbers` that add up to `target`.
    :rtype: list[int]
    """
    sorted_numbers = sorted(numbers)
    first, last = 0, len(sorted_numbers) - 1
    while last > first:
        if sorted_numbers[first] + sorted_numbers[last] == target:
            first = numbers.index(sorted_numbers[first])
            numbers = numbers[::-1]
            last = len(numbers) - numbers.index(sorted_numbers[last]) - 1
            return [first, last]
        if sorted_numbers[first] + sorted_numbers[last] < target:
            first += 1
        else:
            last -= 1
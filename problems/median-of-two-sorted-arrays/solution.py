def find_median(numbers: list) -> int:
    """
    Given a list of integers `numbers`, returns the median value of the list. If the list has an even number of elements, the function returns the average of the middle two elements.

    :param numbers: A list of integers to find the median of.
    :type numbers: list
    :return: The median value of the list.
    :rtype: int
    """
    length = len(numbers)
    if len(numbers) % 2 == 1:
        return numbers[length // 2]
    elif len(numbers) % 2 == 0:
        return (numbers[length // 2] + numbers[(length - 1) // 2]) / 2 

def find_median_sorted_arrays(numbers_one: list, numbers_two: list) -> int:
    """
    Given two sorted lists of integers `numbers_one` and `numbers_two`, returns the median value of the combined lists.

    :param numbers_one: A sorted list of integers.
    :type numbers_one: list
    :param numbers_two: A sorted list of integers.
    :type numbers_two: list
    :return: The median value of the combined lists.
    :rtype: int
    """
    return find_median(sorted(numbers_one + numbers_two))
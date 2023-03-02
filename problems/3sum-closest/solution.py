def three_sum_closest(numbers: list, target: int) -> int:
    """
    Find the sum of three numbers in a list that is closest to a given target.

    :param numbers: a list of integers
    :type numbers: list
    :param target: an integer representing the target sum
    :type targer: int
    :return: an integer representing the closest sum of three numbers in the list
    :rtype: int
    """
    numbers = sorted(numbers)
    answer = numbers[0] + numbers[1] + numbers[2]
    for index, number in enumerate(numbers):
        left, right = index + 1, len(numbers) - 1
        while left < right:
            local_result = number + numbers[left] + numbers[right]
            if abs(local_result - target) < abs(answer - target):
                answer = local_result
            if local_result == target:
                return target
            elif local_result > target:
                right -= 1
            elif local_result < target:
                left += 1
    return answer
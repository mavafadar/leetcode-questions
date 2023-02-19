def three_sum(numbers: list) -> list:
    """
    Given an array `numbers` of n integers, returns all unique triplets
    `[numbers[i], numbers[j], numbers[k]]` such that `i != j != k` and `i, j, k`
    are indices in the array, and `numbers[i] + numbers[j] + numbers[k] == 0`.
    The solution set must not contain duplicate triplets. The elements in each triplet
    should be ordered in non-descending order.

    :param numbers: A list of integers
    :type numbers: list
    :return: A list of unique triplets whose sum is 0
    :rtype: list
    """
    answer = list()
    numbers = sorted(numbers)
    for index, number in enumerate(numbers[:len(numbers) - 1]):
        if index != 0 and number == numbers[index - 1]:
            continue
        left_pointer, right_pointer = index + 1, len(numbers) - 1
        while left_pointer < right_pointer:
            summation = number + numbers[left_pointer] + numbers[right_pointer]
            if summation == 0:
                answer.append([number, numbers[left_pointer], numbers[right_pointer]])
                left_pointer += 1
                while numbers[left_pointer] == numbers[left_pointer - 1] and left_pointer < right_pointer:
                    left_pointer += 1
            elif summation > 0:
                right_pointer -= 1
            elif summation < 0:
                left_pointer += 1
    return answer
MAX_INT = 2147483647
MIN_INT = -2147483648


def reverse(number: int) -> int:
    """
    Reverses the digits of an integer number.

    :param number: The integer to be reversed.
    :type number: int

    :return: The reversed integer. Returns 0 if the reversed integer is outside the range [-2147483648, 2147483647].
    :rtype: int
    """
    reversed_number = 0
    negative_flag = number < 0
    number = abs(number)
    while number != 0:
        pop = number % 10
        number = number // 10
        if reversed_number > MAX_INT // 10 or (
                reversed_number == MAX_INT // 10 and pop > 7 and negative_flag is False) or (
                reversed_number == MAX_INT // 10 and pop > 8 and negative_flag is True):
            return 0
        reversed_number = reversed_number * 10 + pop
    return reversed_number if negative_flag is False else -1 * reversed_number

def is_palindrome(x: int) -> bool:
    """
    Determine if a given integer is a palindrome.

    :param x: The integer to check for palindromicity.
    :type x: int
    :return: True if the integer is a palindrome, False otherwise.
    :rtype: bool
    """
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False
    reversed_number = int(str(x)[::-1])
    return True if reversed_number == x else False
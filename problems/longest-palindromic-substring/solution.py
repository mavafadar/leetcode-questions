def is_palindrome(string: str) -> bool:
    """
    Given a string `string`, checks if it is a palindrome.

    :param string: The input string to check for palindrome.
    :type string: str
    :return: True if the input string is a palindrome, False otherwise.
    :rtype: bool
    """
    return string == string[::-1]


def longest_palindrome(string: str) -> str:
    """
    Given a string `string`, finds and returns the longest palindrome substring in the string.

    :param string: The input string to search for the longest palindrome substring.
    :type string: str
    :return: The longest palindrome substring found in the input string.
    :rtype: str
    """
    length = len(string)
    start_index = 0
    while True:
        if start_index + length == len(string) + 1:
            length -= 1
            start_index = 0
            continue
        if is_palindrome(string[start_index:start_index + length]):
            return string[start_index:start_index + length]
        start_index += 1
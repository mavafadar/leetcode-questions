MAX_INT = 2147483647
MIN_INT = -2147483648


def my_atoi(string: str) -> int:
    """
    Converts a string to an integer.

    This function converts the given string to an integer. If the string
    does not represent a valid integer, this function returns 0.

    The conversion ignores leading and trailing white space. A string
    starting with a '+' or '-' sign is valid input. If the string
    contains any other characters besides digits or the sign character,
    they will be ignored. The output will be bounded to the 32-bit
    signed integer range [-2147483648, 2147483647].

    :param string: The string to be converted.
    :type string: str
    :return: The converted integer.
    :rtype: int
    """
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sign = ['+', '-']
    string = string.strip()
    final_answer = str()
    if len(string) > 1 and string[0] in sign:
        final_answer += string[0]
        string = string[1:]
    for character in string:
        if character in characters:
            final_answer += character
        if character not in characters:
            break
    return 0 if final_answer in sign + [''] else max(min(int(final_answer), MAX_INT), MIN_INT)
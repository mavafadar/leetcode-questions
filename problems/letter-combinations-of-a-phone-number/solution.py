def letter_combinations(digits: str) -> list:
    """
    Generate all possible letter combinations that can be formed from the digits of a phone number.

    :param digits: A string of digits representing a phone number.
    :type digits: str
    :return: A list of strings representing all possible letter combinations of the input digits.
    :rtype: list[str]

    Example:
    >>> letter_combinations("23")
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    If the input string is empty, the function will return an empty list.

    .. note:: The input string should only contain digits 2 to 9, inclusive.
    """
    if not digits:
        return []

    hash_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    answers = hash_map.get(digits[0], [])
    for number in digits[1:]:
        new_characters = hash_map.get(number, [])
        answers = [answer + new_character for answer in answers for new_character in new_characters]

    return answers

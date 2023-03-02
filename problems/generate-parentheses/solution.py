def generate_parenthesis(number: int) -> list:
    """
    Generate all combinations of well-formed parentheses consisting of `number` pairs.

    :param number: The number of pairs of parentheses to generate combinations for.
    :type number: int
    :return: A list of strings, where each string represents a combination of well-formed parentheses.
    :rtype: list
    """
    result = list()
    generateParenthesisHelper(result, str(), 0, 0, number)
    return result


def generateParenthesisHelper(result: list, string: str, _open: int, close: int, number: int):
    """
    A helper function for generating all valid parentheses combinations.

    Parameters:
    :param result: The list of valid parentheses combinations.
    :type result: list
    :param string: The current parentheses string being constructed.
    :type string: str
    :param _open: The number of open parentheses in the current string.
    :type _open: int
    :param close: The number of close parentheses in the current string.
    :type close: int
    :param number: The total number of parentheses pairs to use.
    :type number: int
    :return: The valid parentheses combinations are added to the result list.
    :rtype: None
    """
    if _open == number and close == number:
        result.append(string)
        return
    if _open < number:
        generateParenthesisHelper(result, string + '(', _open + 1, close, number)
    if close < _open:
        generateParenthesisHelper(result, string + ')', _open, close + 1, number)
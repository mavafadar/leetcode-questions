
def is_valid(string: str) -> bool:
    """
    Checks if a string of parentheses, brackets, and curly braces is valid.
    Valid strings have opening and closing brackets of the same type in the correct order.

    :param string: A string containing only parentheses, brackets, and curly braces.
    :type string: str
    :return: True if the string is valid, False otherwise.
    :rtype: bool
    """
    stack = [0]
    
    if len(string) == 0:
        return True

    for character in string:
        if character in ["(", "{", "["]:
            stack.append(character)
        if character == ")" and stack[-1] == "(" or character == "]" and stack[-1] == "[" or character == "}" and stack[-1] == "{":
            stack.pop()
        elif character == ")" and stack[-1] != "(" or character == "]" and stack[-1] != "[" or character == "}" and stack[-1] != "{":
            return False
    
    return True if len(stack) == 1 else False
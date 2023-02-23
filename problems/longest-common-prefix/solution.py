def longestCommonPrefix(strings: list) -> str:
    """
    Finds the longest common prefix string amongst a list of strings.

    :param strings: A list of strings.
    :type strings: list
    :return: The longest common prefix string if there is one, or an empty string if there isn't.
    :rtype: str
    """
    if len(strings) == 1:
        return strings[0]
    
    shortest_string = min(strings, key=len)
    
    for index, character in enumerate(shortest_string):
        for string in strings:
            if string[index] != character:
                return shortest_string[:index]
            
    return shortest_string
        
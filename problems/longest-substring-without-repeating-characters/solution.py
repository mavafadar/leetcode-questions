def length_of_longest_substring(string: str) -> int:
    """
   Given a string `string`, returns the length of the longest substring within `string` that contains no repeating characters.

   :param string: A string to search through.
   :type string: str
   :return: The length of the longest substring within `string` that contains no repeating characters.
   :rtype: int
       """
    local_answer, final_answer, index = 0, 0, 0
    characters_dict = dict()
    while index != len(string):
        if string[index] in characters_dict:
            final_answer = max(final_answer, local_answer)
            local_answer = 0
            index = characters_dict[string[index]] + 1
            characters_dict = dict()
        characters_dict[string[index]] = index
        local_answer += 1
        index += 1
    return max(final_answer, local_answer)
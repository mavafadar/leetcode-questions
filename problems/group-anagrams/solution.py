def group_anagrams(strings: list) -> list:
    """
    Group a list of strings into lists of anagrams.

    :param strings: A list of strings to group into anagrams.
    :type strings: list
    :return: A list of lists, where each inner list contains all the strings from the input list that are anagrams of each other.
    :rtype: list
    """
    hash_map = dict()
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in hash_map.keys():
            hash_map[sorted_word].append(word)
        else:
            hash_map[sorted_word] = [word]
    return hash_map.values()
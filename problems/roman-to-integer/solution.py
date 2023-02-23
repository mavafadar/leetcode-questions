def roman_to_integer(string: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    :param string: A string containing a Roman numeral.
    :type string: str
    :return: The integer value corresponding to the Roman numeral.
    :rtype: int
    """
    roman_to_int_dict_single = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    roman_to_int_dict_double = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    
    answer, index = 0, 0
    while index < len(string):
        if len(string) > index + 1 and string[index: index+2] in roman_to_int_dict_double:
            answer += roman_to_int_dict_double[string[index: index+2]]
            index += 2
        else:
            answer += roman_to_int_dict_single[string[index]]
            index += 1
    
    return answer
        
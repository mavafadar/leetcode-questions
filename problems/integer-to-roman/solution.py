def int_to_roman(number: int) -> str:
    """
    Converts an integer to a Roman numeral.

    :param number: An integer to be converted.
    :type number: inr
    :return: A string representing the Roman numeral equivalent of the given integer.
    :rtype: str
    """
    int_to_roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    
    answer = ''
    keys = list(int_to_roman_dict.keys())
    
    index = 0
    while index < len(keys):
        if number >= keys[index]:
            number -= keys[index]
            answer += int_to_roman_dict[keys[index]]
        else:
            index += 1
                
    return answer
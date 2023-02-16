def convert(string: str, rows_number: int) -> str:
    """
    Given a string `string` and an integer `rows_number`, returns the ZigZag conversion of the string.

    :param string: The input string to convert.
    :type string: str
    :param rows_number: The number of rows to be used in the ZigZag conversion.
    :type rows_number: int
    :return: The ZigZag converted string.
    :rtype: str
    """
    if rows_number == 1:
        return string
    rows = [list() for _ in range(rows_number)]
    flag, index, row_number = True, 0, 0
    while True:
        rows[row_number].append(string[index])
        index += 1
        if index == len(string):
            break
        row_number = row_number + 1 if flag == True else row_number - 1
        flag = flag if (row_number != 0 and row_number != rows_number - 1) else ~flag
    final_string = str()
    for this_list in rows:
        final_string += ''.join(this_list)
    return final_string
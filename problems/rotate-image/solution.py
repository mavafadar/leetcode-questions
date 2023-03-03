def rotate(matrix: list) -> None:
    """
    Rotates a square matrix in-place by 90 degrees clockwise.

    :param matrix: a list of lists representing a square matrix to be rotated
    :type matrix: list[list[int]]
    :return: None
    :rtype: None

    This function modifies the input matrix in-place, without returning a new matrix.
    It rotates the matrix by dividing it into four layers (starting from the outermost layer)
    and swapping the values of the four elements that form a cycle in each layer. The rotation
    is performed by iterating over the layers using two nested loops, and swapping the values
    of four elements in each cycle. The function has a time complexity of O(N^2) and a space
    complexity of O(1), where N is the size of the matrix.
    """
    for i in range(len(matrix) - 1):
        for j in range(i, len(matrix) - i - 1):
            i_one, j_one = i, j
            i_two, j_two = j_one, len(matrix) - i_one - 1
            i_three, j_three = j_two, len(matrix) - i_two - 1
            i_four, j_four = j_three, len(matrix) - i_three - 1
            matrix[i_one][j_one], matrix[i_two][j_two], matrix[i_three][j_three], matrix[i_four][j_four] =\
                matrix[i_four][j_four], matrix[i_one][j_one], matrix[i_two][j_two], matrix[i_three][j_three]
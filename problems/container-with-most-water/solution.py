def max_area(height: list) -> int:
    """
    Calculates the maximum area that can be contained by two vertical lines and the x-axis
    given a list of non-negative integers representing the heights of each point.

    :param height: A list of non-negative integers representing the heights of each point.
    :type height: list
    :return: The maximum area that can be contained by two vertical lines and the x-axis.
    :rtype: int
    """
    left, right = 0, len(height) - 1
    water = 0
    while left < right:
        this_water = (right - left) * min(height[right], height[left])
        water = this_water if this_water > water else water
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return water

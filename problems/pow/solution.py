def my_power(x: float, n: int) -> float:
    """
    Computes x raised to the power of n using a recursive algorithm.

    :param x: The base number to raise to the power.
    :type x: float
    :param n: The exponent to raise the base number to.
    :type n: int

    :return: The result of x raised to the power of n.
    :rtype: float
    """
    result = helper_power(x, abs(n))
    return result if n >= 0 else 1 / result

def helper_power(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    result = helper_power(x * x, n // 2)
    return result if n % 2 == 0 else result * x
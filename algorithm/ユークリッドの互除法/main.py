def get_greatest_common_divisor(a:int, b:int) -> int:
    """
    二つの数字の最大公約数を返す
    >>> get_greatest_common_divisor(1, 3)
    1
    >>> get_greatest_common_divisor(5, 1)
    1
    >>> get_greatest_common_divisor(4, 6)
    2
    >>> get_greatest_common_divisor(9, 6)
    3
    """
    if (a <= 0) or (b <= 0):
        raise ValueError("wrong value.")

    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    a, b = [int(x) for x in input("A, B: ").split(maxsplit=1)]
    print(get_greatest_common_divisor(a, b))

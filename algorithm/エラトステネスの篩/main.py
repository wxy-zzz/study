import math
from typing import List

def find_prime_numbers(limit: int) -> List[int]:
    """
    与えられた整数以下の全ての素数のリストを返す
    >>> find_prime_numbers(1)
    []
    >>> find_prime_numbers(2)
    [2]
    >>> find_prime_numbers(3)
    [2, 3]
    >>> find_prime_numbers(4)
    [2, 3]
    >>> find_prime_numbers(10)
    [2, 3, 5, 7]
    >>> find_prime_numbers(16)
    [2, 3, 5, 7, 11, 13]
    >>> find_prime_numbers(19)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if limit < 1:
        raise ValueError("wrong value.")

    a = [True] * (limit+1)
    limit_sqrt = int(math.sqrt(limit))
    prime_numbers = []

    for i in range(2, limit_sqrt+1):
        if a[i]:
            prime_numbers.append(i)
            for j in range(i * i, limit + 1, i):
                a[j] = False

    for i in range(limit_sqrt+1, limit+1):
        if a[i]:
            prime_numbers.append(i)

    return prime_numbers


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(find_prime_numbers(int(input("limit: ").strip())))

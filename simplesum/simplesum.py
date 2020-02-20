from typing import List, Union


def ssum(x: List) -> Union[int, float]:
    """
    Sum of array items

    Parameters
    ----------
    x : list
        Array

    Returns
    -------
    Union[int, float]
        Result of sum

    Examples
    -------
    >>> ssum([1, 2])
    3
    """

    return sum(x)

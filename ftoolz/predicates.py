from typing import Optional, TypeVar

A = TypeVar('A')


def some(a: Optional[A]) -> bool:
    """
    Check if given optional argument contains some value.

    >>> some('a')
    True
    >>> some(None)
    False
    """
    return a is not None


def none(a: Optional[A]) -> bool:
    """
    Check if given optional argument contains no value.

    >>> none(None)
    True
    >>> none('a')
    False
    """
    return a is None


def even(n: int) -> bool:
    """
    Check that given number is even.

    >>> [(n, even(n)) for n in range(5)]
    [(0, True), (1, False), (2, True), (3, False), (4, True)]
    """
    return n % 2 == 0


def odd(n: int) -> bool:
    """
    Check that given number is odd.

    >>> [(n, odd(n)) for n in range(5)]
    [(0, False), (1, True), (2, False), (3, True), (4, False)]
    """
    return n % 2 != 0


def vand(*args: A) -> bool:
    """
    Variadic `and` over given set of arguments.

    >>> vand()
    True
    >>> vand(True, True, True)
    True
    >>> vand(1, 1, 1)
    True
    >>> vand(True, False, True)
    False
    >>> vand(1, 0, 1)
    False
    """
    return all(bool(a) for a in args) if args else True


def vor(*args: A) -> bool:
    """
    Variadic `or` over given set of arguments.

    >>> vor()
    False
    >>> vor(False, False, False)
    False
    >>> vor(0, 0, 0)
    False
    >>> vor(False, False, True)
    True
    >>> vor(0, 0, 1)
    True
    """
    return any(bool(a) for a in args) if args else False

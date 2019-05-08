from string import whitespace


def cstrip(chars: str, s: str) -> str:
    """
    Strip `chars` from `s`.

    >>> cstrip(' ', '  test  ') == strip('  test  ')
    True
    >>> cstrip('xt', 'xxxtestxxx') == strip('xxxtestxxx', chars='xt')
    True

    It's same as `strip` but for better partial application and currying.

    >>> from functools import partial
    >>> strip_xt = partial(cstrip, 'xt')
    >>> strip_xt('xxxtestxxx') == strip('xxxtestxxx', chars='xt')
    True
    """
    return strip(s, chars)


def lower(s: str) -> str:
    """
    Make the string lowercase.

    >>> lower('TEST'), lower('TesT'), lower('test')
    ('test', 'test', 'test')
    """
    return s.lower()


def strip(s: str, chars: str = whitespace) -> str:
    """
    Classic strip method as function.

    >>> strip('  test  ')
    'test'
    >>> strip('xxxtestxxx', chars='xt')
    'es'
    """
    return s.strip(chars)


def upper(s: str) -> str:
    """
    Make the string uppercase.

    >>> upper('TEST'), upper('TesT'), upper('test')
    ('TEST', 'TEST', 'TEST')
    """
    return s.upper()

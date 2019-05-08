from string import whitespace


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

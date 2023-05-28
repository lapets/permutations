"""
Python library for instantiating and working with permutation collections
that provide efficient implementations of all sequence methods (including
random-access retrieval by index).
"""
from __future__ import annotations
from typing import Iterable
import doctest
import collections.abc
import operator
import functools

class permutations:
    """
    Sequence of all permutations of a specific collection of elements.

    >>> len(permutations(range(3)))
    6

    An optional length parameter ``r`` can be supplied to restrict the output
    to only permutations of ``r`` elements.

    >>> len(permutations(range(3), 2))
    6

    An exception is raised when arguments are not of a correct type or
    our outside the supported range.

    >>> permutations(123)
    Traceback (most recent call last):
      ...
    TypeError: object is not iterable
    >>> permutations(range(3), 'abc')
    Traceback (most recent call last):
      ...
    TypeError: Expected int as r
    >>> permutations(range(3), -2)
    Traceback (most recent call last):
      ...
    ValueError: r must be non-negative
    """
    def __init__(self: permutations, iterable: Iterable, r: int = None):
        """
        Instantiate an instance for an iterable of elements and an optional
        permutation length.
        """
        if not isinstance(iterable, collections.abc.Iterable):
            raise TypeError('object is not iterable')

        self._iterable = tuple(iterable)
        self._n = len(self._iterable)

        if r is not None:
            if not isinstance(r, int):
                raise TypeError('Expected int as r')

            if r < 0:
                raise ValueError('r must be non-negative')

        self._r = self._n if r is None else r
        self._length = functools.reduce(
            operator.mul,
            range(self._n, self._n - self._r, -1),
            1
        )

    def __len__(self: permutations) -> int:
        """
        Return the number of distinct permutations in the collection
        represented by this instance.

        >>> len(permutations(range(8))) == 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        True
        """
        return self._length

if __name__ == '__main__':
    doctest.testmod() # pragma: no cover

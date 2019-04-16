from random import Random as _Random
from typing import Any, Callable, Dict, Iterable, Iterator, List, Sequence, \
    Tuple, TypeVar, Union, overload

_K = TypeVar('_K')
_V = TypeVar('_V')
# noinspection PyShadowingBuiltins
_T = TypeVar('_T')
# noinspection PyShadowingBuiltins
_T_co = TypeVar('_T_co', covariant=True)
# noinspection PyShadowingBuiltins
_T1 = TypeVar('_T1')
# noinspection PyShadowingBuiltins
_T2 = TypeVar('_T2')
no_default: str
no_pad: str


def concat(seqs: Iterable[Iterable[_T]]) -> Iterable[_T]: ...


def concatv(*seqs: Iterable[_T]) -> Iterable[_T]: ...


def cons(el: _T, seq: Iterable[_T]) -> Iterator[_T]: ...


def count(seq: Iterable) -> int: ...


@overload
def diff(*seqs: Sequence[_T]) -> Iterable[Tuple[_T, ...]]: ...


@overload
def diff(
        *seqs: Sequence[_T],
        key: Callable[[_T], _T1],
) -> Iterable[Tuple[_T1, ...]]: ...


@overload
def diff(
        *seqs: Sequence[_T],
        default: _T2,
) -> Iterable[Tuple[Union[_T, _T2], ...]]: ...


@overload
def diff(
        *seqs: Sequence[_T],
        key: Callable[[_T], _T1],
        default: _T2,
) -> Iterable[Tuple[Union[_T1, _T2], ...]]: ...


def drop(n: int, seq: Iterable[_T]) -> Iterable[_T]: ...


def first(seq: Iterable[_T]) -> _T: ...


def frequencies(seq: Iterable[_T]) -> Dict[_T, int]: ...


@overload
def get(ind: int, seq: Iterable[_T]) -> _T: ...


@overload
def get(
        ind: int,
        seq: Iterable[_T],
        default: Union[_T1, str] = no_default,
) -> Union[_T, _T1]: ...


# TODO
def getter(index: Any) -> Any: ...


@overload
def groupby(
        key: _K,
        seq: Iterable[Dict[_K, _V]],
) -> Dict[_K, List[Dict[_K, _V]]]: ...


@overload
def groupby(key: Callable[[_T], _T1], seq: Iterable[_T]) -> Dict[_T1, List[_T]]: ...


def identity(x: _T) -> _T: ...


def isdistinct(seq: Iterable) -> bool: ...


def isiterable(x: Any) -> bool: ...


# TODO
def join(leftkey: Any, leftseq: Any, rightkey: Any, rightseq: Any,
         left_default: Any = no_default,
         right_default: Any = no_default) -> Any: ...


def last(seq: Iterable[_T]) -> _T: ...


def mapcat(func: Callable[[_T_co], Iterable[_T1]],
           seqs: Iterable[_T_co]) -> Iterable[_T1]: ...


# TODO replace kwargs with key
def merge_sorted(*seqs: Iterable[_T], **kwargs: Any) -> Iterable[_T]: ...


def nth(n: int, seq: Iterable[_T]) -> _T: ...


@overload
def partition(n: int, seq: Iterable[_T]) -> Iterable[Tuple[_T, ...]]: ...


@overload
def partition(
        n: int,
        seq: Iterable[_T],
        pad: _T1,
) -> Iterable[Tuple[Union[_T, _T1], ...]]: ...


def partition_all(n: int, seq: Iterable[_T]) -> Iterable[Tuple[_T, ...]]: ...


def peek(seq: Iterable[_T]) -> Tuple[_T, Iterable[_T]]: ...


@overload
def pluck(
        ind: Union[int, List[int], str, List[str]],
        seqs: Union[List[_T], Dict[Union[str, int], _T]],
) -> Iterable[Tuple[_T, ...]]: ...


@overload
def pluck(
        ind: Union[int, List[int], str, List[str]],
        seqs: Union[List[_T], Dict[Union[str, int], _T]],
        default: Union[_T1, str] = no_default,
) -> Iterable[Tuple[Union[_T, _T1], ...]]: ...


@overload
def reduceby(
        key: Callable[[_T], _T1],
        binop: Callable[[_T, _T], _T],
        seq: Iterable[_T],
) -> Dict[_T1, _T]: ...


# Causes error in mypy by conflicting with first overload
# @overload
# def reduceby(
#         key: _K,
#         binop: Callable[[Dict[_K, _V], Dict[_K, _V]], Dict[_K, _V]],
#         seq: Dict[_K, _V],
# ) -> Dict[_V, Dict[_K, _V]]: ...


@overload
def reduceby(
        key: _K,
        binop: Callable[[_T, Dict[_K, _V]], _T],
        seq: Dict[_K, _V],
        init: Union[Callable[[], _T], _T],
) -> Dict[_V, _T]: ...


@overload
def reduceby(
        key: Callable[[_T], _T1],
        binop: Callable[[_T2, _T], _T2],
        seq: Iterable[_T],
        init: Union[Callable[[], _T2], _T2],
) -> Dict[_T1, _T2]: ...


# uncomment if necessary
# @overload
# def reduceby(key: Any, binop: Any, seq: Any, init: Any = no_default) ->
# Any: ...


# TODO - no documentation
def rest(seq: Any) -> Any: ...


def second(seq: Iterable[_T]) -> _T: ...


def tail(n: int, seq: Iterable[_T]) -> Iterable[_T]: ...


def take(n: int, seq: Iterable[_T]) -> Iterable[_T]: ...


def take_nth(n: int, seq: Iterable[_T]) -> Iterable[_T]: ...


def topk(k: int, seq: Iterable[_T], key: Any = None) -> Iterable[_T]: ...


def unique(seq: Iterable[_T], key: Any = None) -> Iterable[_T]: ...


####################################################################
# TBD
####################################################################

def heapify(*args: Any, **kwargs: Any) -> Any: ...


def heappop(*args: Any, **kwargs: Any) -> Any: ...


def heapreplace(heap: Any, item: Any) -> Any: ...


class Random(_Random):
    __init__: Any = ...
    VERSION: Any = ...
    _randbelow: Any = ...
    betavariate: Any = ...
    choice: Any = ...
    choices: Any = ...
    expovariate: Any = ...
    gammavariate: Any = ...
    gauss: Any = ...
    getstate: Any = ...
    lognormvariate: Any = ...
    normalvariate: Any = ...
    paretovariate: Any = ...
    randint: Any = ...
    randrange: Any = ...
    sample: Any = ...
    seed: Any = ...
    setstate: Any = ...
    shuffle: Any = ...
    triangular: Any = ...
    uniform: Any = ...
    vonmisesvariate: Any = ...
    weibullvariate: Any = ...
    __getstate__: Any = ...
    __reduce__: Any = ...
    __setstate__: Any = ...


class accumulate:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class chain:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    @classmethod
    def from_iterable(cls, *args: Any, **kwargs: Any) -> Any: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class deque:
    maxlen: Any = ...
    __hash__: Any = ...

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def append(self, *args: Any, **kwargs: Any) -> Any: ...

    def appendleft(self, *args: Any, **kwargs: Any) -> Any: ...

    def clear(self, *args: Any, **kwargs: Any) -> Any: ...

    def copy(self, *args: Any, **kwargs: Any) -> Any: ...

    def count(self, *args: Any, **kwargs: Any) -> Any: ...

    def extend(self, *args: Any, **kwargs: Any) -> Any: ...

    def extendleft(self, *args: Any, **kwargs: Any) -> Any: ...

    def index(self, *args: Any, **kwargs: Any) -> Any: ...

    def insert(self, *args: Any, **kwargs: Any) -> Any: ...

    def pop(self, *args: Any, **kwargs: Any) -> Any: ...

    def popleft(self, *args: Any, **kwargs: Any) -> Any: ...

    def remove(self, *args: Any, **kwargs: Any) -> Any: ...

    def reverse(self, *args: Any, **kwargs: Any) -> Any: ...

    def rotate(self, *args: Any, **kwargs: Any) -> Any: ...

    def __add__(self, other: Any) -> Any: ...

    def __bool__(self) -> Any: ...

    def __contains__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __copy__(self) -> Any: ...

    def __delitem__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __eq__(self, other: Any) -> Any: ...

    def __ge__(self, other: Any) -> Any: ...

    def __getitem__(self, index: Any) -> Any: ...

    def __gt__(self, other: Any) -> Any: ...

    def __iadd__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __imul__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __iter__(self) -> Iterator: ...

    def __le__(self, other: Any) -> Any: ...

    def __len__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __lt__(self, other: Any) -> Any: ...

    def __mul__(self, other: Any) -> Any: ...

    def __ne__(self, other: Any) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __reversed__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __rmul__(self, other: Any) -> Any: ...

    def __setitem__(self, index: Any, object: Any) -> Any: ...

    def __sizeof__(self) -> Any: ...


class interleave:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class interpose:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class islice:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class itemgetter:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

    def __reduce__(self) -> Any: ...


class iterate:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class map:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...


class random_sample:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class remove:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class sliding_window:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...


class zip:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...


class zip_longest:

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __iter__(self) -> Iterator: ...

    def __next__(self) -> Any: ...

    def __reduce__(self) -> Any: ...

    def __setstate__(self, state: Any) -> Any: ...
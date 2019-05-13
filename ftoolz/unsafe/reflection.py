from typing import List, Set, Type, TypeVar

T = TypeVar('T')


def abstract(clz: Type) -> bool:
    """
    Predicate that returns `True` iff given class has abstract methods.

    >>> from abc import ABC, abstractmethod

    >>> class A(ABC):
    ...     @abstractmethod
    ...     def test(self) -> None:
    ...         pass
    >>> abstract(A)
    True

    >>> class B(A):
    ...     def test(self) -> None:
    ...         pass
    >>> abstract(B)
    False

    >>> class C(ABC):
    ...     pass
    >>> abstract(C)
    False

    >>> class D(A):
    ...     pass
    >>> abstract(D)
    True
    """
    return bool(getattr(clz, "__abstractmethods__", False))


def implementations(clz: Type[T], package: str) -> List[Type[T]]:
    """
    Inspect given `package` and find all *implementations* of given class.
    An implementation is a (not necessarily direct) subclass which has
    no abstract methods.

    Optionally, class can define `__protected__ = True` which will make this
    function omit such class from the result set.

    **Warning**: Class discovery uses `import_all` so any side-effect of any
    import under the package will be executed as a side-effect of this function

    >>> from abc import ABC, abstractmethod

    >>> class A(ABC):
    ...     @abstractmethod
    ...     def test(self) -> None:
    ...         pass
    ...     @abstractmethod
    ...     def test2(self) -> None:
    ...         pass

    >>> class B(A, ABC):
    ...     def test(self) -> None:
    ...         pass
    >>> class C(B):
    ...     def test2(self) -> None:
    ...         pass
    >>> class D(C):
    ...     def test2(self) -> None:
    ...         pass

    >>> class E(A):
    ...     def test(self) -> None:
    ...         pass
    ...     def test2(self) -> None:
    ...         pass
    >>> class F(E):
    ...     __protected__ = True

    >>> [c.__name__ for c in implementations(A, __package__)]
    ['C', 'D', 'E']
    >>> [c.__name__ for c in implementations(B, __package__)]
    ['C', 'D']
    >>> [c.__name__ for c in implementations(E, __package__)]
    []
    """
    instances = (
        c for c in subclasses(clz, package)
        if not abstract(c) and not protected(c)
    )
    return sorted(instances, key=lambda c: c.__name__)


def import_all(package: str) -> None:
    """
    Recursively import every module reachable from given `package`.

    **Warning**: Any side-effect of any import under the package will be
    executed as a side-effect of this function.
    """
    import pkgutil
    import sys
    pkg = sys.modules[package]
    path = pkg.__path__  # type: ignore
    for loader, module_name, _ in pkgutil.walk_packages(path):
        loader.find_module(module_name).load_module(module_name)


def protected(clz: Type[T]) -> bool:
    """
    Predicate that is `True` iff given class has attribute `__protected__` set
    and has value `True`.

    >>> class A:
    ...     pass
    >>> protected(A)
    False

    >>> class B:
    ...     __protected__ = True
    >>> protected(B)
    True

    >>> class C:
    ...     __protected__ = False
    >>> protected(C)
    False
    """
    return bool(getattr(clz, '__protected__', False))


def subclasses(clz: Type[T], package: str) -> Set[Type[T]]:
    """
    Inspect given `package` and look up all subclasses of given class.

    **Warning**: Class discovery uses `import_all` so any side-effect of any
    import under the package will be executed as a side-effect of this function

    >>> from abc import ABC, abstractmethod
    >>> class A(ABC):
    ...     @abstractmethod
    ...     def test(self) -> None:
    ...         pass
    >>> class B(A):
    ...     def test(self) -> None:
    ...         pass
    >>> class C(B):
    ...     def test(self) -> None:
    ...         pass
    >>> class D(C):
    ...     def test(self) -> None:
    ...         pass
    >>> class E(A):
    ...     def test(self) -> None:
    ...         pass

    >>> sorted(c.__name__ for c in subclasses(A, __package__))
    ['B', 'C', 'D', 'E']
    >>> sorted(c.__name__ for c in subclasses(B, __package__))
    ['C', 'D']
    >>> sorted(c.__name__ for c in subclasses(D, __package__))
    []
    """

    def rec(cls: Type[T]) -> Set[Type[T]]:
        sub = set(cls.__subclasses__())
        return sub.union(s for c in sub for s in rec(c))

    import_all(package)
    return rec(clz)

"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""


from typing import Callable, TypeVar, ParamSpec
from typing import Concatenate  

T = TypeVar("T")
P = ParamSpec("P")

def decorator(func: Callable[P, T]) -> Callable[P, T]:
    return func

#!/usr/bin/env python3

"""Complex types - string and int/float to tuple"""

from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return sum of floats"""

    def multiplier_func(value: float) -> float:
        """multiiply mulitplier by value"""
        return value * multiplier

    return multiplier_func

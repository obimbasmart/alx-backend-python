#!/usr/bin/env python3

"""Basic annotations - Complex types - mixed list"""

from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """return sum of floats"""
    return sum(mxd_lst)

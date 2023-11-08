#!/usr/bin/env python3
"""
This project module contains a function that
takes two integer arguments and returns a tuple.
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple:
    """
    Function that takes two integer arguments and
    returns a tuple.
    Returns:
        A tuple of size two containing a start index
        and an end index corresponding to the range
        of indexes to return in a list for those
        particular pagination parameters.
    """
    tuple1 = ()
    tuple2 = ()
    end_index = page * page_size
    tuple2 += (end_index, )
    start_index = end_index - page_size
    tuple1 += (start_index, )

    return tuple1 + tuple2

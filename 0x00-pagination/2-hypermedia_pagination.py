#!/usr/bin/env python3
"""
This project module contains a class and a function that
takes two integer arguments and returns a dictionary.
"""
import csv
import math
from typing import Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method that takes two integer arguments and returns a list
        with the information from the dataset, organized by the
        page number and the page size given.
        Returns:
            A list with data according to the page number and the
            page size.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        tupl = index_range(page, page_size)
        start_index = int(tupl[0])
        end_index = int(tupl[1])
        result = Server.dataset(self)
        length_list = len(result)
        if page * page_size > length_list:
            return []

        return result[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Method that takes two integer arguments and returns a
        dictionary containing several key-value pairs.
        Returns:
            A dictionary with the following key-value pairs: page_size,
            page, data, next_page, prev_page and total_pages.

        """
        dic_result = {}
        result = Server.dataset(self)
        length_list = len(result)

        if page * page_size > length_list:
            dic_result['page_size'] = 0
        else:
            dic_result['page_size'] = page_size

        dic_result['page'] = page
        data = Server.get_page(self, page, page_size)
        dic_result['data'] = data

        if page * page_size > length_list:
            dic_result['next_page'] = None
        else:
            dic_result['next_page'] = page + 1

        if page == 1:
            dic_result['prev_page'] = None
        else:
            dic_result['prev_page'] = page - 1

        total_pages = length_list / page_size
        dic_result['total_pages'] = math.ceil(total_pages)

        return dic_result


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

#!/usr/bin/env python3
"""_summary_
"""
import csv
import math import ceil
from typing import List, Any, Dict


def index_range(page: int, page_size: int):
    """_summary_

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        _type_: _description_
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict[str, Any]: _description_
        """

        length_data = len(self.__dataset)
        total_pages = ceil(length_data / page_size)

        data = self.get_page(page, page_size)
        if not data:
            page_size = 0
        else:
            page_size = len(data)
        if page < total_pages:
            next_page = page + 1
        else:
            None
        if page > 1:
            prev_page = page - 1
        else:
            None
        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }

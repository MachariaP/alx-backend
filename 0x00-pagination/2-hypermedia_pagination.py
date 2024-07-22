#!/usr/bin/env python3
"""Task 3 Module"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index

    :param page: The page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """Retrieves a page of data resource.
        """
        assert isinstance(page, int) and \
            page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and \
            page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retrieves hyper data for the given page."""
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_data = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_data

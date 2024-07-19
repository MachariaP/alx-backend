#!/usr/bin/env python3
"""
Module takes two integer arguments: page and page_size.
Calculates and returns a tuple containing the start
and end index for a slice of items.
Page numbers are 1-indexed(first page is page 1.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for pagination.

    Parameters:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []  # Return an empty list if out of range
        return dataset[start_index:end_index]

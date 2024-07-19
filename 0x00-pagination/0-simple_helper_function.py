#!/usr/bin/env python3
"""
Module takes two integer arguments: page and page_size.
Calculates and returns a tuple containing the start
and end index for a slice of items.
Page numbers are 1-indexed(first page is page 1.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end index for pagination.

    Parameters:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

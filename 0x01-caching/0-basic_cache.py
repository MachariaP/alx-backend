#!/usr/bin/env python3
""" Basic dictionary module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a
        caching system without limit.
    """
    def put(self, key, item):
        """ Assigns item value for the key in self.cache_data dictionary.
            Does nothing if key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to key in self.cache_data.
            Returns None if key is None or key doesn't exist.
        """
        return self.cache_data.get(key, None)

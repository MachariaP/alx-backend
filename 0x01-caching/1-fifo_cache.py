#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
        that discards the least recently added item.
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Assigns item value for the key in self.cache_data dictionary.
            Discards the first item added if the cache exceeds its limit.
            Does nothing if key or item is None.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keys.append(self.keys.pop(self.keys.index(key)))
            else:
                self.cache_data[key] = item
                self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.keys.pop(0)
                del self.cache_data[discarded]
                print("DISCARD:", discarded)

    def get(self, key):
        """ Returns the value linked to key in self.cache_data.
            Returns None if key is None or key doesn't
        """
        return self.cache_data.get(key, None)

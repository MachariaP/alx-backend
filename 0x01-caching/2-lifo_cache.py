#!/usr/bin/env python3
""" LIFO Caching module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is caching system
        that discards the most recently added item.
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key_added = None

    def put(self, key, item):
        """ Assigns item value for the key in self.cache_data dictionary.
            Discard the most recently added item if the cache
            exceeds its limit.
            Does nothing if key or item is None.
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                print("DISCARD:", self.last_key_added)
                del self.cache_data[self.last_key_added]
            self.cache_data[key] = item
            self.last_key_added = key

    def get(self, key):
        """ Returns the value linked to key in self.cache_data.
            Returns None if key is None or key doesn't exist
        """
        return self.cache_data.get(key, None)

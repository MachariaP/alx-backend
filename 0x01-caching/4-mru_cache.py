#!/usr/bin/env python3
""" MRU Caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system that
        discards the most recently used item.
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_tracker = []

    def put(self, key, item):
        """ Assigns item value for the key in self.cache_data dictionary.
            Discard the most recently used item if the cache exceeds its limit.
            Does nothing if key or item is None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_tracker:
                self.key_tracker.remove(key)
            self.key_tracker.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # The most recently used item is the last item in key_tracker
                # -1 is the current key, so -2 is the MRU before it
                mru_key = self.key_tracker[-2]
                print("DISCARD:", mru_key)
                self.cache_data.pop(mru_key)
                self.key_tracker.remove(mru_key)

    def get(self, key):
        """ Returns the value linked to key in self.cache_data.
            If key is None or if key doesn't exist in self.cache_data,
            return None.
        """
        if key is not None and key in self.cache_data:
            if key in self.key_tracker:
                self.key_tracker.remove(key)
            self.key_tracker.append(key)
            return self.cache_data[key]
        return None

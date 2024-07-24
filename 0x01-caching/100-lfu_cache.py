#!/usr/bin/env python3
""" LFU Caching module
"""
from base_caching import BaseCaching
from time import time


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
        and implements LFU caching
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.usage_counts = {}  # Frequency of access
        self.usage_order = {}  # Timestamp of last access

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.usage_counts[key] = self.usage_counts.get(key, 0) + 1
        self.usage_order[key] = self._current_time()

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the least frequently used keys
            min_freq = min(self.usage_counts.values())
            lfu_keys = [k for k,
                        v in self.usage_counts.items() if v == min_freq]

            # Find the least recently used key among them
            lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
            del self.cache_data[lru_key]
            del self.usage_counts[lru_key]
            del self.usage_order[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_counts[key] += 1
        self.usage_order[key] = self._current_time()
        return self.cache_data[key]

    def _current_time(self):
        """ Return the current time in milliseconds for ordering
        """
        return int(time() * 1000)

#!/usr/bin/env python3
""" LFU Caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements a caching system
        using LFU and LRU algorithms.
    """
    def __init__(self):
        """ Initialize LFUCache.
        """
        super().__init__()
        self.usage_counts = {}  # Frequency of access
        self.lru_tracker = {}  # Order of access
        self.operation_counter = 0  # Order of operations

    def put(self, key, item):
        """ Add or update a key-value pair. Discard the least
            frequently used item if necessary.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.usage_counts[key] = self.usage_counts.get(key, 0) + 1
        self.operation_counter += 1
        self.lru_tracker[key] = self.operation_counter

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used = min(self.usage_counts.items(),
                             key=lambda x: (x[1], self.lru_tracker[x[0]]))
            del self.cache_data[least_used[0]]
            del self.usage_counts[least_used[0]]
            del self.lru_tracker[least_used[0]]
            print("DISCARD:", least_used[0])

    def get(self, key):
        """ Return the value of the key if it exists, None otherwise.
            Increment access count.
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_counts[key] += 1
        self.operation_counter += 1
        self.lru_tracker[key] = self.operation_counter
        return self.cache_data[key]

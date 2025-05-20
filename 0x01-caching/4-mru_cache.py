#!/usr/bin/env python3
"""
MRU caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching and is a caching system
    with Most Recently Used replacement policy.
    """

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using MRU replacement policy.

        Args:
            key: The key to store the item under
            item: The item to store
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.order.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key and update its position in the order.

        Args:
            key: The key to retrieve the item for

        Returns:
            The item stored under the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key) 
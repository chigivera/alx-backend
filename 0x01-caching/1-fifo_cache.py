#!/usr/bin/env python3
"""
FIFO caching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching and is a caching system
    with FIFO replacement policy.
    """

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO replacement policy.

        Args:
            key: The key to store the item under
            item: The item to store
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key.

        Args:
            key: The key to retrieve the item for

        Returns:
            The item stored under the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key) 
#!/usr/bin/env python3
"""
Basic caching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching and is a caching system
    without limit.
    """

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key to store the item under
            item: The item to store
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
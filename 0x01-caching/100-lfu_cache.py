#!/usr/bin/env python3
"""
LFU caching module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching and is a caching system
    with Least Frequently Used replacement policy.
    """

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using LFU replacement policy.

        Args:
            key: The key to store the item under
            item: The item to store
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                lfu_items = [k for k, v in self.frequency.items() if v == min_freq]
                
                # If multiple items have the same frequency, use LRU
                if len(lfu_items) > 1:
                    for k in self.order:
                        if k in lfu_items:
                            discard = k
                            break
                else:
                    discard = lfu_items[0]
                
                del self.cache_data[discard]
                del self.frequency[discard]
                self.order.remove(discard)
                print("DISCARD: {}".format(discard))
            
            self.cache_data[key] = item
            self.order.append(key)
            self.frequency[key] += 1

    def get(self, key):
        """Get an item by key and update its frequency.

        Args:
            key: The key to retrieve the item for

        Returns:
            The item stored under the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        self.frequency[key] += 1
        return self.cache_data.get(key) 
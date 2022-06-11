#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.previous = ''

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.previous))
                self.cache_data.pop(self.previous)
            self.previous = key

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key in self.cache_data:
            return self.cache_data[key]
        if key is None or self.cache_data.get(key) is None:
            return None

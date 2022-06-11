#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.data = {}
        self.new = 0
        self.previous = 0

    def _pop(self):
        """_summary_
        """
        self.previous = self.previous + 1
        key = self.data[self.previous]
        del self.data[self.previous]
        del self.cache_data[key]

    def _push(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.previous + 1]))
            self._pop()
        self.cache_data[key] = item
        self.new = self.new + 1
        self.data[self.new] = key

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key in self.cache_data:
            result = self.cache_data[key]
            return result
        if key is None or self.cache_data.get(key) is None:
            return None

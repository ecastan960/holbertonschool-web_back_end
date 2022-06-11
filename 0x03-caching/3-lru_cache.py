#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.head = '-'
        self.tail = '='
        self.next = {}
        self.prev = {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """_summary_

        Args:
            head (_type_): _description_
            tail (_type_): _description_
        """
        self.next[head] = tail
        self.prev[tail] = head

    def _remove(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
        if key is None or self.cache_data.get(key) is None:
            return None

#!/usr/bin/python3
"""_summary_

Returns:
    _type_: _description_
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        count = self.counter.get(key, None)
        if count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            temp = self.first_list(self.queue)
            if temp:
                self.queue.pop(0)
                del self.counter[temp]
                del self.cache_data[temp]
                print("DISCARD: {}".format(temp))
        if key not in self.queue:
            self.queue.insert(0, key)
        self.last_list(key)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        info = self.cache_data.get(key, None)
        if info is not None:
            self.counter[key] += 1
            self.last_list(key)
        return info

    def last_list(self, item):
        """_summary_

        Args:
            item (_type_): _description_
        """
        length = len(self.queue)
        index = self.queue.index(item)
        count = self.counter[item]
        for i in range(index, length):
            if i != (length - 1):
                temp = self.queue[i + 1]
                j = self.counter[temp]
                if j > count:
                    break
        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def first_list(array):
        """_summary_

        Args:
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
        if (array):
            return array[0]
        else:
            return None

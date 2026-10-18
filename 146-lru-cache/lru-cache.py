from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None"""
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return
        if len(self.cache) >= self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value
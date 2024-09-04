#!/usr/bin/python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary """

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

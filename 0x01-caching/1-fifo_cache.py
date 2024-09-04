#!/usr/bin/python3
""" FIFO caching"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """

    def __init__(self):
        """ Override superclass __init__ """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                discard = list(self.cache_data.keys())[0]
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))

            if key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key:
            return self.cache_data.get(key)

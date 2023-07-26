#!/usr/bin/python3
""" LIFOCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliazes
        """
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache
        """
        dict_data = self.cache_data
        if not (key is None or item is None):
            if (len(dict_data) == BaseCaching.MAX_ITEMS and
                    key not in dict_data):
                last = sorted(dict_data.keys())[-1]
                print("DISCARD: {}".format(last))
                del dict_data[last]
                dict_data[key] = item
            else:
                dict_data[key] = item

    def get(self, key):
        """ Gets an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]

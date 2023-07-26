#!/usr/bin/python3
""" BasicCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if not (key is None or item is None):
            dict_data = self.cache_data
            dict_data[key] = item

    def get(self, key):
        """ Gets an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]

#!/usr/bin/python3
""" FIFOCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching.
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
            if(
                len(dict_data) == BaseCaching.MAX_ITEMS and
                key not in dict_data
            ):
                fi = sorted(dict_data.keys())[0]
                print("DISCARD: {}".format(fi))
                del dict_data[fi]
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

#!/usr/bin/python3
""" LRUCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache - a caching system that inherits from BaseCaching..
    """

    def __init__(self):
        """ Initiliazes
        """
        super().__init__()
        self.ordered_cache_keys = []

    def put(self, key, item):
        """ Adds an item in the cache
        """
        dict_data = self.cache_data
        if not (key is None or item is None):
            if (len(dict_data) == BaseCaching.MAX_ITEMS and
                    key not in dict_data):
                mru = self.ordered_cache_keys[-1]
                print('DISCARD: {}'.format(mru))
                self.ordered_cache_keys.remove(mru)
                self.ordered_cache_keys.append(key)
                del dict_data[mru]
                dict_data[key] = item
            elif (len(dict_data) == BaseCaching.MAX_ITEMS and
                    key in dict_data):
                self.ordered_cache_keys.remove(key)
                self.ordered_cache_keys.append(key)
                dict_data[key] = item
            else:
                self.ordered_cache_keys.append(key)
                dict_data[key] = item

    def get(self, key):
        """ Gets an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        self.ordered_cache_keys.remove(key)
        self.ordered_cache_keys.append(key)
        return dict_data[key]

#!/usr/bin/env python3
"""0-module
"""


import redis
import uuid
from typing import Union


class Cache:
    """A class for caching data using Redis."""

    def __init__(self):
        """
        Initialize a Cache instance.

        This method initializes a Redis client and flushes the database.

        Args:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache and return the associated key.

        This method generates a random key using uuid, stores the input data in
        Redis using the generated key, and returns the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in
            the cache.

        Returns:
            str: The randomly generated key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

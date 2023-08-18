#!/usr/bin/env python3
"""web.py"""


from typing import Callable
import requests
import redis
from functools import wraps


redis_store = redis.Redis()
"""Redis instance"""


def cach_data(method: Callable) -> Callable:
    """
    caches the fetched data
    """
    @wraps(method)
    def invoker(url) -> str:
        """The wrapper function"""
        redis_store.incr(f"count:{url}")
        result = redis_store.get(f"result:{url}")
        if result:
            return result.decode("utf-8")
        result = method(url)
        redis_store.set(f"count:{url}", 0)
        redis_store.setex(f"result:{url}", 10, result)
        return result
    return invoker


@cach_data
def get_page(url: str) -> str:
    """Return the content of a URL after ahing the request response"""
    return requests.get(url).text

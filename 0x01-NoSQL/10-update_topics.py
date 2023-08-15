#!/usr/bin/env python3
"""10-update_topics"""


def update_topics(mongo_collections, name, topics):
    """update many"""
    result = mongo_collections.update_many({"name": name}, {"$set": {"topics":
                                                                     topics}})
    return result.modified_count

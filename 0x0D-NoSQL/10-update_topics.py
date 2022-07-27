#!/usr/bin/env python3
"""_summary_
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """_summary_
    """
    return mongo_collection.update_many({"name":name},{"$set":{"topics":topics}})
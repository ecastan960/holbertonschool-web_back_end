#!/usr/bin/env python3
"""_summary_
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """_summary_
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})

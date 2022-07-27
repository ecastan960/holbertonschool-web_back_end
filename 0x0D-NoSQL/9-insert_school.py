#!/usr/bin/env python3
"""_summary_
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """_summary_
    """
    return mongo_collection.insert_one(kwargs).inserted_id 

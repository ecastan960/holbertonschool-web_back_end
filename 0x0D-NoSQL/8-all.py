#!/usr/bin/env python3
"""_summary_
"""
import pymongo


def list_all(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_

    Returns:
        _type_: _description_
    """
    return [doc for doc in mongo_collection.find()] if mongo_collection else []

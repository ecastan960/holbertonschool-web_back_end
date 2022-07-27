#!/usr/bin/env python3
"""_summary_
"""
from pymongo import MongoClient


def logger(a: dict) -> int:
    """_summary_
    """
    return MongoClient('mongodb://127.0.0.1:27017').logs.nginx.count_documents(a)


def main():
    """_summary_
    """
    info = [f"{ logger({}) } logs", "Methods:",
            f"\tmethod GET: { logger({'method': 'GET'}) }",
            f"\tmethod POST: { logger({'method': 'POST'}) }",
            f"\tmethod PUT: {logger({'method': 'PUT'})}",
            f"\tmethod PATCH: {logger({'method': 'PATCH'})}",
            f"\tmethod DELETE: {logger({'method': 'DELETE'})}",
            f"{logger({'method': 'GET', 'path': '/status'})} status check"]

    for i in info:
        print(i)


if __name__ == "__main__":
    main()

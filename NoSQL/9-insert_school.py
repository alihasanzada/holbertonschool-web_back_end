#!/usr/bin/env python3
"""Module that inserts a new document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection based on kwargs.

    Returns the _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id

#!/usr/bin/env python3
"""Module that changes all topics of a school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of all documents matching the given name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

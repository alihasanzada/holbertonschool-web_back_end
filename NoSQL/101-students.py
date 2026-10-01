#!/usr/bin/env python3
"""Module that returns all students sorted by average score."""


def top_students(mongo_collection):
    """Return all students sorted by average score (descending).

    The average score is included in each item with key averageScore.
    """
    return list(mongo_collection.aggregate([
        {"$project": {
            "name": 1,
            "topics": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]))

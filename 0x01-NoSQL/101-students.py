#!/usr/bin/env python3
"""101-students.py module"""


def top_students(mongo_collection):
    """Rreturns all students sorted by average score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_student

#!/usr/bin/env python3
"""11-schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of dictionaries, each representing a school document
        with the specified topic.
    """
    schools = []

    # Find schools with the specified topic
    for school in mongo_collection.find({"topics": topic}):
        schools.append(school)

    return schools

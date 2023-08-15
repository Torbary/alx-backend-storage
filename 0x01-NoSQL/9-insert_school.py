#!/usr/bin/env python3
"""9-insert_school"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object.
        **kwargs: Keyword arguments representing the attributes
        of the new document.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    # Insert the document into the collection
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)

    # Return the _id of the newly inserted document
    return result.inserted_id

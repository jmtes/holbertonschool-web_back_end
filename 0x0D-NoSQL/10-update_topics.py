#!/usr/bin/env python3
''' Update documents in a collection. '''


def update_topics(mongo_collection, name, topics):
    ''' Update documents in given collection. '''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

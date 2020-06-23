#!/usr/bin/env python3
''' Find documents in a collection. '''


def schools_by_topic(mongo_collection, topic):
    ''' Return list of schools that teach given topic. '''
    res = mongo_collection.find(
        {"topics": {"$in": [topic]}}
    )
    return [item for item in res]

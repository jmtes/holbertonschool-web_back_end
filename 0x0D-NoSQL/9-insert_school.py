#!/usr/bin/env python3
''' Insert document into collection. '''


def insert_school(mongo_collection, **kwargs):
    ''' Insert document into given collection. '''
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id

#!/usr/bin/env python3
''' Provide stats about Nginx logs stored in MongoDB. '''

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['logs']
col = db['nginx']

log_count = col.count_documents({})

get_count = col.count_documents({"method": "GET"})
post_count = col.count_documents({"method": "POST"})
put_count = col.count_documents({"method": "PUT"})
patch_count = col.count_documents({"method": "PATCH"})
delete_count = col.count_documents({"method": "DELETE"})

status_count = col.count_documents(
    {"method": "GET",
     "path": "/status"}
)

print('{:d} logs'.format(log_count))
print('Methods:')
print('\tmethod GET: {:d}'.format(get_count))
print('\tmethod POST: {:d}'.format(post_count))
print('\tmethod PUT: {:d}'.format(put_count))
print('\tmethod PATCH: {:d}'.format(patch_count))
print('\tmethod DELETE: {:d}'.format(delete_count))
print('{:d} status check'.format(status_count))

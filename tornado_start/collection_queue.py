#!/usr/bin/env python
# fileencoding=utf-8

from operator import itemgetter


class CollectionQueue(object):

    def __init__(self, db, name):
        self.col = db[name]

    def enqueue(self, key, value, namespace='default'):
        doc = {
            'key': key,
            'namespace': namespace,
            'value': value,
            'deleted': False
        }
        return self.col.insert(doc)

    def dequeue(self, _id, key=None):
        query = {'_id': _id, 'deleted': False}
        if key:
            query['key'] = key
        doc = self.col.find_and_modify(query, {'$set': {'deleted': True}})
        if doc:
            doc['value']['_id'] = doc['_id']
            return doc['value']
        else:
            return None

    def get_all(self, key, namespace='default'):
        return self.get_n(key, namespace, 0)

    def get_n(self, key, namespace='default', limit=20):
        spec = {
            'key': key,
            'namespace': namespace,
            'deleted': False
        }
        docs = list(self.col.find(spec, sort=[('_id', 1)], limit=limit))
        for doc in docs:
            doc['value']['_id'] = doc['_id']
        return map(itemgetter('value'), docs)

    def get(self, _id):
        doc = self.col.find_one({'_id': _id, 'deleted': False})
        if doc:
            doc['value']['_id'] = doc['_id']
            return doc['value']
        else:
            return None

    def remove(self, _id):
        result = self.col.update({'_id': _id}, {'$set': {'deleted': True}})
        return result['n'] == 1

    def count(self, key, namespace='default'):
        spec = {
            'key': key,
            'namespace': namespace,
            'deleted': False
        }
        return self.col.find(spec).count()

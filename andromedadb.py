# andromedadb.py

from BTrees.OOBTree import OOBTree
import datetime
import hashlib
import gzip
import json
import os
import pickle
from random import SystemRandom
import uuid


def seconds_since_epoch():
    t_now = datetime.datetime.utcnow()
    t_epoch = datetime.datetime(2016, 2, 26, 6, 45)
    t_delta = (t_now - t_epoch).seconds
    return t_delta


def gen_nonce():
    crypto_thing = SystemRandom()
    return crypto_thing.randrange(17179869184)


def hash_data(data_to_hash):
    return hashlib.sha256(str(data_to_hash).encode()).hexdigest()


class AndromedaDB:
    nonce = 0
    db_path = '.'

    # It was decided that a DB should be responsible for it's own transactions.
    # Writes must be committed (synchronized) before passing on data.
    def save(fname, payload):
        object_blob = None
        with gzip.open(fname, 'wb') as object_file:
            pickle.dump(payload, object_file)
        return True

    # This totally will not fly in C or Rust.  Type will need to be
    # pre-determined before defining this variable.
    def load(fname):
        object_blob = None
        with gzip.open(fname, 'rb') as object_file:
            object_blob = pickle.load(object_file)
        return object_blob

    class Document:
        doc_btree = OOBTree()
        file_mode = 'wb+'
        file_name = ''
        file_object = None
        record_serial = 'doc_' + str(uuid.uuid4())

        def __init__(self, fname=None, mode=None):
            self.file_name = fname
            self.file_mode = mode
            if self.file_name:
                if self.file_mode:
                    self.file_object = open(self.file_name, self.file_mode)
            self.doc_btree.update({
                'atime': 0,
                'ctime': 0,
                'serial': '',
                'data': {},
                'digest': '',
                'codex_doc': 1,
                'mtime': 0
            })

        def insert(self, key, data):
            # Build the document and add it to data key values
            t_delta = seconds_since_epoch()
            self.doc_btree.update({
                'atime': t_delta,
                'ctime': t_delta,
                'serial': 'doc_' + str(uuid.uuid4()),
                'data': json.dumps(data),
                'digest': hash_data(self.doc_btree['data']),
                'mtime': t_delta
            })
            AndromedaDB.save(self.doc_btree['serial'], self.doc_btree)
            return self.doc_btree

        # target refers to the actual value of the data to base a retreival on
        # target_type referst to 1 of either 'key' or 'value'
        # NOTE: query will be used to find a specified value when a document
        # key is not known.  Need to figure out how to keep it from being slow.
        def extract(self, db_filename, search_target, target_type='key'):
            ret_val = None
            # Load the DB file
            object_blob = AndromedaDB.load(db_filename)
            self.doc_btree = object_blob
            if target_type == 'key':
                ret_val = self.doc_btree.has_key(search_target)
            elif target_type == 'value':
                ret_val = self.doc_btree.values(search_target)
            else:
                ret_val = -1
            return ret_val

        # It might be better to make these methods call an AndromedaDB.delete
        def destroy(self, object_serial):
            object_blob = AndromedaDB.load(object_serial)
            os.remove(object_serial)
            return object_blob

    class Table:
        # Honestly, we'll probably just embed an SQLite3 table into a pickle
        # and call it good enough, even in production.  The use case for this
        # is likely a small data set (< 20,000 records)
        # ... or maybe this will be a hash table.  This will evolve when a clear
        # use case is established.
        serial = 'tab_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Edge:
        edg_dict = {
            'codex_edg': 1,
            'serial': '',
            'type': '',
            'vertex': {}
        }
        edg_serial = 'edg_' + str(uuid.uuid4())

        def __init__(self):
            pass

        # This whole thing is a fuster cluck...
        def create(self, edg_type, vertices):
            # Investigate vertices.  Should have parent/child field.
            if vertices == 'directed':
                self.edg_dict['type'] = 'directed'
                if isinstance(vertices, dict):
                    print(":: It's a dictionary.  Yay")
                else:
                    print(":: It's a {t}, not a dictionary.".format(
                        t=type(vertices)))
                self.edg_dict['vertex'] = None
            elif vertices == 'nondirected':
                self.edg_dict['type'] = 'nondirected'
                self.edg_dict['vertex'] = None
            elif vertices == 'tree':
                self.edg_dict['type'] = 'tree'
                self.edg_dict['vertex'] = None
            else:
                self.edg_dict['type'] = 'null'
                self.edg_dict['vertex'] = None

        def destroy(self, edg_serial):
            pass

    # NOTE: Vertex is a pointer to other objects.  It does not contain the
    # object(s) it references
    class Vertex:
        vertex_serial = 'ver_' + str(uuid.uuid4())
        vertex_dict = {'atime': None,
                       'base': '',
                       'codex_ver': 1,
                       'ctime': None,
                       'edges': [],
                       'label': '',
                       'mtime': None,
                       'priority': 0,
                       'serial': ''
                       }

        def __init__(self):
            pass

        def create(self, object_serial, object_priority, object_label=None):
            self.vertex_dict['atime'] = seconds_since_epoch()
            self.vertex_dict['base'] = object_serial
            self.vertex_dict['ctime'] = self.vertex_dict['atime']
            self.vertex_dict['label'] = object_label
            self.vertex_dict['mtime'] = self.vertex_dict['atime']
            self.vertex_dict['priority'] = int(object_priority)
            self.vertex_dict['serial'] = self.vertex_serial
            print(":: Writing file ", self.vertex_dict['serial'])
            AndromedaDB.save(self.vertex_dict['serial'], self.vertex_dict)
            return self.vertex_dict

        def destroy(self, object_serial):
            object_blob = AndromedaDB.load(object_serial)
            os.remove(object_serial)
            return object_blob

    # A container for 2 or more documents or (xor) tables so they can become a Vertex
    class Collection:
        serial = 'col_' + str(uuid.uuid4())

        def __init__(self):
            pass
    # A container of 2 or more docuements or (inclusive) tables so they can become a Vertex
    class Assimilation:
        serial = 'ass_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Hyperlink:
        serial = 'hyp_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Block:
        serial = 'blo_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Chain:
        serial = 'cha_' + str(uuid.uuid4())

        def __init__(self):
            pass

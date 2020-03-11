# NOW WITH B-TREES!!
# https://btrees.readthedocs.io/en/latest/

from BTrees.OOBTree import OOBTree
import datetime
import hashlib
import json
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
                'mtime': 0
            })

        # DISCUSSION: Save internally, or present the data to be saved to a
        # microservice within the PCAS ecosystem?
        def save(self, fname=None):
            if fname:
                self.file_name = fname
            # If a file is already open...
            if self.file_object:
                # Do some stuff
                # update access time, and modified time
                # parse existing data and append current data, the write
                pass
            else:
                # If not, open the file.
                self.file_object = (self.file_name, self.file_mode)
                # Update atime, ctime, and mtime
                # write data

        def load(self):
            pass

        def insert(self, key, data):
            # Build the document and add it to data key values
            t_delta = seconds_since_epoch()
            self.doc_btree.update({
                'atime': t_delta,
                'ctime': t_delta,
                'serial': str(uuid.uuid4()),
                'data': json.dumps(data),
                'digest': hash_data(self.doc_btree['data']),
                'mtime': t_delta
            })
            return self.doc_btree

        # target refers to the actual value of the data to base a retreival on
        # target_type referst to 1 of either 'key' or 'value'
        # NOTE: It occurred to me on 2020-03-11 @ 12:47 UTC that in our use
        # case query and extract are essentially the same.  Removed query.

        def extract(self, target, target_type='key'):
            ret_val = None
            if target_type == 'key':
                ret_val = self.doc_btree.has_key(target)
            elif target_type == 'value':
                ret_val = self.doc_btree.values(target)
            else:
                ret_val = -1
            return ret_val

        def delete(self, serial):
            pass

    class Table:
        # Honestly, we'll probably just embed an SQLite3 table into a pickle
        # and call it good enough, even in production.  The use case for this
        # is likely a small data set (< 20,000 records)
        serial = 'tab_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Edge:
        """
         Appends an 'edges':('edge_1','edge_2','edge_n') into the wrapper dict
         Then creates and edg_<UUID> pickle with the contents:
         {'type': 'directional | ambiguous | tree(n)',
            'vertex':('<type>','<vertex_1>'...'<vertex_n>') }

            'type' can be
            (directional)   parent, child
            (ambiguous)     simple
            (tree)          root, branch
        """
        serial = 'edg_' + str(uuid.uuid4())

        def __init__(self):
            pass

    class Vertex:
        """
        A dict with 'base': '<serial>', 'edge':('edge_1','edge_2','edge_n'),
        Example:
         {
            'base': 'doc_2fdd6ce-bf64-44a3-b710-ba77ef6bf58c',
            'edge': (edg_9e73f43a-32a9-48d4-8abe-8fd127e37530,
                'edg_3fb991c4-41dc-4581-bd46-f7cbd473a176',
                'edg_54f93345-a4b9-4523-832d-f1a0edf136c6'),
            'label': 'locations'
            'priority': 99
        }
        Lower number = higher priority
        Connecting vertex priority must be equal to (ambiguous edge),
        or greater than (directional, tree) the vertexes connected to it
        WITHOUT skipping priorities between connections.
        See doc/Allowed Vertex Relationships.odg for an illustration
        """
        serial = 'ver_' + str(uuid.uuid4())
        vertex_dict = {}

        def __init__(self):
            pass

        def create(self, object_label=None,
                   object_serial, object, object_priority):
            self.vertex_dict.update('atime') = seconds_since_epoch()
            self.vertex_dict.update('base') = object_serial
            self.vertex_dict.update('ctime') = self.vertex_dict['atime']
            self.vertex_dict.update('label') = object_label
            self.vertex_dict.update('mtime') = self.vertex_dict['atime']
            self.vertex_dict.update('object') = object
            self.vertex_dict.update('priority') = int(object_priority)
            self.vertex_dict.update('serial') = self.serial
            file_path = AndromedaDB.db_path + '/' + self.serial
            ret_val = pickle.dump(file_path, self.vertex_dict)
            print('vertex retval ', ret_val)
            return ret_val

    class Collection:
        serial = 'col_' + str(uuid.uuid4())

        def __init__(self):
            pass

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

# NOW WITH B-TREES!!
# https://btrees.readthedocs.io/en/latest/

from BTrees.OOBTree import OOBTree
import datetime
import hashlib
import json
import pickle
from random import SystemRandom
import uuid


# =================================================================================================================== #
# PROBLEMS:
# 1. Writes to source dir instead of a dir defined by env var or passed string
# 2. Writes a new pickle for every doc without anyway to track the contents of each
# =================================================================================================================== #

def seconds_since_epoch():
    t_now = datetime.datetime.utcnow()
    t_epoch = datetime.datetime(2016,2,26,6,45)
    t_detla = (t_now - t_epoch).seconds
    return t_delta

def gen_nonce():
    crypto_thing = SystemRandom()
    return crypto_thing.randrange(17179869184)

def hash_data( data_to_hash):
    return hashlib.sha256(str(data_to_hash).encode()).hexdigest()


class AndromedaDB:
    nonce = 99999999999

    class Document:
        doc_data = OOBTree()
        file_mode = 'wb+'
        file_name = ''
        file_object = None
        serial = 'doc_' + str(uuid.uuid4())

        def __init__(self, fname, mode):
            self.file_name = fname
            self.file_mode = mode
            self.file_object = open(self.file_name, self.file_mode)

        # DISCUSSION: Save internally, or present the data to be saved to a
        # microservice withint the PCAS ecosystem?
        def save(self, fname=self.file_name):
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
            doc_btree = OOBTree()
            # Init document structure, generate and add random UUID
            doc_serial = 'doc_' + str(uuid.uuid4())
            # Binarize and hash the content of 'data'
            doc_digest = hashlib.sha256(bytes(list(doc_btree.values('data')))).hexdigest()
            # Build the document
            doc_btree.update({
                'atime': seconds_since_epoch,
                'ctime': '',
                'serial': doc_serial,
                'data': json.dumps(data),
                'digest': hash_data(doc_btree['data']),
                'mtime': datetime.datetime.utcnow()
                })
            return doc_btree


        def extract(self, target, target_type):
            #TODO: accept either title or serial as input to exctact a document
            doc_btree = OOBTree()
            #TODO: Replace with app.pcas_pickler calls
            with open(serial, 'rb') as file:
                doc_btree = pickle.load( file )
            doc_data = list(doc_btree.values('data'))
            # NOTE: Returns values from position 'digest', to the end.  Needs a little trimming
            doc_digest = list(doc_btree.values('digest'))
            doc_digest = str().join(doc_digest[:1])

            print("DATA .   : ", doc_data)
            print("DIGEST   : ", doc_digest)
            print("T(DIGEST): ", type(doc_digest))
            verify_digest = hashlib.sha256(bytes(list(doc_btree.values('data')))).hexdigest()
            print("HASHLIB  : ", verify_digest)
            print("T(HASHLIB): ", type(verify_digest))

            if hashlib.sha256(bytes(list(doc_btree.values('data')))).hexdigest() == doc_digest:
                return(doc_data)
            else:
                return None


        def query(self, intent, term):
            pass


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


        def __init__(self):
            pass


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

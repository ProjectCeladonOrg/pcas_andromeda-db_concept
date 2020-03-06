import datetime
import hashlib
import json
import pickle
from random import SystemRandom
import uuid
import zlib


#TODO: Replace with app.pcas_pickler calls
def dict_to_bin(the_dict):
    #str = json.dumps(the_dict)
    #binary = ' '.join(format(ord(letter), 'b') for letter in str)
    #return binary
    # Convert to json
    json_data = json.dumps(the_dict)
    blob_data = str(json_data).encode()
    return blob_data


def bin_to_dict(the_binary):
    return json.loads(str(the_binary).decode())


def gen_nonce():
    crypto_thing = SystemRandom()
    return crypto_thing.randrange(17179869184)


class AndromedaDB:
    nonce = 99999999999

    def gen_nonce():
        return 1


    class Document:
        serial = 'doc_' + str(uuid.uuid4())

        def __init__(self):
            pass


        def insert(self, name, data):
            # Init document structure, generate and add random UUID
            doc_serial = 'doc_' + str(uuid.uuid4())
            doc_dict = { 'serial' : doc_serial }
            # Insert file name
            doc_dict['name'] = name
            # Add data in JSON format to document
            doc_dict['data'] = json.dumps(data)
            # Binarize and hash the content of 'data'
            doc_digest = hashlib.sha256(str(doc_dict['data']).encode()).hexdigest()
            doc_dict['digest'] = doc_digest
            # Let's make a pickle!
            with open(doc_serial, 'wb') as file:
                 pickle.dump(doc_dict, file)
            return {'serial': doc_serial, 'digest': doc_digest}


        def extract(self, serial):
            #TODO: accept either title or serial as input to exctact a document
            data = None
            with open(serial, 'rb') as file:
                data = pickle.load( file )
            data_data = data['data']
            if hashlib.sha256(str(data['data']).encode()).hexdigest() == data['digest']:
                return(data['data'])
            else:
                return None


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

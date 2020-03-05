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
            #TODO: Need to extract the 'data' poriton and verify it's hash,
            # returning only the data
            return data


    class Table:
        serial = 'tab_' + str(uuid.uuid4())

        def __init__(self):
            pass


    class Edge:
        serial = 'edg_' + str(uuid.uuid4())

        def __init__(self):
            pass


    class Vertex:
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

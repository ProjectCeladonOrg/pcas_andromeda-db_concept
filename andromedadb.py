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


        def insert(self, title, data):
            print("\r\n>> INSERT -------------------------------------------------")
            serial = 'doc_' + str(uuid.uuid4())
            encoded_data = dict_to_bin(data)
            print("encoded data: ", encoded_data)
            doc_hash = hashlib.sha256(encoded_data).digest()
            doc_digest = hashlib.sha256(encoded_data).hexdigest()
            doc_record = {'serial':serial, 'title': title, 'data':data, 'hash': doc_hash, 'nonce': gen_nonce()}
            # TODO: pickles must be signed! probably via app.pcas_crypto
            pickle.dump(doc_record, open(serial, 'wb'))
            return {'serial': serial, 'digest': doc_digest}


        def extract(self, serial):
            print("\r\n>> EXTRACT ------------------------------------------------")
            #TODO: accept either title or serial as input to exctact a document
            print("string type:", type(serial) )
            print("string contents:", serial )
            data = None
            #with open(serial, 'rb') as file:
            #    data = bin_to_dict( pickle.load( file ) )
            #data_digest = data[hash]
            #data.pop('serial')
            #data.pop('hash')
            # Test that hash matches data...
            #print('Data after read: ', data)
            #encoded_data = str(data)


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

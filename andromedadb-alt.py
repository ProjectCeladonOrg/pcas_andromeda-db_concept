import datetime
import hashlib
import json
from random import SystemRandom
import uuid
import zlib


def dict_to_bin(input_dict):
    return str(json.dump(input_dict)).encode()

class AndromedaDB:
    nonce = 99999999999

    def gen_nonce():
        return 1

    class Document:
        serial = 'doc_' + str(uuid.uuidv4())

        def __init__(self):
            pass

        def insert(self, serial, title, data):
            doc_hash = hashlib.sha256(data).digest()
            doc_digest = hashlib.sha256(data).hexdigest()
            doc_record = {'serial':serial, 'title': title, 'data':data, 'hash': doc_hash, 'nonce': gen_nonce}
            # TODO: pickles must be signed!
            pickle.dump(dict_to_bin(doc_record), open(doc_digest, 'wb'))
            return {'serial': serial, 'digest': doc_digest)

        def extract( self):
            TODO: accept either title or serial as input to exctact a document

    class Table:
        serial = 'tab_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Edge:
        serial = 'edg_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Vertex:
        serial = 'ver_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Collection:
        serial = 'col_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Assimilation:
        serial = 'ass_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Hyperlink:
        serial = 'hyp_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Block:
        serial = 'blo_' + str(uuid.uuidv4())

        def __init__(self):
            pass

    class Chain:
        serial = 'cha_' + str(uuid.uuidv4())

        def __init__(self):
            pass

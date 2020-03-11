# TODO: This does not conform to PEP or Org standards; Will fix before FST
import andromedadb
from BTrees import OOBTree
import hashlib
import json
from random import SystemRandom
import uuid


testDoc = andromedadb.AndromedaDB.Document()
testVertex = andromedadb.AndromedaDB.Vertex()

print(">> BEGINNING TEST -----------------------------------------------------")
crypto_thing = SystemRandom()
blah_doc = {
    'module': 'pcas_core',
    'mdep': ['pcas_core'],
    'odep':['python3', 'pip3', 'django'],
    'pdep': ['BTrees'],
    'tags':'test,red,99,bogus'
}
print('SAMPLE: ', blah_doc)

print("\r\n\r\n>> INSERTING RECORD -------------------------------------------")
doc_vitals = testDoc.insert("pcas_test", blah_doc)
print('RESULT: ', doc_vitals)

print("\r\n\r\n>> EXTRACTING RECORD ------------------------------------------")
doc_read = testDoc.extract( doc_vitals['serial'], 'data', 'key')
print('RESULT: ', doc_read)

print("\r\n\r\n>> CREATING VERTEX --------------------------------------------")
print('... Getting object serial number')
doc_serial = doc_vitals['serial']
print('RESULT: ', doc_serial)
print('... Creating vertex')
ret_val = testVertex.create(doc_serial, 1)
print('RESULT: ', ret_val)

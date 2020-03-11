# test.py
# TODO: This does not conform to PEP or Org standards; Will fix before FST
import andromedadb
from BTrees.OOBTree import OOBTree
import hashlib
import json
from random import SystemRandom
import uuid


testDoc = andromedadb.AndromedaDB.Document()
testVer = andromedadb.AndromedaDB.Vertex()

print(">> BEGINNING TEST -----------------------------------------------------")
crypto_thing = SystemRandom()
sample_doc = {
    'module': 'pcas_core',
    'mdep': ['pcas_core'],
    'odep':['python3', 'pip3', 'django'],
    'pdep': ['BTrees'],
    'tags':'test,red,99,bogus'
}
print('SAMPLE: ', sample_doc)

print("\r\n\r\n>> INSERTING RECORD -------------------------------------------")
doc_btree = testDoc.insert("pcas_test", sample_doc)
print('RESULT: ', doc_btree)

print("\r\n\r\n>> EXTRACTING RECORD ------------------------------------------")
doc_read = testDoc.extract( doc_btree['serial'], 'data', 'key')
print('RESULT: ', doc_read)

print("\r\n\r\n>> CREATING VERTEX --------------------------------------------")
print('... Getting object serial number')
doc_serial = doc_btree['serial']
print('RESULT: ', doc_serial)
print('... Creating vertex')
ver_dict = testVer.create(doc_serial, 1)
print('!!!!!!!!!!')
print('RESULT: ', ver_dict)
print('TYPE  : ', type(ver_dict))
print('!!!!!!!!!!')

print("\r\n\r\n>> DESTROYING VERTEX ------------------------------------------")
ver_serial = ver_dict['serial']
print('... Serial  : ', ver_serial)
testVer.destroy(ver_serial)

print("\r\n\r\n>> DESTROYING DOCUMENT ----------------------------------------")
print('... Serial  : ', doc_serial)
testDoc.destroy(doc_serial)

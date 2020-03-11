# test.py
# TODO: This does not conform to PEP or Org standards; Will fix before FST
import andromedadb
from BTrees.OOBTree import OOBTree
import hashlib
import json
from random import SystemRandom
import uuid


testDoc1 = andromedadb.AndromedaDB.Document()
testDoc2 = andromedadb.AndromedaDB.Document()
testVer1 = andromedadb.AndromedaDB.Vertex()
testVer2 = andromedadb.AndromedaDB.Vertex()
testEdg1 = andromedadb.AndromedaDB.Edge()

print(">> BEGINNING TEST -----------------------------------------------------")
crypto_thing = SystemRandom()
sample_doc = {
    'module': 'pcas_core',
    'mdep': ['pcas_core'],
    'odep': ['python3', 'pip3', 'django'],
    'pdep': ['BTrees'],
    'tags': 'test,red,99,bogus'
}
print('SAMPLE: ', sample_doc)

print("\r\n\r\n>> INSERTING RECORD 1 -----------------------------------------")
doc_btree1 = testDoc1.insert("pcas_test", sample_doc)
print('RESULT: ', doc_btree1)

print("\r\n\r\n>> EXTRACTING RECORD ------------------------------------------")
doc_read1 = testDoc1.extract(doc_btree1['serial'], 'data', 'key')
print('RESULT: ', doc_read1)

print("\r\n\r\n>> CREATING VERTEX 1 ------------------------------------------")
print('... Getting object serial number')
doc_serial1 = doc_btree1['serial']
print('RESULT: ', doc_serial1)
print('... Creating vertex')
ver_dict1 = testVer1.create(doc_serial1, 1)
print('!!!!!!!!!!')
print('RESULT: ', ver_dict1)
print('TYPE  : ', type(ver_dict1))
print('!!!!!!!!!!')

print("\r\n\r\n>> INSERTING RECORD 2 -----------------------------------------")
doc_btree2 = testDoc2.insert("pcas_test", sample_doc)
print('RESULT: ', doc_btree2)

print("\r\n\r\n>> CREATING VERTEX 2 ------------------------------------------")
print('... Getting object serial number')
doc_serial2 = doc_btree2['serial']
print('RESULT: ', doc_serial2)
print('... Creating vertex')
ver_dict2 = testVer2.create(doc_serial2, 1)
print('!!!!!!!!!!')
print('RESULT: ', ver_dict2)
print('TYPE  : ', type(ver_dict2))
print('!!!!!!!!!!')

print("\r\n\r\n>> CREATING EDGE 1 --------------------------------------------")
edge_dict1 = testEdg1.create('simple', (ver_dict1['serial'], ver_dict2['serial']))

print("\r\n\r\n>> DESTROYING VERTEX ------------------------------------------")
ver_serial1 = ver_dict1['serial']
print('... Serial  : ', ver_serial1)
testVer1.destroy(ver_serial1)

print("\r\n\r\n>> DESTROYING DOCUMENT ----------------------------------------")
print('... Serial  : ', doc_serial1)
testDoc1.destroy(doc_serial1)

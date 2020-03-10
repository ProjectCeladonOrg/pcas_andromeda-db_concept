# TODO: This does not conform to PEP or Org standards; Will fix before FST
import andromedadb
import hashlib
import json
from random import SystemRandom
import uuid


testDoc = andromedadb.AndromedaDB.Document('modules.pdb', 'wb+')

print(">> BEGINNING TEST -----------------------------------------------------")
crypto_thing = SystemRandom()
blah_doc = {
    'module': 'pcas_core',
    'mdep': None,
    'odep':'python3, pip3, django',
    'tags':'test,red,99,bogus'
}
print('SAMPLE: ', blah_doc)

print("\r\n\r\n>> INSERTING RECORD -------------------------------------------")
doc_vitals = testDoc.insert("pcas_test", blah_doc)
print('RESULT: ', doc_vitals)

print("\r\n\r\n>> EXTRACTING RECORD ------------------------------------------")
doc_read = testDoc.extract(doc_vitals["serial"])
print('RESULT: ', doc_read)

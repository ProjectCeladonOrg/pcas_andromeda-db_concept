#import andromedadb
import andromedadb
import hashlib
import json
from random import SystemRandom
import uuid


testDoc = andromedadb.AndromedaDB.Document()

#print("beginning this thing")
crypto_thing = SystemRandom()
nonce = crypto_thing.randrange(17179869184)
blah_doc = {'tags':'test,red,99,bogus','nonce':nonce}
#print(blah_doc)
doc_vitals = testDoc.insert("Test Document 1", blah_doc)
#print("doc vitals: ", doc_vitals)
#print("serial: ", doc_vitals["serial"])
doc_read = testDoc.extract(doc_vitals["serial"])

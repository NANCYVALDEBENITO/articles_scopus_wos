#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyzotero import zotero
import pandas as pd 
import numpy as np
import csv


zot = zotero.Zotero('4867718','user','2I7tmhYZQXln3Ciu5u3BxLw5')
# we now have a Zotero object, zot, and access to all its methods
print(zot)

items = zot.top(limit=2)

#Returns items from the specified collection. This includes sub-collection items

for item in items:
	print('Item Type: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
	f = open('test.csv','wb')
	print(item)
	w = csv.DictWriter(f,item.keys())
	w.writerows(item.encode("utf-8").decode("ascii"))

print(items.encode("utf-8").decode("ascii"))

collection_isi_2017 = zot.collection('WNWA9J3A')

print(collection_isi_2017)
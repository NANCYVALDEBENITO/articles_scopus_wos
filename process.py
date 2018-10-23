#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 

df = pd.read_csv("/home/nvaldebenito/Documentos/20_articles_process/cr2_articles.csv", sep='\t', encoding='utf-8')

DOI = df["Copy for Cites DOI"]

print(len(DOI))

DOI_SCOPUS=[]
DOI_WEBOFS=[]

for i in range(0,len(DOI)):
	DOI_SCOPUS.append(str(" DOI(")+str(DOI[i])+str(")"))

for i in range(0,len(DOI)):
	DOI_WEBOFS.append(str(" DO=(")+str(DOI[i])+str(") OR"))


DOI_SCOPUS="".join(DOI_SCOPUS)
DOI_WEBOFS="".join(DOI_WEBOFS)

print(DOI_WEBOFS)
print(DOI_SCOPUS)
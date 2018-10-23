#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 
from selenium import webdriver

df = pd.read_csv("/home/nvaldebenito/Documentos/20_articles_process/cr2_articles.csv", sep='\t', encoding='utf-8')

DOI = df["Copy for Cites DOI"]

DOI_SCOPUS=[]
DOI_WEBOFS=[]

for i in range(0,len(DOI)):
	DOI_SCOPUS.append(str(" DOI(")+str(DOI[i])+str(")"))

for i in range(0,len(DOI)):
	DOI_WEBOFS.append(str(" DO=(")+str(DOI[i])+str(")"))

DOI_SCOPUS="".join(DOI_SCOPUS)
DOI_WEBOFS=" OR".join(DOI_WEBOFS)

print(DOI_WEBOFS)

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?SID=7CWt7eMDxKOrXhHC3cS&product=WOS&search_mode=AdvancedSearch")
button = driver.find_element_by_id('value(input1)')
button.send_keys(DOI_WEBOFS)

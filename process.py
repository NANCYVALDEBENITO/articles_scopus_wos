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

#add DOI
button = driver.find_element_by_id('value(input1)')
button.send_keys(DOI_WEBOFS)

#start to search
enter = driver.find_element_by_id('search-button')
enter.click()

#click in number of publications found
enter = driver.find_element_by_id('set_4_div')
enter.click()

#enter = driver.find_element_by_class_name('select2-selection__arrow')
#enter.click()
#save in other files format 
enter = driver.find_element_by_id('select2-saveToMenu-container')
enter.click()

#
enter = driver.find_element_by_id('markFrom')
enter.send_keys(1)

enter = driver.find_element_by_id('markTo')
npub  = driver.find_element_by_id('hitCount.top')
enter.send_keys(npub)

enter = driver.find_element_by_id('select2-bib_fields-result-qq0h-HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ')
enter.click()

enter = driver.find_element_by_id('select2-saveOptions-result-qs3k-tabWinUTF8')
enter.click()

enter = driver.find_element_by_id('select2-saveToMenu-result-veek-other')
enter.click()
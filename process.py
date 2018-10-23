#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 
from selenium import webdriver

#open dataframe DOI
df = pd.read_csv("/home/nvaldebenito/Documentos/20_articles_process/cr2_articles.csv", sep='\t', encoding='utf-8')

DOI = df["Copy for Cites DOI"]

DOI_SCOPUS=[]
DOI_WEBOFS=[]

#write string
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

#npub  = len(driver.find_elements_by_xpath('/summary.do?product=WOS&amp;doc=1&amp;qid=21&amp;SID=7CWt7eMDxKOrXhHC3cS&amp;search_mode=AdvancedSearch&amp;update_back2search_link_param=yes'))
#print(npub)

#click in number of publications found
enter = driver.find_element_by_id('set_4_div')
enter.click()

#enter = driver.find_element_by_class_name('select2-selection__arrow')
#enter.click()

#save in other files format 
enter = driver.find_element_by_id('select2-saveToMenu-container')
enter.click()

#from number
enter = driver.find_element_by_id('markFrom')
enter.send_keys(1)

#to number
enter = driver.find_element_by_id('markTo')
enter.send_keys(243)

#option for register content
enter = driver.find_elements_by_xpath('//span[contains(@class, "select2") and contains(@class, "select2-container") and contains(@class, "select2-container--default") and contains(@class,"select2-container--focus")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-selection") and contains(@class,"select2-selection--single")]')
enter = driver.find_element_by_xpath('//option[contains(@value,"HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ")]')
enter.click()

#option format file

enter = driver.find_elements_by_xpath('//span[contains(@class, "select2") and contains(@class, "select2-container") and contains(@class, "select2-container--default") and contains(@class,"select2-container--below") and contains(@class,"select2-container--focus") and contains(@class,"select2-container--open")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-selection") and contains(@class,"select2-selection--single")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-results__option select2-results__option--highlighted")]')
enter = driver.find_element_by_xpath('//option[contains(@value,"tabWinUTF8")]')
enter.click()


enter = driver.find_element_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
enter = driver.find_element_by_xpath('//span[contains(@class,"quickoutput-action")]')
enter = driver.find_element_by_xpath('//button[contains(@class,"standard-button") and contains(@class,primary-button) and contains(@title,"Enviar")]')
enter.click()

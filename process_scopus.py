#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#open dataframe DOI
df = pd.read_csv("/home/nvaldebenito/Documentos/20_articles_process/cr2_articles.csv", sep='\t', encoding='utf-8')

DOI_1 = df["Copy for Cites DOI"]


DOI_SCOPUS=[]


#write string
for i in range(0,len(DOI)):
	DOI_SCOPUS.append(str(" DOI(")+str(DOI[i])+str(")"))

DOI_SCOPUS="".join(DOI_SCOPUS)

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://www.scopus.com")



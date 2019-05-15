#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Importing libraries
import pandas as pd 
import numpy as np

#Open and read Scopus database
df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')

#Open and read Web of Science database
df_webofscience = pd.read_csv("input_table/02_webofscience.csv", sep='\t', encoding='utf-8')

#Zotero database
df_zotero = pd.read_csv("input_table/06_cr2_2019_isi.csv", sep=',', encoding='utf-8')

#Look for DOI  for including to cr2articles database. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
doi_input = df["DOI"]

# Input-Output 
df_master = pd.read_csv("cr2_articles.csv", sep=';',encoding='utf-8')
doi_master = df_master["Copy for Cites DOI"]
#df_users = pd.read_csv("input_table/07_users_Investigadores.csv", sep=',', encoding='utf-8')

#Filter by DOI
df_zotero=pd.merge(df,df_zotero, on=["DOI"])
df_scopus= pd.merge(df,df_scopus, on=["DOI"])

#Look for columns on Zotero 
journal 	= df_zotero["Publication Title"]
doi_zotero	= df_zotero["DOI"]
url			= df_zotero["Url"]
issn 		= df_zotero["ISSN"]
line		= df_zotero["Manual Tags"]
title		= df_zotero["Title"]
year		= df_zotero["Publication Year"]
volume		= df_zotero["Volume"]
issue		= df_zotero["Issue"]
pages		= df_zotero["Pages"]
abstracts	= df_zotero["Abstract Note"]
authors_zotero 	= df_zotero["Author"]

#Add columns on new file cr2_articles
		
df["Funding Year"]				= "2019"
df["Report 4.5"]				= "no"
df["Manual Tags"]				= line

df["Publication Year"]			= year
df["Author original"]			= authors_zotero
df["Author"]					= authors_zotero


df["Title of publication"]		= title
df["Journal"]					= journal
df["Volume"] 					= ["vol."+(str(v)) for v in volume]
df["Issue"]						= [" is."+(str(i)) for i in issue ]
df["Pages"]						= pages
df["Year"]						= year

df["ISSN"]						= issn
df["Copy for Cites Title"]		= title
df["Copy for Cites DOI"]		= doi_zotero


df["Volume"] = df["Volume"]+df["Issue"]
df["Volume"]=[d.replace('nan','') for d in df["Volume"]]


#Create a new dataframe
df_master_created = pd.DataFrame(df, columns = ["N","Funding Year", "Report 4.5", "Manual Tags", "Research Lines", "Publication Year",
 "Author original","Author", "File Attachments", "Link Attachments","Manual Tags", "Lines Collaboration", "N", "Title of publication", "Journal", "Volume",
 "Pages", "Year", "CR2", "Researchers","Principal Researchers", "Full time Researchers", "Associate Researchers", "Adjoint Researchers", "Postdoc.", 
 "Undergraduated Students", "Graduated Students", "FONDAP", "FONDECYT", "FONDEF", "BASAL", "ICM", "OTHER (specify)", "ESPECIFY", "Journal Name", "ISSN",
 "Name Check", "Sub Category", "Journal Rank", "% Journal Rank", "Is it top 10 in category", "Journal Impact Factor", "5 year Journal Impact Factor", 
 "Scimago Quartile", "Copy for Cites Title", "Copy for Cites DOI"])

df_master_created.to_csv(str("output_table/cr2_articles.csv"), sep=';', encoding='utf-8')

df_master = pd.read_csv("cr2_articles.csv", sep=';',encoding='utf-8')
df_master_created = pd.read_csv("output_table/cr2_articles.csv", sep=';',encoding='utf-8')

print(df_master)
print(df_master_created)
frames =[df_master,df_master_created]
result =pd.concat(frames,sort=False)
print(result)

result=result.drop('Unnamed: 0', 1)

print(result)
result.to_csv(str("cr2_articles_modified.csv"), sep=';', encoding='utf-8', index=False)



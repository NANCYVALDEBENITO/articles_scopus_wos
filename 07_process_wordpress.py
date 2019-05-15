#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np



#Scopus 
df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')

#Web of Science
df_webofscience = pd.read_csv("input_table/02_webofscience.csv", sep='\t', encoding='utf-8')

#Zotero
df_zotero = pd.read_csv("input_table/06_cr2_2019_isi.csv", sep=',', encoding='utf-8')

#Look for DOI to include to database intranet. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
doi_input = df["DOI"]

# Input-Output
df_wordpress = pd.read_csv("13-ARTICULOS-CR2-ISI-y-NO-ISI-2019-05-13.csv", sep=';',encoding='utf-8')
doi_wordpress = df_wordpress["DOI"]

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

#Add columns on new file Intranet
df["N"]					  		= ""
df["Funding Year"]				= "2019"
df["Línea de Investigación"]	= line
df["Research Lines"]			= ""
df["Año"]						= year
df["Autores"]					= authors_zotero
df["Título"]					= title
df["Revista"]					= journal
df["Ficha de Publicación"]		= ""
df["Volume"] 					= ["vol."+(str(v)) for v in volume]
df["Issue"]						= [" is."+(str(i)) for i in issue ]
df["DOI"]						= doi_zotero
df["ISSN"]						= issn
df["Abstract"] 					= abstracts
df["Acceso"]					= url
df["Páginas"]					= pages
df["Volumen"] 					= df["Volume"]+df["Issue"]
df["Index"]						= "Thomson Reuters ISI"
df["Volumen"]					= [d.replace('nan','') for d in df["Volumen"]]


#Create a new dataframe Wordpress
df_wordpress_created = pd.DataFrame(df, columns = ["N","Funding Year", "Línea de Investigación", "Research Lines",
	"Año", "Autores", "Título", "Revista", "Ficha de Publicación", "DOI", "ISSN", "Abstract", "Acceso", "Páginas",
	"Volumen", "Index"])

#Save dataframe in a new csv file
df_wordpress_created.to_csv(str("output_table/wordpress.csv"), sep=';', encoding='utf-8')

#Open and read dataframes, table wordpress original on web and table wordpress created
df_wordpress = pd.read_csv("13-ARTICULOS-CR2-ISI-y-NO-ISI-2019-05-13.csv", sep=';',encoding='utf-8')
df_wordpress_created = pd.read_csv("output_table/wordpress.csv", sep=';',encoding='utf-8')

print(df_wordpress)
print(df_wordpress_created)
frames =[df_wordpress,df_wordpress_created]
result =pd.concat(frames,sort=False)
print(result)

result=result.drop('Unnamed: 0', 1)

print(result)
#Dataframes concatenated in a new file modified
result.to_csv(str("wordpress_modified.csv"), sep=';', encoding='utf-8', index=False)

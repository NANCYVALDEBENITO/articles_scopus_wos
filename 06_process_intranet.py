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
df_intranet = pd.read_csv("tracker_38.csv", sep=',',encoding='utf-8')
doi_intranet = df_intranet["DOI -- 746"]
df_users = pd.read_csv("input_table/07_users_Investigadores.csv", sep=',', encoding='utf-8')

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
df["itemId"]					= ""
df["status"]					= ""
df["created"]					= ""
df["lastModif"]					= ""
df["Datos Publicación -- 737"]	= ""

df["Estado -- 741"]				= "Publicadas"
df["Reconocimiento o Afiliacion -- 751"] = "SI"
df["Título -- 742"]				= title
df["Código ISSN / ISBN -- 747"]	= issn
df["DOI -- 746"]				= doi_zotero
df["Autores -- 743"]			= authors_zotero
df["Lineas Involucradas -- 745"]= line
df["Nombre Journal -- 748"]		= journal
df["Ubicación en Línea -- 749"]	= url
df["Año de Publicación -- 750"]	= year
df["PARTICIPACION -- 753"]		= ""
df["FONDOS que aportaron a la publicación -- 754"] = "A COMPLETAR"
df["% aportado por FONDAP -- 755"] = "A COMPLETAR"
df["% aportado por FONDECYT -- 756"] = "A COMPLETAR"
df["% aportado por FONDEF -- 757"] = "A COMPLETAR"
df["% aportado por BASAL -- 758"] = "A COMPLETAR"
df["% aportado por ICM -- 759"] = "A COMPLETAR"
df["% aportado por Otro (indicar) -- 760"] = "A COMPLETAR"
df["Adjunta la Publicación -- 763"] = ""
df["Abstract -- 764"] = abstracts
df["Revisión INTERNA -- 738"] = "en zotero"
df["Periodo -- 752"] = "A REPORTAR 2019"
df["Líneas Involucradas antiguas -- 744"] = ""

#Process like replace lines
df["Lineas Involucradas -- 745"]=[d.replace('Ciudades Resilientes',':Cities') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace('Cambio de Uso de Suelo',':Land Use Change') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace('Zonas Costeras',':Coastal Zones') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace('Agua y Extremos',':Water extremes') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace('Gobernanza e Interfaz Ciencia y Política'.decode('utf8'),':Governance') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace('Transversal',':Transversal') for d in df["Lineas Involucradas -- 745"]]
df["Lineas Involucradas -- 745"]=[d.replace(';',',') for d in df["Lineas Involucradas -- 745"]]

print(authors_zotero)
users_all=[]
for n in range(0,len(authors_zotero)):
	users=[]
	if 'Lara, A'.decode('utf8') in  authors_zotero[n]:
		users.append('alara')
		
	if 'Muñoz, A'.decode('utf8') in  authors_zotero[n]:
		users.append('amunoz')
		
	if 'Osses, A'.decode('utf8') in  authors_zotero[n]:
		users.append('aosses')
	
	if 'Sepulveda, A'.decode('utf8') in  authors_zotero[n] or 'Sepulveda-Jauregui, A'.decode('utf8') in  authors_zotero[n]:
		users.append('asepulveda')

	if 'Urquiza, A'.decode('utf8') in  authors_zotero[n]:
		users.append('aurquiza')
	
	if 'Diez, B'.decode('utf8') in  authors_zotero[n]:
		users.append('bdiez')

	if 'Aguirre, C'.decode('utf8') in  authors_zotero[n]:
		users.append('caguirre')

	if 'Ibarra, C'.decode('utf8') in  authors_zotero[n]:
		users.append('cibarra')
	
	if 'Little, C'.decode('utf8') in  authors_zotero[n]:
		users.append('clittle')
	
	if 'Tejo, C'.decode('utf8') in authors_zotero[n]:
		users.append('ctejo')
	if 'Zamorano, C'.decode('utf8') in  authors_zotero[n]:
		users.append('czamorano')

	if 'Bozkurt, D'.decode('utf8') in  authors_zotero[n]:
		users.append('dbozkurt')

	if 'Christie, D'.decode('utf8') in  authors_zotero[n]:
		users.append('dchristie')

	if 'Gayo, E'.decode('utf8') in  authors_zotero[n]:
		users.append('egayo')

	if 'Lambert, F'.decode('utf8') in  authors_zotero[n]:
		users.append('flambert')
		
	if 'Blanco, G'.decode('utf8') in  authors_zotero[n] or 'Blanco Wells, G'.decode('utf8') in  authors_zotero[n]:
		users.append('gblanco')
	
	if 'Zambrano, M'.decode('utf8') in  authors_zotero[n] or 'Zambrano-Bigiarini, M'.decode('utf8') in  authors_zotero[n]:
		users.append('hzambrano')
		
	if 'Masotti'.decode('utf8') in  authors_zotero[n]:
		users.append('imasotti')
	if 'Boisier, J'.decode('utf8') in  authors_zotero[n]:
		users.append('jboisier')
	if 'Cordero, L'.decode('utf8') in  authors_zotero[n]:
		users.append('lcordero')
	if 'Farías, L'.decode('utf8') in  authors_zotero[n] or 'Farias, L'.decode('utf8') in  authors_zotero[n]:
		users.append('lfarias')
	if 'Gallardo, L'.decode('utf8') in  authors_zotero[n]:
		users.append('lgallardo')
	if 'Galleguillos, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mgalleguillos')
	if 'Gonzalez, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mgonzalez')
	if 'Jacques, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mjacques')
	if 'Munizaga, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mmunizaga')
	if 'Osses, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mosses')
	if 'Rojas, M'.decode('utf8') in  authors_zotero[n]:
		users.append('mrojas')
	if 'Hitschfeld, N'.decode('utf8') in  authors_zotero[n]:
		users.append('nhitschfeld')
	if 'Huneeus, N'.decode('utf8') in  authors_zotero[n]:
		users.append('nhuneeus')
	if 'Aldunce, P'.decode('utf8') in  authors_zotero[n]:
		users.append('paldunce')
	if 'Moraga, P'.decode('utf8') in  authors_zotero[n]:
		users.append('pmoraga')
	if 'Moreno, P'.decode('utf8') in  authors_zotero[n]:
		users.append('pmoreno')
	if 'Smith, P'.decode('utf8') in  authors_zotero[n]:
		users.append('psmith')
	if 'Arriagada, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rarriagada')
	if 'De Polz-Holz, R'.decode('utf8') in  authors_zotero[n]  or 'de Polz-Holz, R'.decode('utf8') in  authors_zotero[n] or 'De Pol-Holz, R'.decode('utf8') in  authors_zotero[n] :
		users.append('rdepol')
	if 'Garreaud, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rgarreaud')
	if 'O´Ryan, R'.decode('utf8')  in  authors_zotero[n] or "O'Ryan, R" in  authors_zotero[n]:
		users.append('roryan')
	if 'Rondanelli, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rrondanelli')
	if 'Sapiains, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rsapiains')
	if 'Seguel, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rseguel')
	if 'Urrutia, R'.decode('utf8') in  authors_zotero[n] or 'Urrutia-Jalabert, R'.decode('utf8') in  authors_zotero[n]:
		users.append('rurrutia')
	if 'Gomez, S'.decode('utf8') in  authors_zotero[n] or 'Gómez, S'.decode('utf8') in  authors_zotero[n]:
		users.append('sgomez')
	if 'Delgado, V'.decode('utf8') in  authors_zotero[n]:
		users.append('vdelgado')
	if 'Fleming, Z'.decode('utf8') in  authors_zotero[n]:
		users.append('zfleming')
	if 'Miranda, A'.decode('utf8') in  authors_zotero[n]:
		users.append('amiranda')

	print(users)
	print(authors_zotero[n])
	users_all.append(users)

print(users_all)
df["Usuario -- 739"] = users_all
df["Usuario -- 739"] = [str(d).replace("'","").replace('[','').replace(']','').replace("''","") for d in df["Usuario -- 739"]]

#Create a new dataframe
df_intranet_created = pd.DataFrame(df, columns = ["itemId","status","created", "lastModif",
	 "Datos Publicación -- 737","Usuario -- 739", "Reconocimiento o Afiliacion -- 751", "Estado -- 741",
	 "Título -- 742", "Autores -- 743", "Lineas Involucradas -- 745", "DOI -- 746" ,"Código ISSN / ISBN -- 747",
	  "Nombre Journal -- 748","Ubicación en Línea -- 749","Año de Publicación -- 750", "PARTICIPACION -- 753",
	  "FONDOS que aportaron a la publicación -- 754", "% aportado por FONDAP -- 755", 
	  "% aportado por FONDECYT -- 756", "% aportado por FONDEF -- 757", "% aportado por BASAL -- 758",
	  "% aportado por ICM -- 759", "% aportado por Otro (indicar) -- 760","Adjunta la Publicación -- 763",
	  "Abstract -- 764", "Revisión INTERNA -- 738","Periodo -- 752","Líneas Involucradas antiguas -- 744"])

df_intranet_created.to_csv(str("output_table/intranet.csv"), sep=',', encoding='utf-8')

df_intranet = pd.read_csv("tracker_38.csv", sep=',',encoding='utf-8')
df_intranet_created = pd.read_csv("output_table/intranet.csv", sep=',',encoding='utf-8')

print(df_intranet)
print(df_intranet_created)
frames =[df_intranet,df_intranet_created]
result =pd.concat(frames,sort=False)
print(result)

result=result.drop('Unnamed: 0', 1)

print(result)
result.to_csv(str("tracker_38_modified.csv"), sep=',', encoding='utf-8', index=False)

#df_zotero.to_csv(str("test_zotero.csv"), sep=',', encoding='utf-8')
#df_intranet.to_csv(str("test_intranet.csv"), sep=',', encoding='utf-8')
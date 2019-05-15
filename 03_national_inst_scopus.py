#!/usr/bin/env python
# -*- coding: utf-8 -*-


##This program was building for ordering the articles affiliation in national or international autors.
##AFFILIATION   : look for https://www.scopus.com/search/form.uri?zone=TopNavBar&origin=sbrowse&display=basic
##AFFILIATION   : ook for http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&preferencesSaved=&SID=7EEKxdVddPzAYCUX3HK&excludeEventConfig=ExcludeIfReload
##Saving the files how N_AFF.csv and N_CIT.csv N be N=number of articles. 
##CITES         : look for http://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&preferencesSaved=&SID=7EEKxdVddPzAYCUX3HK&excludeEventConfig=ExcludeIfReload
##Saving the files how N_AFF.csv and N_CIT.csv N be N=number of articles. 
##Writing the number of articles with DOI in Scopus 


import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 
os.getcwd()

def parseaff(line):
    # Cleaning the line from " and text between sqare brackets [ person1 ; person2 ]  aff details 
    #print line
    if pd.isnull(line):
       return "_C1 null"
    line = re.sub('"','',line)
    line = re.sub(r'\[[^]]+?\]', '', line)
    #print "L:",line
    if ';' in line:
        affiliations = line.split(';')
    else:
        affiliations = list([line])
    clist=[]
    print "affs:",affiliations
    for aff in iter(affiliations):
        print "AFF:",aff
        # We keep the last two:
        items= aff.rsplit(',', 2)
        print items
        if len(items)<3:
            print "ERROR with:"+str(items)
            #return "Error with "+items
        #city =  ' '.join(s for s in items[1].split() if not any(c.isdigit() for c in s))
        #country = items[2].rsplit(' ',1)[1]
        print(items)
        n=len(items)
        country = ' '.join(items[n-1].split())
        print country
        #affcity = ",".join([city,country])
        #print "AFF:"+country
        clist.append(country)
    print "****",clist
    # make unique
    myset = set(clist)
    return myset
    
def parseafftot(line):
    # Cleaning the line from " and text between sqare brackets [ person1 ; person2 ]  aff details 
    #print line
    if pd.isnull(line):
       return "_C1 null"
    line = re.sub('"','',line)
    line = re.sub(r'\[[^]]+?\]', '', line)
    #print "L:",line
    if ';' in line:
	affiliations = line.split(';')
    else:
	affiliations = list([line])
    clist=[]
    print "affs:",affiliations
    for aff in iter(affiliations):
        print "AFF:",aff
        # We keep the last two:
        items= aff.rsplit(',', 2)
        print items
        if len(items)<3:
	    print "ERROR with:"+str(items)
            #return "Error with "+items
        #city =  ' '.join(s for s in items[1].split() if not any(c.isdigit() for c in s))
        #country = items[2].rsplit(' ',1)[1]
        n=len(items)
        country = ' '.join(items[n-1].split())
        #affcity = ",".join([city,country])
        #print "AFF:"+country
        clist.append(country)
    print "****"+ str(clist)
    # make unique
   
    myset=clist.count("Chile")
    print myset
    return myset

def parseinst(line):
    # Cleaning the line from " and text between sqare brackets [ person1 ; person2 ]  aff details 
    #print line
    if pd.isnull(line):
       return "_C1 null"
    line = re.sub('"','',line)
    line = re.sub(r'\[[^]]+?\]', '', line)
    #print "L:",line
    if ']' in line:
	institutions = line.split(']')
    else:
	institutions = list([line])
    ilist=[]
    #print "inst:",institutions
    for inst in iter(institutions):
        #print "INS:",inst
        # We keep the last two:
        items= inst.rsplit(',', 2)
        if len(items)<3:
	    print "ERROR with:"+items
            return "Error with "+items
        #city =  ' '.join(s for s in items[1].split() if not any(c.isdigit() for c in s))
        #country = items[2].rsplit(' ',1)[1]
        institutes = ' '.join(s for s in items[2].split() if not any(c.isdigit() for c in s))
        #affcity = ",".join([city,country])
        #print "AFF:"+country
        ilist.append(inst)
    #print "****",ilist
    
    # make unique
    myset = set(ilist)
    return myset     


df = pd.read_csv("input_table/01_scopus.csv", sep=',', index_col=["DOI"], encoding='utf-8',error_bad_lines=False)
print df
#print df["C1"].head()

df["AFF"] = df["Affiliations"].map(parseaff)
df["NAT"] = df["Affiliations"].map(parseafftot)
df["INST"]= df["Affiliations"].map(parseinst)

df_out = pd.DataFrame(df, columns = ['AFF','INST','Title','NAT'])
#print df.head()

# output: DOI + AFF, to mix with Masterlist
df_out.to_csv(str("output_table/04_ARTICLES_SAFF.csv"), sep='\t', encoding='utf-8')

# DOI article by Paulina Aldunce problem with index OR DO=(10.1080/17477891.2015.1134427)

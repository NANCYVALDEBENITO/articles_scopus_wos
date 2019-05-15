

###write out the dataframe in csv format
 

scopus    	<-read.csv("scopus.csv", sep=",", stringsAsFactors = FALSE)

authors 	<-scopus$Authors
scopus_id	<-scopus$Author.Ids
title 		<-scopus$Title
year 		<-scopus$year
journal		<-scopus$Source.title
abstract 	<-scopus$Abstract
DOI_scopus	<-scopus$DOI
volume		<-scopus$Volume
issue		<-scopus$Issue
pag1		<-scopus$Page.start
pag2		<-scopus$Page.end

wos    		<-read.table("savedrecs.csv")

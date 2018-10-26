

###write out the dataframe in csv format
 

scopus    <-  read.csv("scopus.csv", sep=",", stringsAsFactors = FALSE)


authors <-scopus$Authors
title <-scopus$Title
year <-scopus$year
journal<-scopus$Source.title
print(journal)
names(scopus)
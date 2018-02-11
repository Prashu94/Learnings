setwd("G:/extra things/Knowledge/practice/RP/datasets")
data_titanic<-read.csv("G:/extra things/Knowledge/practice/RP/datasets/titanic.csv",stringsAsFactors = FALSE)

data_titanic<-data.frame(data_titanic)
str(data_titanic)

#class VS survived, as this is not number we need to do as follows
boxplot(X~(Class+Survived),data = data_titanic)
#Age VS sex
boxplot(X~(Age+Sex),data = data_titanic)

#Create correlation matrix for mtcars and analyse which variables are linearly
#correlated and document the analysis.
library(corrgram)
cor(mtcars)
corrgram(mtcars)
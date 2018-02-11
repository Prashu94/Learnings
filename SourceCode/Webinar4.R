
library(ggplot2)
library(plyr)
library(dplyr)
library(caret)
library(moments)
library(glmnet)
library(elasticnet)
library(knitr)
library(MASS)
library(ISLR)
real_estate<- Boston
advertising_data<- Advertising
View(real_estate)
?Boston

test<-read.csv("G:/extra things/Knowledge/practice/RP/datasets/Real_Estate/test.csv",stringsAsFactors = FALSE)
train<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/Real_Estate/train.csv",stringsAsFactors = FALSE)

all_data <- rbind(select(train,MSSubClass:SaleCondition),select(test,MSSubClass:SaleCondition))

df <- rbind(data.frame(version="log(price+1)",x=log(train$SalePrice + 1)),
            data.frame(version="price",x=train$SalePrice))
View(df)

ggplot(data=df) +
  facet_wrap(~version,ncol=2,scales="free_x") +
  geom_histogram(aes(x=x))

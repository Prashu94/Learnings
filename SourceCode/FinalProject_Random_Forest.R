##################################################################
library(randomForest)
library(caTools)
library(rpart)
library(rpart.plot)
#Set the current working directory
setwd("G:/extra things/Knowledge/practice/RP/datasets")
?rpart.plot
#In the problem statement sale made is the dependent varibale
#because the ultimate aim of the retailer is tom find out whether
#he has made the sale for the product

retailer_data<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/Retail_Case_Study_Data.csv")

#have removed cutomer_id column as it is insignificant
retailer_data1<- retailer_data
#1747 obs and 11 variables
#Exploring Data
str(retailer_data)
str(retailer_data1)
summary(retailer_data1)

head(retailer_data1)
#converted Sale Made to Factor
retailer_data1$Sale.Made<- as.factor(retailer_data1$Sale.Made)

#Starting to create model
set.seed(2)

sample<- sample.split(retailer_data1$Sale.Made, SplitRatio = 0.70)
#Returns vector data of true and false
View(sample)
?split()
train_data<- subset(retailer_data1,sample= TRUE)
test_data<- subset(retailer_data1,sample= FALSE)
View(train_data) 
View(test_data)

#Random forest model
random_model<-randomForest(Sale.Made ~ .,data=train_data,importance = T)

?randomForest()
random_model

ran_pred<- predict(random_model, test_data)
View(ran_pred)

ran_pred1<- data.frame(ran_pred)

final_data_r<-cbind(retailer_data1,ran_pred1)

View(final_data_r)
write.csv(final_data,"random_forest1.csv")

#Confusion Matrix
conf_mat1<-table(test_data$Sale.Made,ran_pred)
conf_mat1

#Calculation of the accuracy percent
accuracy<- sum(conf_mat1[1,1],conf_mat1[2,2])/sum(conf_mat1)*100


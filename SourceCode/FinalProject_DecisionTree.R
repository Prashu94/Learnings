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

#Always use train_data to train a model
segment_model<- rpart(Sale.Made ~ .,data=train_data)

plot(segment_model,margin=0.1)
text(segment_model,all = TRUE, use.n = TRUE)

#Prediction can be done using pred with the test data
pred<- predict(segment_model, test_data,type = "class")
pred1<-data.frame(pred)

View(pred1)

final_data<-cbind(retailer_data1,pred1)

View(final_data)
write.csv(final_data,"decison_tree1.csv")
#Confusion Matrix is used to validation of performace of the model classified
conf_mat<-table(test_data$Sale.Made,pred)

#Calculation of the accuracy percent
accuracy<- sum(conf_mat[1,1]+conf_mat[2,2])/sum(conf_mat)*100


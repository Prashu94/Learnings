library(caTools)
library(rpart)
library(rpart.plot)
setwd("G:/extra things/Knowledge/practice/RP/datasets")
#5000 obs and 20 varibales
telecom_data<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/churn_data.csv")
str(telecom_data)
summary(telecom_data)

class(telecom_data)

names(telecom_data1)

#First Three variables are not required

telecom_data1<-telecom_data[,-c(1,2,3)]
View(telecom_data1)
class(telecom_data1)#17 variables
names(telecom_data1)

#set the seed to reproduce my sample or  it will output same output when ever the model is executed
set.seed(2)

#Sample the inout data with 70% of training data and 30% of test data
sample<- sample.split(telecom_data1$churn, SplitRatio = 0.70)
#Returns vector data of true and false
View(sample)
?split()
train_data<- subset(telecom_data1,sample= TRUE)
test_data<- subset(telecom_data1,sample= FALSE)

#Always use train_data to train a model
churn_model<- rpart(churn ~ .,data=train_data)

churn_model
plot(churn_model,margin=0.1)
text(churn_model,all = TRUE, use.n = TRUE)

#Prediction can be done using pred with the test data
pred<- predict(churn_model, test_data,type = "class")
pred1<-data.frame(pred)

View(pred1)

#Confusion Matrix is used to validation of performace of the model classified
conf_mat<-table(test_data$churn,pred)

#Calculation of the accuracy percent
accuracy<- sum(conf_mat[1,1]+conf[2,2])/sum(conf)
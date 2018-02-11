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

#1747 obs and 11 variables
#Exploring Data
str(retailer_data)

head(retailer_data)
sample<- sample.split(retailer_data$Sale.Made, SplitRatio = 0.70)

train_data<- subset(retailer_data,sample= TRUE)
test_data<- subset(retailer_data,sample= FALSE)

#Logistic Model
logit_model<- glm(Sale.Made~ .,data=train_data,family = binomial(link='logit'))
summary(logit_model)
#AIC: 1597.3

anova(logit_model, test="Chisq")

fitted.results1 <- predict(logit_model,newdata=test_data,type='response')
fitted.results1 <- ifelse(fitted.results1 > 0.5,1,0)



misClasificError1 <- mean(fitted.results1 != test_data$Sale.Made)
print(paste('Accuracy',(1-misClasificError1)*100))

##############################################################

#After seeing the result of the above we can remove some variables and create one more logistic model
logit_model_1<- glm(Sale.Made~ Months.Since.Last.Buy+Spend.Category+Visited.Website,data=train_data,family = binomial(link='logit'))
summary(logit_model_1)
#AIC:1594.7

anova(logit_model_1,test="Chisq")

fitted.results <- predict(logit_model_1,newdata=test_data,type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)

misClasificError <- mean(fitted.results != test_data$Sale.Made)
print(paste('Accuracy',(1-misClasificError)*100))

#####################################################
#ROC Curve model for logistoc regression

library(ROCR)
r_logit_model<- predict(logit_model_1, newdata = test_data,type='response')

pred_r<- prediction(r_logit_model,test_data$Sale.Made)
?performance()
#TPR-True Positive Rate #FPR- False Positive Rate
perf_r<- performance(pred_r, measure = "tpr", x.measure = "fpr")

plot(perf_r)

#Accuracy calculation
accur<- performance(pred_r,measure = "auc")
accur<- accur@y.values[[1]]
accur<-accur*100



#############################################

#As per the above analysis we find the following group of data to be 
#negligible which can be removed
#Which is done as follows, this improves the AIC.
retailer_data1<- retailer_data[!grepl("6)",retailer_data$Spend.Category),]
retailer_data1<- retailer_data1[!grepl("7)",retailer_data1$Spend.Category),]

sample_new<- sample.split(retailer_data1$Sale.Made, SplitRatio = 0.70)

train_data.new<- subset(retailer_data1,sample= TRUE)
test_data.new<- subset(retailer_data1,sample= FALSE)


logit_model_2<- glm(Sale.Made~ Months.Since.Last.Buy+Spend.Category+Visited.Website,data=train_data.new,family = binomial(link='logit'))
summary(logit_model_2)
#AIC: 1523.6

anova(logit_model_2,test="Chisq")

fitted.results.new <- predict(logit_model_2,newdata=test_data.new,type='response')
fitted.results.new <- ifelse(fitted.results.new > 0.5,1,0)

misClasificError_new <- mean(fitted.results.new != test_data.new$Sale.Made)
print(paste('Accuracy',(1-misClasificError_new)*100))

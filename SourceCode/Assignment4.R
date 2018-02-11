setwd("G:/extra things/Knowledge/practice/RP/datasets")
people_data<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/People.csv")
people_data<-data.frame(people_data)
class(people_data)
#calculate the mean of the weights for people having height more than 4.7
data_p<-people_data[people_data$Height>4.7,3]
mean(data_p,na.rm=T)
mean(people_data[people_data$Height>4.7,3],na.rm = T)
#In the above data, change the weight of Bobby to 45kgs.
people_data[2,3]<-45

#Import Cricket data from Cricinfo
library(RCurl)
data_url<- "http://decisionstats.com/2013/04/25/using-r-for-cricket-analysis-rstats-ipl/"

url_data<- getURL(data_url)


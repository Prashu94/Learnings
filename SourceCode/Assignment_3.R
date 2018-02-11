#Calculate the mean of the death of the rural female from VADeaths data set in R
data_va<- VADeaths

head(data_va)

mean(data_va[,2])

#Perform string manipulation functions for the data given above
str(data_va)
d1<-colnames(data_va)
dl<- tolower(d1)
du<-toupper(d1)

#Apply the lapply(), sapply() and tapply() functions from mtcars data set in R.
data_mt_cars<- mtcars
class(data_mt_cars)

str(data_mt_cars)

#lapply-returns a list
lapply(data_mt_cars, function(x) mean(x,na.rm=T))
#sapply()-returns a vector
sapply(data_mt_cars, function(x) mean(x,na.rm=T))
#tapply()
tapply(data_mt_cars$mpg,data_mt_cars$cyl)

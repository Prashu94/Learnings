#data directory on your computer
#G:\\extra things\\Knowledge\\practice\\RP\\datasets
#Creating a working dircetory
setwd("G:/extra things/Knowledge/practice/RP/datasets")
getwd()

#Importing dataset in R
data1<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/spss_dataset.csv")
#2466 obs and 12 variables
#first 6 rows of the data by default
head(data1)
#below 6 rows of the data by defualt
tail(data1)
#gives me the summary i.e. statistics of numeric data
summary(data1$InvoiceAmount)
#structure of the data is given by the str() function
str(data1)
#converting a varaible to date
data1$PaperlessDate<- as.Date(data1$PaperlessDate,"%m/%d/%y")
data1$InvoiceDate<- as.Date(data1$InvoiceDate,"%m/%d/%y")
data1$DueDate<- as.Date(data1$DueDate,"%m/%d/%y")
data1$SettledDate<- as.Date(data1$SettledDate,"%m/%d/%y")
#names : provides the name of the columns in the data sets
names(data1)
#dim: provides the dimensions of the data i.e no of obs and varibales in the data set
dim(data1)
#mean : displays the mean of the dataset variable
mean(data1$InvoiceAmount)
#median: diplays the median of the datasets variable
median(data1$InvoiceAmount)
#min: displays the min of the dataset variable
min(data1$InvoiceAmount)
#var: variance of the dataset variable
var(data1$InvoiceAmount)
#sd: std.deviation of the dataset variable
sd(data1$InvoiceAmount)

#Factor variables mostly contains the level data
#see the structure of the data
#levels:displays the levels of the varibales present in the data
levels(data1$PaperlessBill)
#Electronic, Paper
#table:displays the count of each level present in the data
table(data1$PaperlessBill)
#Electronic- 1203, Paper- 1263

#range:displays the diff bet min and max values
range(data1$InvoiceAmount)
#tolower:converts data to lower characters
tolower(data1$PaperlessBill)
#toupper: converts data to uppercase
toupper(data1$PaperlessBill)
#ncol: displays no. of cols in the data
ncol(data1)
#nrow: displays no. of rows in th data
nrow(data1)
#class: displays the str of the data variables
class(data1)#data.frame
class(data1$invoiceNumber)#numeric
class(data1$PaperlessDate)#Date
class(data1$InvoiceAmount)#Numeric

#Assigning th changed value to a new variable
data2<- toupper(data1$PaperlessBill)
data3<-data.frame(data2)
data4<- data.frame(data1)#backup file
write.csv(data3,"data_output.csv")
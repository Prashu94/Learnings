setwd("G:/extra things/Knowledge/practice/RP/datasets")
#import the dataset
data_man1<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/data_manipulation.csv")
data_man1$Order_Date<-as.Date(data_man1$Order_Date,'%m/%d/%y')
data_man1$Shipping_date<-as.Date(data_man1$Shipping_date,'%m/%d/%y')
summary(data_man1$jan_Sales)
summary(data_man1$feb_sales)

data_man2<-data.frame(data_man1)

str(data_man2)

#to keep specific var in data 
data_man3<-data_man2[,c(1,2,3,4,7)]

#to drop specific variable in data
data_man4<-data_man2[,-c(1,2,3,4,7)]

#to rename columns in data
colnames(data_man2)[1]<-"Order_no"

#to change names of many columns
colnames(data_man2)[c(4,8,9)]<-c("Ageing","Jan_Sales","Feb_Sales")

#Displaying rows in the data
data_man5<-data_man2[10:30,]

#To display 2,5,8 columns, 20:30 rows
data_man6<-data_man2[20:30,c(2,5,8)]

#Create a data to diplay 3,4,5 column
data_man7<-data_man2[,c(3,4,5)]

#drop 21,22 variable
data_man8<-data_man2[,-c(21,22)]

#1:20 row no.
data_man9<-data_man2[1:20,]

#1:20 row no,c(21,22) column
data_man10<-data_man2[1:20,c(21,22)]

#rename "Country" to "Count"
colnames(data_man2)[20]<-"Country"

#HOW YOU CAN CREATE NEW VARIABE FROM OLD VARIABLE IN YOUR DATA?

#Total Sales of Jan and Feb Sales add it to a new varaible in the dataframe
data_man2$TotalSales<- data_man2$Jan_Sales+data_man2$Feb_Sales

#difference between total_sales and jan_sales
data_man2$Diff1<- data_man2$TotalSales - data_man2$Jan_Sales

#How we can position your data?
data_man10<-data_man2[,c(1:9,23,10:22)]
rm(data_man10)

#total_sales>300 High sales or low sales

data_man2$sales_status<- ifelse(data_man2$TotalSales>300,"High Sales",'Low Sales')

#total_sales
data_man11<-data_man2[data_man2$TotalSales>250,]

#Using and operator in R
data_man2$sales_status1<- ifelse(data_man2$TotalSales >300 & data_man2$Profit>=100,"High Sales","Low Sales")

#Using or operator in R
data_man2$sales_status2<- ifelse(data_man2$TotalSales >300 | data_man2$Profit>=100,"High Sales","Low Sales")

#Levels present in segment variable
levels(data_man2$Segment)

#subset function in R
data_man12<- subset(data_man2, data_man2$Segment == 'Corporate')

data_man12<-data_man2[data_man2$Segment == 'Corporate',]

#using "and or" in subset

data_man13<- subset(data_man2,data_man2$Segment == "Corporate" & data_man2$TotalSales >= 300)

data_man14<- subset(data_man2,data_man2$Segment == "Corporate" | data_man2$TotalSales >= 300)

#Sorting in R
data_man15<- data_man2[order(data_man2$TotalSales),]#Ascending

data_man16<- data_man2[order(-data_man2$TotalSales),]#Descending

data_man17<- data_man2[order(data_man2$Ageing,-data_man2$Jan_Sales),]

########################################
#CaSe Study: Titanic data
#Mean of the Birth Year of the victims
########################################
#Reading text file
titanic_data<- readLines("G:/extra things/Knowledge/practice/RP/datasets/victims.txt")
titanic_data
#My way 
titanic_data1<-titanic_data[-1]
data_1_1<-data.frame(titanic_data1[c(10,1:9)])
data_2_2<-data.frame(gsub("^%","",data_1_1[1:10,]))
#grepl function 
comment<- grepl("^%",titanic_data)
comment
data_1<-titanic_data[!comment]

#accept caharter vector and a split argument tell strsplit to split the string into substring
splitlines<- strsplit(data_1,split = ",")
splitlines
?strsplit
#to c0py elemt into matrix :unlist concatenates all the vec in  alist into one large character vector
lines<-matrix(unlist(splitlines),nrow=length(splitlines),byrow=TRUE)
lines

#to create column names
colnames(lines)<-c("Name","Birth_Year","Death_Year")
colnames(lines)

#converting the matrix into data_frame
#coercion of one type to another type
data_titanic<-as.data.frame(lines,stringsAsFactors = FALSE)
str(data_titanic)
#My method to convert data to numeric
data_titanic$Birth_Year<- as.numeric(data_titanic$Birth_Year)
data_titanic$Death_Year<- as.numeric(data_titanic$Death_Year)
#Instructor's Method
tit1<- transform(data_titanic, Birth_Year=as.numeric(data_titanic$Birth_Year), Death_Year=as.numeric(data_titanic$Death_Year))
str(tit1)
View(data_titanic)

#Mean of birth year and death year
round(mean(data_titanic$Birth_Year,na.rm = T))
mean(data_titanic$Death_Year,na.rm = T)

#Data Types
#Vector-One dimensional data,homogenous data
a<-c(1,2,5,4)
class(a)
b<-c("u","s","t")
class(b)
c<-c(TRUE,TRUE,FALSE,TRUE)
class(c)
a[c(1,4)]

#Scalar-One element vector is a scalar
x<-(6)
class(x)
y<-("US")
class(y)
Z<-(FALSE)
class(Z)
#Matrix-2dimensinal homogenous data
f00<- matrix(a,nrow=2,ncol=2,byrow=TRUE)
f00[1,]
f00[,2]
f00[1,2]
#Bydefault coulmnwise entry, or byrow=TRUE for entering values rowwise


#Arrays-Multidimensional data, homogenous
#Dim: Dimension (r,c,m),row,column,matrix
array1<- array(1:20,c(2,4,3))
array1[1,,3]
#Dataframe-Tabular format,specific coulmns names present in data,
#Heterogenous data

#Lists
p1<-1:5
p2<-c(T,F,T,F)
L1<-list(p1,p2)
L1[[1]]
L1[[2]]

L5<- list(p1,p2,f00)
L5

#Merging and Appending dataset
#Appending - rbind() -Column name and datatypes should be similar
data_titanic1 <- c("Prashant",1910,1912)
data_titanic<-rbind(data_titanic,data_titanic1)
#Merging - cbind()- there must be primary key in all datasets
#var name in all datasets must be different

data_app1<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/Plasma.csv")
data_app2<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/creditdata.csv")
data_app3<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/hour_transaction.csv")
data_app4<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/all_transactions.csv")
data_app5<- read.csv("G:/extra things/Knowledge/practice/RP/datasets/Diabetes.csv")

#Append the data by rbind()
data_append<- rbind(data_app3,data_app4)

#Merging the data by cbind()-similar number of observations
data_merge<- cbind(data_app1,data_app5)
#Only the common obeservations
total<- merge(data_app2,data_app4,by = "custID")
View(total)
#All observations alongwith NA's are populated
total1<- merge(data_app2,data_app4, by = "custID", all=TRUE)
View(total1)
?merge
#if you do not know the matching columns use intersect function in by clause
#by = intersect(names(x),names(y))

#User Defined function
#In-Built function
sqrt(3*3)
square<- 3*2
sqrt(square)

b<-seq(0.5,0,-0.1)
?seq

#Reading from xlsx file
library(xlsx)# openxlsx package is very good as it does not have any dependency on java and it is fast
data_xl <- read.xlsx("G:/extra things/Knowledge/practice/RP/datasets/order.xlsx",1) 

#Reading from xml file
library(XML)
??XML
data_xml<-xmlParse("G:/extra things/Knowledge/practice/RP/datasets/Passport_data.xml")
View(data_xml)

#Reading data of spss format
library(foreign)

data_spss<- read.spss("G:/extra things/Knowledge/practice/RP/datasets/Cancer.sav")
View(data_spss)

#Web Scraping
library(RCurl)
??RCurl

data_url<- "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/old.adult.names"
data_url1<- getURL(data_url)
cat(data_url1) #display the data

#reading from database
??RODBC

library(RODBC)

ch<-odbcConnect("my_db", uid="PRASHANT", pwd="prashant")
db_products <- sqlFetch(ch,"PRODUCTS")
db_products1<- sqlQuery(ch,"select * from DBA_OBJECTS")
View(db_products1)
library(dplyr)
#Data Visualization
data_mt<- mtcars

View (data_mt)

#Barplot
counts<- table(data_mt$gear)
barplot(counts)
barplot(counts,horiz = TRUE)
barplot(counts,
        main="Simple Bar Plot",
        xlab="Improvement",
        ylab="Frequency",
        legend=rownames(counts),
        col=c("red","yellow","green"))
#Stack Bar chart
counts_1<- table(data_mt$vs,data_mt$gear)
barplot(counts_1,
        main="cars by gears and vs",
        xlab="gear",
        ylab="frequency",
        legend=rownames(counts_1),
        color= c("red","green")
        )
#GRouped Bar plot
barplot(counts_1,
        main="cars by gears and vs",
        xlab="gear",
        ylab="frequency",
        legend=rownames(counts_1),
        color= c("red","green"),
        beside = TRUE
)

#Pie Charts
slices<- c(10,12,2,16,8)
lbls<-c("US","UK","Germany","France","India")
pie(slices,labels=lbls,main="simple Pie Chart")

#Pie Charts with percentages and colors
slices_1<- c(10,12,2,16,8)
pct <- round(slices_1/sum(slices_1)*100)
#Paste function combines percentage and coutry name together
#Same like concatenation.
lbls<- paste(c("US","UK","Germany","France","India"),"",pct,'%',sep=" ")
pie(slices_1,labels = lbls, main="Percentage Pie",col = rainbow(5))

#3 Dimensional pichart
#explode function keeps the pie chart together
library(plotrix)
pie3D(slices_1,labels = lbls, main="3D Pie chart", explode = 0.0)

#Histogram
data_mt$mpg
hist(data_mt$mpg, breaks = 10, col = "blue", labels = TRUE)

#Linechart
weight<- c(2.5,2.8,3.1,3.4,5.6,5.7,5.8,6.0,8.1,8.3)
months<- seq(0,9,by = 1)

plot(months, weight, type = 'b', main = "Baby Weights by month")

#Box Plot
boxplot(data_mt$mpg ~ data_mt$cyl, col = c("Yellow","Blue","Orange"))

#Simple way to understand boxplot
vec<-c(3,2,5,6,4,1,8,2,3,4)
boxplot(vec,varwidth = TRUE)

?boxplot()

library(ggplot2)

View (iris)
data_iris<-iris

qplot(data_iris$Species, data_iris$Petal.Length, geom = "boxplot")


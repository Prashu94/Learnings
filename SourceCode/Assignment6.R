setwd("G:/extra things/Knowledge/practice/RP/datasets")
library(ggplot2)

data_mt<- mtcars
str(data_mt)
#Linegraphs
plot(data_mt$mpg,data_mt$cyl,type = "b",xlab = "Mileage",ylab = "Cylinder")
#ScatterPlot
plot(data_mt$mpg,data_mt$wt,
     main="Mileage vs Weight",
     xlab="Mileage",
     ylab="Weight",
     pch=18, col="blue")
#ScatterPlot Matrix
pairs(~mpg+disp+drat+wt,data = mtcars, main="Basic SCatterPlot Matrix")

#PieChart
pie(data_mt$mpg,main ="Pie Chart for Mileage")

#BarPlot
par(bg="blue")
counts<- table(data_mt$gear)
barplot(counts)
barplot(counts,horiz = TRUE)
barplot(counts,
        main="Simple Bar Plot",
        xlab="Improvement",
        ylab="Frequency",
        legend=rownames(counts),
        col=c("red","yellow","green"))
#Create the following histogram graphs for 
#VADeaths with suitable color palettes. You can use the RColorBrewer package

library(RColorBrewer)
#Histogram
str(VADeaths)
hist(VADeaths,col=brewer.pal(n = 5,"Set3"),main="Set3 Colors")
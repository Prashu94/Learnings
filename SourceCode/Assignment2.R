install.packages(DAAG)
library(DAAG)
?jobs

data_frame1<- jobs
View(data_frame1)
str(data_frame1)
head(data_frame1)

#Create an Alberta and BC data frame and combine it with the jobs dataset
jobs_df<-data_frame1[,c(1,2)]

#Find the month with the highest total employment across the states.
month<- c("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

sum_counts<-c()
for (i in 1:nrow(data_frame1)){
  sum_counts[i]<-sum(data_frame1[i,c(1:6)])
}

data_frame2<-cbind(sum_counts,month)
data_frame2[which.max(data_frame2[,1]),2]

#Find the months in which employment figures in Atlantic went below 950
data_frame3<-cbind(data_frame1[,6],month)
data_frame3[data_frame3[,1]< 950 ,2]

#Sort the figures for Quebec in ascending order
sort(data_frame1$Quebec)
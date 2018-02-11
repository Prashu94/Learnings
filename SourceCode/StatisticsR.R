#RLanguageEssentials

#Matrices and Arrays
x<-1:12
dim(x)<-c(3,4)#gives dimensions to variable x 3rows and 4columns
x
#bydefault byrow is flase i.e columnwise
y<-matrix(1:12,nrow = 3,byrow = T)
#Provide rownames to matrices
rownames(y)<-LETTERS[1:3]
colnames(y)<-LETTERS[1:4]

#Glue vectors columnwis or rowwise together using the cbind and rbind method
#column bind
cbind(A=1:4, B=5:8, c=9:12)
#row bind
rbind(A=1:4, B=5:8, c=9:12)

#Factors-> Practical Example
pain<- c(0,3,2,2,1)
fpain<-factor(pain,levels = 0:3)
levels(fpain)<- c("none","mild","medium","severe")
fpain
#Extracts the numeric encoding
as.numeric(fpain)

#Implicit Loops
lapply(movie_df,mean,na.rm=T)

#Exercises
#Check two vectors to be same if they contain missing values
?all
a<-c(1,2,3,NA,NA,4)
b<-c(1,2,3,NA,NA,NA,4,5)
all(is.na(a) == is.na(b)) & all((a == b)[!is.na(a)])

#If x is a factor of n levels
#and y is length n vector
#factor: 1-Dewey, 2-Huey, 3-Lousie
x1<- factor(c("Huey","Dewey","Lousie","Huey"))
y1<-c("blue","red","green")
y1[x1]

#Write a logical expression to use to extract movies with average rating >8
movie_df[movie_df$Average_Rating > 8,c("Name","Average_Rating")]

#replicate function to simulate 
#the distribution of the mean 20 
#random numbers from the exponential distribution
#by repeating the operation 10 times

sapply(1:10, function (i) mean(rexp(20)))

#Subset function 
movie_df1<- subset(movie_df$Name
                   ,movie_df$Average_Rating>8)

#transform function
movie_df2<-transform(movie_df, log.avg_rating = log(movie_df$Average_Rating))



###############################################################################
#                                                                             #  
#                  3.Probability and Statistics                               #   
#                                                                             #
###############################################################################


#pick five numbers at random from the set 1:40
sample(1:40,size = 5)
#default behaviour of sample is sampling without replacement
#sampling with replacement
sample(c("H","T"),10,replace=T)
#probabilty argument  to sumulate data with non equal probabilities
sample(c("succ","fail"),10,replace=T,prob=c(0.8,0.2))


#Probabilty calculations and combinatorics

#Discrete Distributions
#Continuous distributions
#Four fundamentals can be calculated for a statistical distributions
#density, cummulated probability, distribution function
#quantiles, pseudo random numbers


#dnorm,pnorm,qnorm,rnorm

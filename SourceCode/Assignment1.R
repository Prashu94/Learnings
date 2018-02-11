install.packages("plyr")
library(plyr)
install.packages("ggplot2")
library(ggplot2)
install.packages("RColorBrewer")
library(RColorBrewer)

A<-readline(prompt ="A = ")
A<-as.integer(A)
B<-readline(prompt ="B = ")
B<-as.integer(B)
C<-readline(prompt ="C = ")
C<-as.integer(C)

AVG<- sum(A,B,C)/3

AVG
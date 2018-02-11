#Dataframes

worms<- read.table("G:\\extra things\\Knowledge\\Practice\\RP\\datasets\\d1.csv",header=T,sep=',');
movie_d<- read.csv("G:\\extra things\\Knowledge\\Practice\\RP\\datasets\\MovieD.csv",header=T,sep=',')
#Do the following after importing the data to R
#attach,names,head,tail

attach(worms);
names(worms);
head(worms);


summary(worms);

#DataManipulation
worms[n,m]#n-rows,m-columns
worms[1,] #select all the columns of the row1
worms[-1,]#display the results by dropping the first row from the dataframe
worms[1:3,]#display rows 1 to 3 and all the columns
worms[-(1:3),]#drop rows 1:3 ad dispa=lay the columns
worms[c(1,3,5),]#display only the selected rows in the dataframe
worms[,1]#select all the rows of the specified columns
worms[,-1]#select all the rows dropping the first column
worms[,1:4]

#Aggregate functions
#by(dataframe,ColumnName,FunctionName)
#aggregate function
#both function allow summary on the basis of the factor level
worms[order(Slope),];
worms[rev(order(Slope)),];
worms[order(Vegetation,Worm.Density),];
worms[order(Vegetation,Worm.Density,Soil.pH),];#sort the rows by the specidfied columns and select all the rows
worms[order(Vegetation,Worm.Density,Soil.pH),c(4,7,3,5)];#sortthe rows by the specified columns and only show the specified columns 4,7,3,5
worms[,sapply(worms,is.numeric)]#extract columns that are numeric
worms[,sapply(worms, is.numeric)]#extract columns that are factors
#Using Logical condition to select rows from the dataframe
worms[Damp==T,]#selects all the columns where Dampness property is true for the dataframe
#select all the columns having density greater than the median density and pH factor is less than 5.2.
worms[Worm.Density >median(Worm.Density) & Soil.pH <5.2, ]
#Write a RProgram to drop middle 10 rows
worms[-(6:15),]
#Write a script to display all the rows that are not grasslands
worms[Vegetation=="Grassland",]
#Ommitting missing values
na.omit(worms)
#order and !duplicated should be used to remove pseudoreplication
new<-worms[rev(order(worms$Worm.Density)),]
new[!duplicated(new$Vegetation),]
# Complex Ordering with mixed directions
worms[order(worms$Vegetation,-worms$Worm.Density),]
#The above example sorts VEgetaion column in ascending order
#The Worm.density column in descending order
####################################################
#Tables
####################################################
#Table of counts
counts<-rpois(1000,0.6)
table(counts)
####################
#no. of genre movies
head(movie_d)
movie_df<-as.data.frame(movie_d)
#Gives the segregated format of genre as columns and movie release as rows
table(movie_df[,c(2,4)])

#tapply in action
#tapply(effective_function_Varaible,headerfunction_name)
tapply(movie_df$Average_Rating, movie_df$Length_Min,mean)
#To produce three dimensional table, it produces a stack of two-dimensional,
#tables, 
tapply(movie_df$Average_Rating,list(movie_df$Name,movie_df$Year),mean)
table(movie_df)

#Calculating tables with proportions with prop.table
counts <- matrix(c(2,2,4,3,1,4,2,0,1,5,3,3),nrow = 4)
counts
#prop.tables(counts,margin)-1-refers row total, 2 refers column totals
prop.table(counts,1)
prop.table(counts,2)
#scale function
scale(counts)
#Mathematics
#functions
#continuous distribution
#discrete distribution
#matrix algebra
#calculus
#differential equations
#Logarthmic function
#y=aln(bx)
#y = ae**bx
x<-seq(0.10,0.1)


movie_d<- read.table("G:\\extra things\\Knowledge\\Practice\\RP\\datasets\\MovieD.csv",header=T,sep=',')

summary(movie_d)
movie_d$Name
head(movie_d)

movie_d$hour<-movie_d$Length_Min/60

movie_d[,c("Name","hour")]

movie_d[,c("Name",("Length_Min")/60)]

#Numeric Operations in R
#How to create a vector or factor in R
x<-c(81,25)/60
x
#sequence of number from 1:10
c(1:10)
#reverse the order
c(10:1)
#character vector
c("Toy Story","Batman vs Superman","Guardians fo Galaxy")
#Logical vector
c(T,F)
1997>2000
movie_d[movie_d$Average_Rating>9.0,]
genre_vector<-c("Comedy","Action","Action","Animation","Crime");
genre_factor<-factor(genre_vector)
summary(genre_vector)
#gives the frequency of the vector
summary(genre_factor)
#There ar two type of categorical variable
#Nomainal Categorical Variable
#Ordinal Variables- Order
movielength_vector<-c("Very short","Short","Medium","Short","Long","Very short","Very Long")
movielength_factor<-factor(movielength_vector,ordered=TRUE,levels=c("Very short","Short","Medium","Long","Very Long"))
#In the above example we set the order of the factor to be true
#the levels defined in the vector shows the order that we want to specify


##########################
#Vector Operation
###########################
year<-c(1995,1996,2010,2016)
names(year)<-c("The Breakfast Club","American Beauty","Black Swan","Chicago")
year["Black Swan"]

length(year)
sort(year)#Deafult ascending

#To find the smallest number
min(year)
#to find the largest number
max(year)

#caverage cost of movies in million
cost<-c(8.6,8.1,8.5)
cost<-rev(sort(cost))
cost
#functions that can be used in R
sum(cost)/3
mean(cost)
summary(cost)
cost[2]
cost[c(2,3)]
cost[1:3]

titles<-c("The Dark Knight", "Batman vs superman", "The Sucide Squad","Wonder Woman")
titles[-1]#removes the first element from the vector defined
titles[6]

cost[cost>8.1]

#Dealing with missing values
age_metric<-c(14,12,NA,8,NA)
#An important thing to remember about vectors is that all arithmetic operations 
#are perfomed element wise

sequences<-c(2,3,4,5,6)

multiply<-age_metric * sequences

multiply


##########Data Structures in R#############
#Arrays in R
movie_vector<-as.vector(movie_d$Name)
movie_name_array<-array(movie_vector,c(4,3))
movie_name_array[1,]#Names the first row
movie_name_array[,2]#Names the column 2
#Matrices in R
movie_name_mat<-matrix(movie_vector,nrow=4,ncol=4)
#The above example gives a warning of the rows and columns bigger than the available elements
movie_name_mat<-matrix(movie_vector,nrow=2,ncol=3)
movie_name_mat[1:2,1:2]#1:2 rows, 1:2 columns
#Lists in R
movie_list<-list("Toy Story",1995,c("Animation","Adventure","Comedy"))
movie_list
#give the second elemet in the list
movie_list[2]
#give the lement betn 2nd and 3rd in the list
movie_list[2:3]
#Creating a named list
movie_list1<-list(name="Batman vs Superman",
                  year=2016,
                  genre=c("Action","Drama","Adventure"))
movie_list1
#access the element of the list using the $sign
movie_list1$genre
movie_list["age"]<-NULL
#DataFrames in R
movie_data_frame<-data.frame(name=as.vector(movie_d$Name),
                             year=as.vector(movie_d$Year))
#Both Below examples provide the same result
movie_data_frame$name
movie_data_frame[,1]
#specific elements
movie_data_frame[1,2]
#Structure information of dataframe is given by
str(movie_data_frame)
#Adding a new column 
movie_data_frame['Length_min']<-as.vector(movie_d$Length_Min)
#Adding a new row to the dataframe
movie_data_frame<-rbind(movie_data_frame,c(name='Aquaman',year=2018,Length_min=200))
#Removing element from the data frame
movie_data_frame<-movie_data_frame[-c(6,7),]
#Conditions and Loops
#name the movie greater than 2010 
if(movie_d$Year>2010){
  print(movie_d$Name)
}
#Operators in R
Movie_year=1997
if(Movie_year <2000 & Movie_year > 1990){
  print('Movie Year between 1990 and 2000')
}
if(Movie_year >2010 | Movie_year <2000) {
  print('Movie year not between 2000 and 2010')
}
#Subset in R
#Sometimes we do not want the whole dataset, but we need only a subset of the data
decade='recent'
if (decade=='recent'){
  subset(movie_d,Year >=2000)
}else{
  subset(movie_d,Year < 2000)
}
#Loops in R#
#For Loop usage in R

years<-movie_d['Year']

for (val in years){
  print(val)
}

#While loop in R
iteration=1

while(iteration <= 5){
  print(c('This iteration number:', as.character(iteration)))
  print(movie_d[iteration,]$Name)
  iteration=iteration+1
}

######Apply functions to vectors#########
#First create a vector
my_list<-c(10:22)
my_list+2
my_list**2
###################################################################
#Functions in R
###################################################################
#There are two types of functions:
#Pre-Defined functions
#User-Defined Functions
###################################################################
ratings<-as.vector(movie_d$Average_Rating)
#in built function use in below example
mean(ratings)
sort(ratings,decreasing=T)
#User Defined functions
#Write a program by creting a user defined function in R
printHelloWorld<-function(){
  print("Hello World")
}

printHelloWorld()

#Write a program to add two numbers using an add function
add<-function(x,y){
  print(x+y)
}

add(2,3)

#Explicitly returning outputs in user defined functions
add<-function(x,y){
  return(x+y)
}

print(add(2,3))

#Using if/else function in user defined function
is_good_rating<-function(rating){
  if (rating < 7){
    print("NO")
  }else{
    print("YES")
  }
}
is_good_rating(movie_d[movie_d$Name=='Star Wars',]$Average_Rating,threshold=8)
#Setting default arguments in user-defined functions
is_good_rating<-function(rating,threshold=7){
  if (rating < threshold){
    print("NO")
  }else{
    print("YES")
  }
}

#Using functions within functions
#Create a function that can help us decide on which movie to watch 
#based on its average rating
#the function return NO if the movie rating is below 7 and yes otherwise
watchMovie<-function(movie_name,my_threshold){
  rating<-movie_d[movie_d[,1]==movie_name,"Average_Rating"]
  is_good_rating(rating,my_threshold)
}
is_good_rating<-function(rating,threshold=7){
  if (rating < threshold){
    print("NO")
  }else{
    print("YES")
  }
}
watchMovie("Batman vs Superman",8)

#R Object and classes#

movie_rating<-as.vector(movie_d$Average_Rating)
movie_rating
#class of movie_rating object
class(movie_rating)#Numeric
#Numeric Class
average_rating<-8.5
class(average_rating)
#Character Class
movies<-as.vector(movie_d$Name)
class(movies)
#Combined values in objects
combined<-c(movies,movie_rating)
combined
class(combined)#Character -Numbers type casted into chracter
#Integer object and class
age_restriction<-as.vector(movie_d$Age_Restriction)
class(age_restriction)
#Difference between class and mode
#For a simple vector the class and mode are the same,
#but in some other objects like arrays, matrix, dataframe, and list,
#class and mode means different things
#in such cases the matric object class will be shown as matrix
#and the mode will be shown as character/integer,numeric,logical as per the values in the matrix
mode(movie_d)#the mode of the data frame is list
class(movie_d)#Data Frame
#Debugging
#Error cathcing in R
for (i in 1:3){
  print('a'+10)
}#Error in expression : non-numeric argument to binary operator
tryCatch(10+10)#no error
#Error handling with error function printing message
tryCatch('a'+10,error= function(e) print("Oops something went wrong"))
###############Working with data in R#########################

#Accessing built in data sets of R
data()
help(CO2)
#Strings and dates in R
#String manipulations in R
summary<-readLines("G:\\extra things\\Knowledge\\practice\\RP\\datasets\\BvS.txt")
summary
length(summary)#Gives the length of the string vector
#finding the size of the file
file.size("G:\\extra things\\Knowledge\\practice\\RP\\datasets\\BvS.txt")
#Output: 2277
#using scan function
my_data1<-scan("G:\\extra things\\Knowledge\\practice\\RP\\datasets\\BvS.txt"," ")
my_data1
length(my_data1)
#String operations
#nchar() -will return the toal no. of characters in the given string
nchar(summary[1])
toupper(summary[1])
#chartr() - used to replace characters in the string given
#takes three paratmeters find dtring,replace string, original string
chartr(" ","-",summary[1])
#strsplit()- splits the givcen string by word
character_list<- strsplit(summary[1]," ")
word_list<- unlist(character_list)
word_list

#sorting the list
sorted_list<- sort(word_list)
sorted_list

#paste()- used for concatentaing 3 strings in R
paste(sorted_list, collapse = " ")

#substr()- used to get the sub section of the string in R
sub_string<- substr(summary[1],start=4,stop=50)
sub_string
#removing default trailing spaces from the output ogf the substring function
trimws(sub_string)

#str_sub()- To read the string from the last we use the stringr library
install.packages(stringr)
library(stringr)
str_sub(summary[1],-8.-1)
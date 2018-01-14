S='Spam'
#String object
#Note that string objects are immutable
#You can use expression to change the value of a string
#Below statements prints the varibale value onto the screen.

print("The string is :" + S)

#Print The last element of the string
print("The last element of the string :"+ S[-1])

#Print the second last element of the string
print("The second last element of the string :" +S[-2])

#Print the first element of the string
print("The first element of the string :" +S[0])

#Print the elements except the first character
print("The elements except the first character :" +S[1:])

#Print the elements of the string except the last character
print("The elements of the string except the last character :" +S[:-1])

#Expand the string into a list
S='Shruberry'

#Declaring a list below
L=list(S)

#Displaying the elements of the list, i.e the string is broken into comma seperated values
print("The List:")
print(L)

#Replacing the index positon 1,3 of the list
L[1]='t'
L[3]='a'
S1='wberry'
#L1=list(S1)
L[0:4].extend(S1)
#Printing the modified list
print("The modified List:")
print(L)




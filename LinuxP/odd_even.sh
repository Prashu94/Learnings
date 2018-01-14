echo "Enter a number:"
read p
# if ! (( p % 2))
if  [[ $(( p % 2 )) == 0 ]];
then 
	echo "The number entered is even"
else
	echo "The number entered is odd"
fi


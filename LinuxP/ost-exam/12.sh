val1=10
val2=20
if [ $val1-gt5 ]
then
	echo "the value1 $val1 is greater than 5"
elif [ $val2-gt5 ]
then
	echo "the second value $val2 is greater than 5" 
else
	echo "program finished"
fi

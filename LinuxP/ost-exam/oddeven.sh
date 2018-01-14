#prime number
echo "The integer number you entered is:" $1
i=$[ $1 % 2 ]
if [ $i -eq 0 ]
then 
echo "The no. you entered is even"
else
echo "the no. you entered is odd"
fi

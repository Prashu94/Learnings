echo "Enter a four digit no"
read n
while [ $n -gt 0 ]
do
m=`expr $n % 10 `
n=`expr $n / 10 `
echo "the digits are:"$m
done 
/*
Output:
Enter a four digit no
4567
the digits are:7
the digits are:6
the digits are:5
the digits are:4
*/

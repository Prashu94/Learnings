clear
echo "The year given is:"$1
a=`expr $1 % 4`
b=`expr $1 % 100`
c=`expr $1 % 400`
if [ $a -eq 0 -a $b -ne 0 -o $c -eq 0 ]
then
echo "The year $1 is a leap year"
else
echo "the year $1 is not a leap year"
fi

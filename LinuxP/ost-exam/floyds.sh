clear
a=1
echo "The no. of rows entered is:$1"
for (( i=1 ; i <= $1 ; i++ ))
do
for (( j=1 ; j <= $i ;j++ ))
do
echo -n "$a"
a=`expr $a + 1`
done
echo " "
done

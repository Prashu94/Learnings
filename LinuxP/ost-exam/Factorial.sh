#Factorial
clear
fact=1
i=1
echo -n "$1!="
while [ $i -le $1 ]
do
fact=`expr $fact \* $i`
i=`expr $i + 1`
done
echo -n "$fact "
echo " "

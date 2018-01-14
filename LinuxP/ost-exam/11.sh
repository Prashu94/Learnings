clear
echo " enter the decimal number"
read b
bin=0
while [ $b -ne 0 ]
do
r=`expr $b%2|bc`
b=`expr $b/2|bc`
bin=$r$bin
done
bin=`expr $bin/10|bc`
echo $bin

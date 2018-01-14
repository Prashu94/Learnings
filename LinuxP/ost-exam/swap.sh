echo Enter valuefor a:
read a
echo Enter valuefor b:
read b
clear
echo Values of variables before swaping
echo A=$a
echo B=$b
echo Values of variables after swaping
a=`expr $a + $b`
b=`expr $a - $b`
a=`expr $a - $b`
echo A=$a
echo B=$b

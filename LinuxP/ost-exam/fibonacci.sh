clear
echo "$1 fibonacci nos. will be printed "
x=0
y=1
i=2
echo " The $1 fibonacci nos. generated are :"
echo -n "$x"
echo -n "$y"
while test $i -le $1 
do
i= $i+1
z= $[ $x + $y ]
echo -n "$z"
x=$y
y=$z
done
echo " "

clear
echo "The two integers are:"$1 "," $2
a=$1
b=$2
while [ $b -ne 0 ]
do
t=$b
b=`expr $a % $b`
a=$t
done
gcd=$a
p=`expr $1 \* $2 `
lcm=`expr $p / $gcd`
echo "GCD :" $gcd
echo "LCM :" $lcm 

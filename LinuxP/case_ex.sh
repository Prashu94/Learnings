echo "
1.Addition
2.Subtraction
3.Multiplication
4.Divide"

echo "Enter the option:"

read p

echo "Enter first number:"

read a

echo "Enter second number:"

read b

case $p in
1) c=$(( $a + $b ))
echo "Addition:" $c;;
2) d=$(( $a -$b ))
echo "Subtraction:" $c;;
3) e=$(( $a * $b ))
echo "Multiplication:" $c;;
4) f=$(( $a / $b ))
echo "Division:" $c;;
esac


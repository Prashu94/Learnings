#add sub mult div
clear
echo "The two nos. entered by you are:" $1 "," $2
echo "1.ADD 2.SUBTRACT 3.MULTIPLY 4.DIVIDE"
echo " "
read ch
case $ch in
1) a=$[ $1 + $2 ]
echo "The add result is :" $a;;
2) s=$[ $1 - $2 ]
echo "The subtract result is :" $s;;
3) m=$[ $1 * $2 ]
echo "The multiplied result is:" $m;;
4) d=$[ $1 / $2 ]
echo "The divided result is :" $d;;
esac

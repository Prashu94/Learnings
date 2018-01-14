 clear
echo enter the size of array...
read s
echo enter the elements of array
for ((i=0; $i<$s; i++))
do
            read a[$i]
done
j=`expr $s - 1`
for ((i=0; $i<$j; i++))
do
            temp=${a[$i]}
            a[$i]=${a[$j]}
            a[$j]=$temp
            j=`expr $j - 1` 
done

echo The reverse array is
for ((i=0; $i<$s; i++))
do
echo ${a[$i]}
done

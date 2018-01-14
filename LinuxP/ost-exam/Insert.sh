echo "Enter the size of array :"
read n
echo "Enter Element in the array :"
for (( i=0 ; i < n ; i++ ))
do
read arr[$i]
done
echo "Enter the element position you want to enter:"
read p
echo "Enter the value you want to enter:"
read v
for (( c= $n - 1; c >= p - 1; c-- ))
do
arr[ `expr $c + 1` ] = ${array[ $c ]};
done

array[ `expr $p - 1` ] = $v;

echo "The inserted Elements are:"
for (( i=0 ; i <= n ; i++ ))
do
echo ${arr[$i]}
done

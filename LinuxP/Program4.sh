read n
sum=0
for ((i=0;i<$n;i++))
do
    read temp
    sum=$(awk "BEGIN {print $sum+$temp; exit}")
done
printf "%.3f\n" $(bc -l <<< "$sum/$n")

read var1
printf "%.3f" $(echo "scale = 4; $var1" | bc)

read var2
printf "%.3f" $(echo "scale = 4; $var1" |bc)

read var3
printf "%.3f" $(echo "scale = 4; $var3" | bc)



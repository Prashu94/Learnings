#String concatenate
echo "Enter String 1 "
read st1
echo "Enter String 2"
read st2
printf "Original Strings are :\n$st1\n$st2\n"

st1="$st1""$st2"
echo "String after concatenating : "$st1



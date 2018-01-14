#String reverse
echo "Enter String "
read var

copy=${var}
echo "data of variable copy : $copy"
len=${#copy}
for((i=$len-1;i>=0;i--)); 
do 
	rev="$rev${copy:$i:1}"; #Comment Copy variables ith location 1st part 
done

echo "var: $var, rev: $rev"



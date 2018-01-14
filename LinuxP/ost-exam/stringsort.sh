#String space removal
echo "Enter String "
read var

echo $var | sed -e s/[ ]//gI

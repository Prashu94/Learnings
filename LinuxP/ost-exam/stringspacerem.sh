#String space removal
echo "Enter String "
read var

echo $var | tr -d ' ' #spaces in between
#echo " test test test " | sed 's/ *$//' #Trailing Spaces 
#echo " test test test " | sed 's/^ *//' #Leading Spaces

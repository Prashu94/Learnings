#String vowel removal
echo "Enter String "
read var

echo $var | sed -e s/[aeIou]//gI

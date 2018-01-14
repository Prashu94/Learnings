clear
echo " The character entered by you is :" $1
if [  "$1" == "a"  -o  "$1" == "e"  -o  "$1" == "i" -o  "$1" == "o" -o  "$1" == "u" -o  "$1" == "A" -o  "$1" == "E" -o  "$1" == "I" -o  "$1" == "O" -o  "$1" == "U"  ]
then 
echo "The character $1 is a vowel "
else 
echo "The character $1 is a consonant "
fi
# Program for only one input character 

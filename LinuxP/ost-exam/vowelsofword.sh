read word
v=`echo $word | tr -cd 'aeiou' | wc -c`
c=`echo $word | tr -cd 'bcdfghjklmnpqrstvwxyz' | wc -c`
echo "vowels = $v"
echo "consonants = $c"

#This program is for counting vowels of whole word

#String word swap
echo "Enter Original String "
read var

echo "Enter word to replace "
read word

echo "Enter word to replace with "
read replace

result_string="${var//$word/$replace}"

echo $result_string


#original_string='i love Suzi and Marry'
#string_to_replace_Suzi_with=Sara
#result_string="${original_string/Suzi/$string_to_replace_Suzi_with}"



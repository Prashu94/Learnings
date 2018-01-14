clear
 echo " Type any number "
 read number

 length=`echo $number | wc -c `
 reverse=0
 
 while [ $length -gt 1 ]
 do
   length=`expr $length - 1 `
   d=`echo $number|cut -c $length `
   reverse=`expr $reverse \* 10 + $d `
 done

 echo "Reverse of the entered number is : $reverse"

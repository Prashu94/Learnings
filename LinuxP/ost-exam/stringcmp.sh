#String compare
echo "Enter String 1"
read st1
echo "Enter String 2"
read st2
if(("$st1" == "$st2"))
	then
		echo "String matched"
	else
		echo "Strings does not match"
fi


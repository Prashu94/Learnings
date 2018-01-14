#!/bin/bash

read -p "Enter something: " char
if [[ "$char" == *[AEIOUaeiou]* ]]; then
	echo "Vowel"
else
	echo "Constant"
fi

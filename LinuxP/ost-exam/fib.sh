clear
  echo "How many number of terms to be generated ?"
  read n
  x=0
  y=1
  i=2
  echo "Fibonacci Series up to $n terms :"
  echo -n "$x"
  echo -n " "
  echo -n "$y"
  while [ $i -lt $n ]
  do
      i=`expr $i + 1 `
      z=`expr $x + $y `
      echo -n " "
      echo -n "$z"
      x=$y
      y=$z
  done
  echo -n " "

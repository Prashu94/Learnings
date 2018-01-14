l==5;
for((i=0;i<$l;i++));
do eval "a$i=($(pv=1;v=1;for((j=0;j<$l-$i;j++));
do [ $i -eq 0 -o $j -eq 0 ]&&{ v=1 && pv=1; }||v=$((pv+a$((i-1))[$((j))]));echo -n "$v ";pv=$v;done;));";
eval echo "$(for((k=0;k<=$i;k++)); do eval "echo -n \"\$((a\$((i-k))[k])) \""; done)";
done;

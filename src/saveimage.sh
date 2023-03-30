d1=D`echo $[ $RANDOM % 5 + 1 ]`
d2=D`echo $[ $RANDOM % 5 + 1 ]`
d3=D`echo $[ $RANDOM % 5 + 1 ]`
FSD=$FS/$d1/$d2/$d3
mkdir -p $FSD 
name=`echo $1 | awk -F/ '{print $(NF);}'`
curl $1 -o $FSD/$name

#!/bin/dash

if [ "$#" -ne 1 ] || ! [ "$1" -eq "$1" ] 2>/dev/null || [ "$1" -le 0 ]
then
	echo "Usage: $0 <positive-integer>"
	exit 2
fi 


num="$1"

if [ "$num" -eq 1 ]; then
	echo "1 is not prime"
	exit 1
fi

i=2

while [ $((i * i)) -le "$num" ]; do
	if [ $((num % i)) -eq 0 ]; then
		echo "$num is not prime"
		exit 1	
	fi
	i=$((i + 1))
done

echo "$num is prime"
exit 0

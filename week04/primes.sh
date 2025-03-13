#!/bin/bash

# error checking: 1 arg, int, +ve


num="$1"
i=2

while test "$i" -le "$num"
do
	if ./is_prime.sh "$i" >/dev/null
	then
		echo "$i"
	fi
	i=$((i+1))
done

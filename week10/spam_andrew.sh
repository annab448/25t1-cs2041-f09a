#!/bin/dash
dir="$HOME/comp1521"

for c_file in $(find "$dir" -type f -name "*.c")
do
    echo "mutt -s 'C for AndrewT' -a $c_file -- andrewt@not_his_real_email.com"
done


find "$dir" -type f -name "*.c" |
while read line; do
    echo "mutt -s 'C for AndrewT' -a $c_file -- andrewt@not_his_real_email.com"
done
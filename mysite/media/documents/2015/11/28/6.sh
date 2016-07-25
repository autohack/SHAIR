#!/bin/sh

while read line
do
	abc=$(echo $line | awk -F# '{for (i = 1; i <= NF; i++) print $i " "; print ""}')
	data=();
	count=0
	for word in $abc
	do
		data=("${data[@]}" "$word")
	done

	mbasic=0
	for (( i = 3; i < 17; i++ )); do
		mbasic=`expr $mbasic + ${data[$i]}`
	done

	basic=0
	for (( i = 17; i < 27; i++ )); do
		basic=`expr $basic + ${data[$i]}`
	done

	adv=0
	for (( i = 27; i < 37; i++ )); do
		adv=`expr $adv + ${data[$i]}`
	done

	bvim=0
	for (( i = 37; i < 50; i++ )); do
		bvim=`expr $bvim + ${data[$i]}`
	done

	avim=0
	for (( i = 50; i < 59; i++ )); do
		avim=`expr $avim + ${data[$i]}`
	done

	echo "Evaluation for ${data[0]} ${data[1]}: ${data[2]}"

	echo -n "Part"
	echo -n -e " \t\t\t\t\t"
	echo -n "Correct Answers"
	echo -n -e " \t"
	echo "Marks obtained"

	echo -n "Most basic Commands"
	echo -n -e " \t\t\t\t"
	echo -n "$mbasic"
	echo -n -e " \t\t"
	echo "$mbasic"

	echo -n "Basic Linux Commands"
	echo -n -e " \t\t\t\t"
	echo -n "$basic"
	echo -n -e " \t\t"
	echo `expr $basic \* 2`

	echo -n "Advanced Linux Commands"
	echo -n -e " \t\t\t"
	echo -n "$adv"
	echo -n -e " \t\t"
	echo `expr $adv \* 3`

	echo -n "Basic VIM Commands. Use vim not vi."
	echo -n -e " \t\t"
	echo -n "$bvim"
	echo -n -e " \t\t"
	echo "$bvim"

	echo -n "Advanced VIM"
	echo -n -e " \t\t\t\t\t"
	echo -n "$avim"
	echo -n -e " \t\t"
	echo `expr $avim \* 3`

	echo -n "Total"
	echo -n -e " \t\t\t\t\t\t"
	echo -n `expr $mbasic + $basic + $adv + $bvim + $avim`
	echo -n -e " \t\t"
	echo `expr $mbasic + $basic \* 2 + $adv \* 3 + $bvim + $avim \* 3`

	echo

done < marks.csv
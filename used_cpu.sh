#!/bin/bash
while true
do
	D=$(date +'%Y-%m-%d_%H')
	DN=$(date +'%Y-%m-%d')
	echo -e `date +'%F %T'`'\t' `top | head -n3 | tail -n1 | tr -d ',' | awk '{print $2+$4}'` >> cpu_util_$D.txt
	find cpu_util_* > file.txt | sed 's/ /\n/g'
	while read- r line; do
		Time=$(echo $line | head -c 22 | tail -c 13)
		DP=$(echo $line | head -c 19 | tail -c 10)
		diff=$(($(($(date -d $DN +%s) - $(date -d $DP +%s)))/3600))
		if [ $diff -ge 168 ]; then
			rm $line
		else
			if [ $Time != $D ]; then
				gzip -q $line
			fi
		fi
	done
	rm file.txt
	sleep 5
done

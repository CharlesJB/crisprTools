#!/bin/bash

tags[0]="CGATGT"
tags[1]="GCCAAT"
tags[2]="TGACCA"
tags[3]="OTHER"
names[0]="Fragmented"
names[1]="rRNA-Fragmented"
names[2]="Terminator-Fragmented"
names[3]="Other"
times[0]="0"
times[1]="i15"
times[2]="i45"
times[3]="U15"
times[4]="U45"

source scripts/extractTools

index=0
for tag in ${tags[@]}
do
	for time in ${times[@]}
	do
		formatTime="_"$time"_"
		dir=$(ls | grep $formatTime | grep $tag)
		dir="$dir/Depths/"
		for file in $(ls $dir | grep pth.tsv | grep "ST\|YP")
		do
			ID=$(getGeneID $file)
			name=$(getGeneName $ID) 	
			count=$(fetchCountST $ID $time $tag)
			out=$time"_"$tag.out
			echo -e "$name\t$ID\t$count" >> $out
			#echo "tag: $tag  time: $time  file: $file"
		done	
	done
done
wait

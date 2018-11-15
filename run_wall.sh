#!/bin/bash

tvservice=/opt/vc/bin/tvservice

mkdir -p /tmp/wall

album_ids=( `grep $1 albums.txt | awk '{print $1}'` )

$tvservice -p

photo_idx=1

for album in ${album_ids[*]}
do
    title=`grep $album albums.txt | awk -F ',' '{print $2}'`
    echo $title
    photos=( `cat albums/$album` )

    for photo in ${photos[*]}
    do
	if [[ $photo_idx -eq "1" ]]; then
	    wget -q $photo -O /tmp/wall/$photo_idx.jpg
	    let "photo_idx=$photo_idx+1"
	fi
	wait
	fbi -a --noverbose -T 1 -t 5 -1 /tmp/wall/$photo_idx.jpg 
	
	wget -q $photo -O /tmp/wall/$photo_idx.jpg
	if [[ $photo_idx -gt "10" ]]; then
	    let "photo_idx=1"
	else
	    let "photo_idx=$photo_idx+1"
	fi
    done

done

$tvservice -o


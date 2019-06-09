#!/bin/bash

rm Total.mp4; files='*.mp4'; for i in $files; do
echo " -cat " "'"$i"'" >>input.txt; done

file="input.txt"; name=$(cat "$file"); 

eval "MP4Box " $name " -new Total.mp4";

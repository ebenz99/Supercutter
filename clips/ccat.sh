#!/bin/bash

rm mylist.txt

for i in *.mp4; do echo file $i >> mylist.txt; done

ffmpeg -f concat -i mylist.txt -c copy output.mp4

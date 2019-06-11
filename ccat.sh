#!/bin/bash

rm video/output.mp4

for i in clips/*.mp4; do echo file $i >> mylist.txt; done

ffmpeg -f concat -i mylist.txt -c copy video/output.mp4

rm mylist.txt
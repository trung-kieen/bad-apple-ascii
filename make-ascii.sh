#!/bin/bash
# Author: Nguyen Khac Trung Kien
mkdir -p frames-bad-apple
ffmpeg -i bad_apple.mp4 -vf fps=30 frames-bad-apple/out%04d.jpg

rm  frame-ascii/*
mkdir -p frames-ascii
for file in $PWD/frames-bad-apple/*;
do
#  echo $file
#  ascii-image-converter $file 
  filename=$(basename "$file")
  echo $filename
  ascii-image-converter  $file >  frames-ascii/$filename.txt
done


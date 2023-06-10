#!/bin/bash
# Author: Nguyen Khac Trung Kien

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
echo "The directory of the currently executing script is: ${SCRIPT_DIR}"

if [ "$1" ]; then
  speed=$1
else
  speed=1.0
fi

mpv --no-video --audio-device=alsa  bad_apple.mp4 > /dev/null 2>&1 &
dir="$SCRIPT_DIR/frames-ascii" 

for filename in $(ls -v "$dir"); do
#    clear
    file="$dir/$filename"
    if [ -f "$file" ]; then
        cat "$file"
    fi

#    sleep $((0.02 / $speed))
    sleep 0.024


done


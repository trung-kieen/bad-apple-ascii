#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from time import sleep
import subprocess
import threading

speed = 1.0
videos = [
    "bad_apple.mp4",
    # Add more video filenames here
]

def main():
    if len(sys.argv) > 1:
        speed = float(sys.argv[1])
    else:
        speed = 1.0
    output_thread = threading.Thread(target=display_output)
    output_thread.start()

    audio_threads = []
    for video in videos:
        audio_thread = threading.Thread(target=play_audio, args=(video,))
        audio_threads.append(audio_thread)
        audio_thread.start()

    # Wait for all audio threads to finish
    for audio_thread in audio_threads:
        audio_thread.join()

    output_thread.join()

def play_audio(video):
    command = ["mpv", "--no-video", "--audio-device=alsa" , f"--speed={speed}", video]
    # subprocess.run(command)
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def display_output():
    # Your code for displaying output in the console
    dir = "frames-ascii"
    for filename in sorted(os.listdir(dir)):
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            with open(f, 'r') as file:
                print(file.read())
        sleep(0.024 / speed)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()

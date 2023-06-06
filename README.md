# Bad Apple For Terminal

This repository contains a set of scripts to convert the "Bad Apple" video into ASCII art representation and display it on terminal for linux.
Do the optional mark if you want to make ascii frames for other video.
## Prerequisites

Before running the scripts, please ensure that you have the following dependencies installed on your system:

- [FFmpeg (Optional)](https://ffmpeg.org/): A powerful multimedia framework that can handle video and audio conversion.
- [Python](https://www.python.org/) (version 3.x): An interpreted, high-level programming language.
- [mpv](https://mpv.io/): A media player that will be used to play the ASCII art video.
- [ascii-image-converter (Optional)](https://github.com/TheZoraiz/ascii-image-converter): Convert image to ascii text file.

## Usage

### 1. Converting the Video to ASCII Text (Optional)

To convert the "Bad Apple" video (`bad_apple.mp4`) into ASCII art and save it into `frames-ascii` folder, run the following command:

```bash
$ ./make-ascii.sh
```

### 2. Running the ASCII Art

#### Running from Python

To display the ASCII art directly from a Python script, you can use the `run.py` script. Run the following command:

```bash
$ python run.py
```

#### Running on Terminal

To display the ASCII art directly in the terminal. Run the following command:

```bash
./run.sh
```

## Acknowledgments

This project is inspired by the "Bad Apple" meme and the generation idea from the video tutorial [here](https://www.youtube.com/watch?v=B49nQu4L2O4)

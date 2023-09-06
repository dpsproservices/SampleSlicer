# SampleSlicer
Use the open source python pydub with ffmpeg to process a directory or folder full of raw recordings
and slice them into seperated individual 16bit stereo .wav files
in a second folder.

TO DO: 

Normalize all the .wav files in the second folder into a third folder for further processing.
Peak volume in decibels to 0 dB by default

# Install dependencies
1. Install homebrew

2. Install python or conda or miniconda

This code repo was made using python 3 and MS Visual Studio Code

3. Install ffmpeg with brew

4. Install PyDub with pip3

# Setup raw recording files and folders

Copy paste or move all your raw recordings into a folder.
Create the secomnd folder where the sliced sample files will be output into.

# How to run

python slicer.py raw-recordings-folder sliced-samples-folder

raw-recordings-folder is the first folder where the raw recordings are placed

sliced-samples-folder is the second output folder where the sliced .wav files will be output

# References

Homebrew

https://brew.sh/

ffmpeg

https://ffmpeg.org/

PyDub

https://github.com/jiaaro/pydub

How to split an mp3 file by detecting silent parts?

https://askubuntu.com/questions/1264779/how-to-split-an-mp3-file-by-detecting-silent-parts

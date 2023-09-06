# SampleSlicer
Use the open source python pydub to process a directory or folder full of raw recordings
and slice them into seperated individual 16bit stereo .wav files
in a 2nd folder.
Then normalize all those wave files in the 2nd folder into a 3rd folder
for further processing.

# Setup
Install ffmpeg with brew

Then install PyDub with pip

# Run

Copy or move all the raw recordings into the folder specified in globals.py
Create the 2nd and 3rd folders specified in glboals.py where the files will be output

python slicer.py

# References
-------------------------

ffmpeg

https://ffmpeg.org/

PyDub

https://github.com/jiaaro/pydub

How to split an mp3 file by detecting silent parts?

https://askubuntu.com/questions/1264779/how-to-split-an-mp3-file-by-detecting-silent-parts


License (MIT License)
Copyright © 2023 Joseph Skarulis, https://dpsproservices.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



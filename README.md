# SampleSlicer
Use the open source python pydub with ffmpeg to process a directory or folder full of raw recordings
and slice them into seperated individual 16 bit stereo .wav files
in a second folder.

Normalize all the .wav files in the second folder for further processing.
Peak volume in decibels to 0 dB by default

# Install dependencies

1. Install homebrew

2. Install python or conda or miniconda

This code repo was made using python 3 and MS Visual Studio Code

3. Install ffmpeg with brew

4. Install PyDub with pip3

5. Install ffmpeg-normalize with pip3

# Setup raw recording files and folders

I recommend install "Dolby On" app on your phone, it stores audio recordings as .m4a files which can be 
AirDrop to you computer.  It's quality is more than good enough for fun with sampling and sound design.

Copy paste or move all your raw recordings into a folder: .m4a, .wav, .mp3, .mp4
Create the second folder where the sliced sample files will be output into.

# How to run

To slice samples only, specify the -i and -o arguments, ignore the -n , -l, -p arguments.

example:
python slicer.py -i raw-recordings-folder -o sliced-samples-folder

To slice and normalize, specify the -n output folder, with -l, -p optional.

example:
python slicer.py -i raw-recordings-folder -o sliced-samples-folder -n normalized-samples-folder

# Options

The -i command line option is the raw-recordings-folder the first input folder where the raw recordings are placed

The -o command line option is the sliced-samples-folder the second output folder where the sliced .wav files will be output

The optional -t command line argument is the silence detection threshold which is set default to -40 dB
Setting this to -24 might get tighter slices where you might not need to edit the portion of the sample preceding the initial attack or move the sample playback offset closer to the actual sound want to hear
as soon as you trigger the sample. 

I was able to use the .wav files cut with -40 dB easily in the drag and drop Channel Sampler of FL Studio.
Setting it to -23 will be tighter and you won't need to move the sample start offset to the start of the actual plosive sound as often as -40db will leave more sound on the front.

Optional -m argument is the minimum length of silence defaults to 50 milliseconds. 

-r is the sample rate default 44100 CD quality

-c is to specify the audio codec used by ffmpeg default is pcm_s16le

-n directory to output the normalized sample files

-l normalization target level used by ffmpeg-normalize default here is 0.0 dB

-p true peak level used by ffmpeg-normalize default here is 0.0 dB

example: 

Slice raw recordings in folder "/1_raw_recordings" 

Output the sliced .wav files into folder "/2_sliced"

Normalize the files in "/3_normalized"

Set the silence threshold to -23 decibel

Set the minimum silence duration to 20 milliseconds 

python slicer.py -i /1_raw_recordings -o /2_sliced -n /3_normalized  -t -23 -m 20

# Notes

pydub is used to detect silence using a decibel threshold which is default to -40 dB
it is also set with a minimum length of silence duration of 140 milliseconds see slicer.py

The audio segment export function is set to use stereo channels, sampling rate 44100, 16 bit, (CD quality) 
and ffmpeg will use the audio codec pcm_s16le with sample format s16 refer to documentation of pydub and ffmpeg, you can change the codec and format, but this works excellently for CD quality samples.

ffmpeg-normalize is used to normalize the sliced sample files to a peak loudness so as to be able to use them with software samplers. You can set the velocities in the step sequencer. 

# References

Homebrew

https://brew.sh/

ffmpeg

https://ffmpeg.org/

PyDub

https://github.com/jiaaro/pydub

ffmpeg Normalize

https://github.com/slhck/ffmpeg-normalize

How to split an mp3 file by detecting silent parts?

https://askubuntu.com/questions/1264779/how-to-split-an-mp3-file-by-detecting-silent-parts

FL Studio

https://www.image-line.com/
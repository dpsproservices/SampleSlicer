import sys
import os
import os.path
import time
import logging
import pathlib
from pathlib import Path
#import shutil
import logging
import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence

# ------------------------------------------------------------------------------------
# Log file logging
# ------------------------------------------------------------------------------------

logging.basicConfig(filename='logs/slicer.log', encoding='utf-8', level=logging.DEBUG)

# ------------------------------------------------------------------------------------
# set recrusion limit
# ------------------------------------------------------------------------------------

sys.setrecursionlimit(10000)

# spliting audio file into seperate sample .wav files 16 bit 44100
def splitAudioFile (audioFile, outputDir):
   audioSegment = AudioSegment.from_file(audioFile)
   fileNameBase = os.path.splitext (os.path.basename(audioFile))[0]
   #print(fileNameBase)

   audioChunks = split_on_silence (audioSegment, min_silence_len=140, silence_thresh=-40)

   # loop is used to iterate over the output list
   for i, chunk in enumerate (audioChunks):
     outputFile = str(outputDir) + "/" + fileNameBase + "_" + str(i) + ".wav" 
     print("Exporting file: " + outputFile)
     chunk.export (outputFile, format='wav', parameters=["-ac", "2", "-ar", "44100", "-acodec", "pcm_s16le", "-sample_fmt", "s16"])

def sliceRawRecordings (rawRecordingsDir, slicedWavDir):
   
   # make new directory under sliced wav dir for current date time YYYY-MM-DD-HH-MM-SS-PM
   outputDir = slicedWavDir + "/" + time.strftime("%Y-%m-%d-%I-%M-%S-%p")
   pathlib.Path(outputDir).mkdir(parents=True, exist_ok=True)

   extension_list = ('*.m4a', '*.wav', '*.mp3', '*.mp4')
   os.chdir(rawRecordingsDir)
   for extension in extension_list:
      for audioFile in glob.glob (extension):
         print("Splitting: " + audioFile)
         splitAudioFile (audioFile, outputDir)

def normalizeAudioFile (audioFile, outputDir):
   audioSegment = AudioSegment.from_file(audioFile)
   fileNameBase = os.path.splitext (os.path.basename(audioFile))[0]
   #print(fileNameBase)
   outputFile = str(outputDir) + "/" + fileNameBase + "_normalized.wav" 
   audioSegment.export (outputFile, format='wav', frame_rate=44100, channels=2, sample_width=2)
   
def normalizeSamples (slicedWavDir, normalizedWavDir):
   # make new directory under sliced wav dir for current date time YYYY-MM-DD-HH-MM-SS-PM
   outputDir = normalizedWavDir + "/" + time.strftime("%Y-%m-%d-%I-%M-%S-%p")
   pathlib.Path(outputDir).mkdir(parents=True, exist_ok=True)

   os.chdir(slicedWavDir)
   extension_list = ('*.wav')
   os.chdir(rawRecordingsDir)
   for extension in extension_list:
      for audioFile in glob.glob (extension):
         print("Normalizing: " + audioFile)
         normalizeAudioFile (audioFile, outputDir)

# ------------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------------

if __name__ == "__main__":

   rawRecordingsDir = "/Volumes/4TB/sound-design/1_raw_recordings"

   slicedWavDir = "/Volumes/4TB/sound-design/2_sliced_wav"

   normalizedWavDir = "/Volumes/4TB/sound-design/3_normalized_wav"

   #rawRecordingsPath = Path (rawRecordingsDir)
   
   slicedWavPath = Path (slicedWavDir)
   
   #normalizedWavPath = Path (normalizedWavDir)

   sliceRawRecordings (rawRecordingsDir, slicedWavDir)





    

import sys
import os
import logging
import pathlib
from pathlib import Path
import logging
import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence
import argparse
from ffmpeg_normalize import FFmpegNormalize

# ------------------------------------------------------------------------------------
# Log file logging
# ------------------------------------------------------------------------------------

logging.basicConfig(filename='logs/slicer.log', encoding='utf-8', level=logging.DEBUG)

# ------------------------------------------------------------------------------------
# set recrusion limit
# ------------------------------------------------------------------------------------

sys.setrecursionlimit(10000)

# instance of FFmpegNormalize
normalizer = None

# spliting audio file into seperate sample .wav files 16 bit 44100
def splitAudioFile (audioFile, outputDir, silence_threshold = -40, min_silence_len = 50, sample_rate = 44100, audio_codec = "pcm_s16le"):
   audioSegment = AudioSegment.from_file(audioFile)
   fileNameBase = os.path.splitext (os.path.basename(audioFile))[0]

   audioChunks = split_on_silence (
      audioSegment, 
      min_silence_len = min_silence_len, 
      silence_thresh = silence_threshold,
      keep_silence = 0, # dont keep leading 100 ms of silence
      seek_step = 1 # 1 millisecond 
   )

   # loop is used to iterate over the output list
   for i, chunk in enumerate (audioChunks):
     outputFile = str(outputDir) + "/" + fileNameBase + "_" + str(i) + ".wav" 
     print("Exporting file: " + outputFile)
     chunk.export (outputFile, format='wav', parameters=["-ac", "2", "-ar", str(sample_rate), "-acodec", str(audio_codec), "-sample_fmt", "s16"])

def sliceRawRecordings (rawRecordingsDir, slicedWavDir, silence_threshold = -40, min_silence_len = 50, sample_rate = 44100, audio_codec =  "pcm_s16le"):
   extension_list = ('*.m4a', '*.wav', '*.mp3', '*.mp4')
   os.chdir(rawRecordingsDir)
   for extension in extension_list:
      for audioFile in glob.glob (extension):
         audioFilePath = Path(audioFile)
         if audioFilePath.is_file():         
            print("Splitting: " + audioFile)
            splitAudioFile (audioFile, slicedWavDir, silence_threshold, min_silence_len, sample_rate, audio_codec)

def createNormalizer (sample_rate = 44100, audio_codec = "pcm_s16le", target_level = -0.0, true_peak = -0.0):
   return FFmpegNormalize (
      normalization_type = 'peak', # Literal['ebu', 'rms', 'peak'] = 'ebu',
      target_level = target_level,
      print_stats = False,
      loudness_range_target = 7.0,
      keep_loudness_range_target = False,
      keep_lra_above_loudness_range_target = False,
      true_peak = true_peak,
      offset = 0.0,
      dual_mono = False,
      dynamic = False,
      audio_codec = audio_codec,
      audio_bitrate = None,
      sample_rate = sample_rate,
      keep_original_audio = False,
      pre_filter = None,
      post_filter = None,
      video_codec = 'copy',
      video_disable = False,
      subtitle_disable = False,
      metadata_disable = False,
      chapters_disable = False,
      extra_input_options = None,
      extra_output_options = None,
      output_format = None,
      dry_run = False,
      debug = False,
	   progress = False
   )

# normalize wav files into normalized subfolder
def normalizeAudioFile (audioFile, outputDir):
   fileNameBase = os.path.splitext (os.path.basename(audioFile))[0]
   outputFile = str(outputDir) + "/" + fileNameBase + ".wav" 
   normalizer.add_media_file (audioFile, outputFile)
   normalizer.run_normalization()
   
def normalizeSamples (slicedWavDir, normalizedWavDir):
   os.chdir(slicedWavDir)
   extension_list = ('*.wav')
   for extension in extension_list:
      for audioFile in glob.glob (extension):
         audioFilePath = Path(audioFile)
         if audioFilePath.is_file():
            print("Normalizing: " + audioFile)
            normalizeAudioFile (audioFile, normalizedWavDir)

# ------------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------------

if __name__ == "__main__":

   try:

      parser = argparse.ArgumentParser()

      parser.add_argument("-i", "--input_dir", help = "recording files input folder")
   
      parser.add_argument("-o", "--output_dir", help = "sliced sample files output folder")

      parser.add_argument("-t", "--silence_threshold", help = "silence threshold in decibels default -40 dB")

      parser.add_argument("-m", "--min_silence_len", help = "minimum silence duration in milliseconds default 50 ms")

      parser.add_argument("-r", "--sample_rate", help = "audio sample rate default 44100")

      parser.add_argument("-c", "--audio_codec", help = "audio codec default pcm_s16le")

      parser.add_argument("-n", "--normalized_dir", help = "normalized sample files output folder")

      parser.add_argument("-l", "--target_level", help = "normalization target level default 0.0 dB")

      parser.add_argument("-p", "--true_peak", help = "true peak level default 0.0 dB")

      args = parser.parse_args()

      if args.input_dir:
         rawRecordingsDir = args.input_dir

         if args.output_dir:
            slicedWavDir = args.output_dir
      
            if args.silence_threshold:
               silence_threshold = args.silence_threshold
               print("Silence threshold: " + str(silence_threshold) + " dB")

            if args.min_silence_len:
               min_silence_len = args.min_silence_len
               print("Silence length: " + str(min_silence_len) + " ms")

            if args.sample_rate:
               sample_rate = args.sample_rate

            if args.audio_codec:
               audio_codec = args.audio_codec

            sliceRawRecordings (rawRecordingsDir, slicedWavDir, silence_threshold = -40, min_silence_len = 50, sample_rate = 44100, audio_codec = "pcm_s16le")

            if args.normalized_dir:
               normalized_dir = args.normalized_dir

               if args.target_level:
                  target_level = args.target_level

               if args.true_peak:
                  true_peak = args.true_peak

               normalizer = createNormalizer (sample_rate = 44100, audio_codec = "pcm_s16le", target_level = 0.0, true_peak = -0.0)

               normalizeSamples (slicedWavDir, normalized_dir)
         else:
            print("Need to specify samples files output directory")
            logging.error("Need to specify samples files output directory")
      else:
         print("Need to specify input recordings directory")
         logging.error("Need to specify input recordings directory")

   except:
      logging.error("See command line usage: python slicer.py -h")

   





    

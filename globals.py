import sys
import logging
from enum import Enum
import copy


# ------------------------------------------------------------------------------------
# Log file logging
# ------------------------------------------------------------------------------------

logging.basicConfig(filename='logs/slicer.log', encoding='utf-8', level=logging.DEBUG)

rawRecordingsDir = "/Volumes/4TB/sound-design/1_raw_recordings"

slicedWavDir = "/Volumes/4TB/sound-design/2_sliced_wav"

normalizedWavDir = "/Volumes/4TB/sound-design/3_normalized_wav"
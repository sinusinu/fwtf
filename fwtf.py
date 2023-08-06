import os
import sys
import time
from faster_whisper import WhisperModel

if (len(sys.argv) < 2):
    print("Usage: %s path-to-audio-file" % sys.argv[0])
    exit()

if (os.path.isfile(sys.argv[1]) == False):
    print("File %s does not exist" % (sys.argv[1]))
    exit()

print("Loading model...")

currentPath = os.path.dirname(os.path.realpath(__file__))
model = WhisperModel("whisper-l2-q8", device="cuda", compute_type="int8", download_root=currentPath, local_files_only=True)
# whisper-l2-q8 is my locally quantized model, made with ct2-transformers-converter
# if you have no local model, use this instead. it will automatically download the model
#model = WhisperModel("large-v2", device="cuda", compute_type="int8", download_root=currentPath)

print("Transcribing...")

startTime = time.time()

segment, info = model.transcribe(sys.argv[1], word_timestamps=True)
seggs = list(segment)   # i know, go away

print("")

for seg in seggs:
    print("[%.2f -> %.2f] %s" % (seg.start, seg.end, seg.text.strip()))

endTime = time.time()

print("")

print("Took %f seconds" % (endTime - startTime))
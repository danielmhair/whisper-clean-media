import os
from moviepy.video.io.VideoFileClip import VideoFileClip

from utils import run_subprocess

def get_name(filename, t1, t2):
  name, ext = os.path.splitext(filename)
  T1, T2 = [int(1000*t) for t in [t1, t2]]
  return "%sSUB%d_%d.%s" % (name, T1, T2, ext)

try:
  print('Paths must be absolute:')
  print('/mnt/c/Users/danie/Workspace/whisper.cpp/samples/JurassicWorldCampCretaceous-s01e01.mkv')
  print('/volume2/NAS-8TB-HDD/Movies/Original_Unedited/Jumper.mkv')
  src = input('Video to extract audio from:')
  dest = input('Location for wav file:')
  # mp4_src = src.replace('.mkv', '.mp4')
  video = VideoFileClip(src)
  print(f"Video duration: {video.duration}")
  run_subprocess(["ffmpeg", "-i", src, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", 'output.wav'])
  print(f"Exported Audio!!!!!! ==============================")

except Exception as e:
   print(e)
   raise e

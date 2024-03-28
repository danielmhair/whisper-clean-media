import os
from moviepy.video.io.VideoFileClip import VideoFileClip

from utils import run_subprocess

def get_name(filename, t1, t2):
  name, ext = os.path.splitext(filename)
  T1, T2 = [int(1000*t) for t in [t1, t2]]
  return "%sSUB%d_%d.%s" % (name, T1, T2, ext)

def convert_to_wav(src, dest):
  try:
    # mp4_src = src.replace('.mkv', '.mp4')
    video = VideoFileClip(src)
    print(f"Video duration: {video.duration}")
    # TODO: Before converting, find the right codec - ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 input.mkv
    run_subprocess(["ffmpeg", "-i", src, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", dest])
    print(f"Exported Audio!!!!!! ==============================")
    print('Paths must be absolute:')
    print('/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/Ghostbusters (1984).mkv')
    print('/volume2/NAS-8TB-HDD/Movies/Original_Unedited/Jumper.mkv')
    src = input('Video to extract audio from:')
    dest = input('Location for wav file:')
    # mp4_src = src.replace('.mkv', '.mp4')
    video = VideoFileClip(src)
    print(f"Video duration: {video.duration}")
    # TODO: Before converting, find the right codec - ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 input.mkv
    run_subprocess(["ffmpeg", "-i", src, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", 'output.wav'])
    print(f"Exported Audio!!!!!! ==============================")

  except Exception as e:
    print(e)
    raise e


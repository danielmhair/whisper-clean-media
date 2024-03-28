import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from convert_to_mp4 import convert_to_mp4, run_subprocess

def get_name(filename, t1, t2):
  name, ext = os.path.splitext(filename)
  T1, T2 = [int(1000*t) for t in [t1, t2]]
  return "%sSUB%d_%d.%s" % (name, T1, T2, ext)


def get_start_end_times():
    start_time = input('start_time (seconds):')
    start_time_parts = start_time.split(':')
    if (len(start_time_parts) != 3):
      raise Exception('start_time must be in the format of hh:mm:ss')
    start_time_sec = int(start_time_parts[0]) * 3600 + int(start_time_parts[1]) * 60 + int(start_time_parts[2])
    end_time = input('end_time (seconds):')
    end_time_parts = end_time.split(':')
    if (len(end_time_parts) != 3):
      raise Exception('end_time must be in the format of hh:mm:ss')
    end_time_sec = int(end_time_parts[0]) * 3600 + int(end_time_parts[1]) * 60 + int(end_time_parts[2])
    return start_time_sec, end_time_sec


try:
  print('Examples of usage for video path')
  print('/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/Ghostbusters (1984).mkv')
  print('/volume2/NAS-8TB-HDD/Movies/Original_Unedited/Jumper.mkv')
  src = input('Video to remove a clip from:')
  clips_to_remove = []

  while (input(f'Do you want to remove {"another" if len(clips_to_remove) > 0 else "a"} clip? (y/n)') == 'y'):
    start_time, end_time = get_start_end_times()
    clips_to_remove.append((start_time, end_time))

  # 'ffmpeg -i input.mkv -c:v copy -c:a copy output.mp4' in a subprocess if the file is mkv
  if (not src.endswith('.mp4')):
    convert_to_mp4(src)

  dest = input('Destination of video:')
  mp4_src = src.replace('.mkv', '.mp4')
  video = VideoFileClip(mp4_src)
  print(f"Video duration: {video.duration}")
  run_subprocess(["ffmpeg", "-i", src, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", 'output.wav'])
  print(f"Exported Audio!!!!!! ==============================")

  print(clips_to_remove)
  # turn tuple array into flat array
  start_end_arr = []
  for clip_a, clip_b in clips_to_remove:
     start_end_arr.append(clip_a)
     start_end_arr.append(clip_b)

  start_end_arr.insert(0, 0)
  start_end_arr.append(video.duration)
  print(start_end_arr)

  name, ext = os.path.splitext(dest)
  part = 0
  while (len(start_end_arr) > 0):
    part += 1
    start = start_end_arr.pop(0)
    end = start_end_arr.pop(0)
    print(f'Creating subclip from {start} to {int(end)} and saving to "{name} - pt{part}.mp4"')    
    ffmpeg_extract_subclip(src, int(start), int(end))
    print('Finished creating subclip!')

  # TODO: Do cleanup
  # TODO: Separate remove clip logic into its own python script
  # TODO: Separate converting file to mp4
  # TODO: Separate converting file to audio

except Exception as e:
   print(e)
   raise e

from utils import convert_to_mp4

try:
  print('Examples of usage for video path')
  print('/mnt/c/Users/danie/Workspace/whisper.cpp/samples/JurassicWorldCampCretaceous-s01e01.mkv')
  print('/volume2/NAS-8TB-HDD/Movies/Original_Unedited/Jumper.mkv')
  src = input('Video to convert to mp4:')
  dest = input('Location for mp4:')

  if (src.endswith('.mp4')):
    print('File is already in mp4 format')
  
  convert_to_mp4(src)

except Exception as e:
   print(e)
   raise e

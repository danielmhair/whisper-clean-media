import subprocess
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips
from pydub import AudioSegment
from pydub.utils import mediainfo

def run_subprocess(command, log = False):
  # Start the command as a subprocess
    print('converting to mp4')
    process = subprocess.Popen(command)

    if log:
        while True:
            output = process.stderr.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.decode('utf-8').strip())

    # Wait for the subprocess to exit
    process.wait()
    print('Finshed converting to mp4')

    # Check if process was exit code 0
    if process.returncode != 0:
        print('But something went wrong!')
        raise subprocess.CalledProcessError(process.returncode, command)

def convert_to_mp4(src):
    # if mp4 file already exists then dont convert
    if (os.path.exists(src.replace('.mkv', '.mp4'))):
       return

    run_subprocess(['ffmpeg', '-i', src, '-c:v', 'copy', '-c:a', 'copy', src.replace('.mkv', '.mp4')])
    print('converted to mp4!')

from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
from spleeter.separator import Separator
import os
import re
from clean_transcription import parse_audio_ouput
from find_profanity import detect_profanity

# Instead of this whole file, we could just set the volume to 0
# ffmpeg -i input.mkv -af volume=enable='between(t,5,10)':volume=0 output.mkv


import os
from pydub import AudioSegment
from spleeter.separator import Separator

def prepare_background_audio(input_file='output.wav', output_folder='output'):
    separator = Separator('spleeter:2stems')
    
    # Build the full paths for the input and output
    input_file = os.path.join(os.path.dirname(__file__), input_file)
    output_folder = os.path.join(os.path.dirname(__file__), output_folder)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the audio file with pydub
    audio = AudioSegment.from_file(input_file, format="wav")

    # Set the length of each chunk (10 minutes here)
    chunk_length = 10 * 60 * 1000  # in milliseconds

    # Initialize list to store processed chunks
    processed_chunks = []

    for i in range(0, len(audio), chunk_length):
        # Get individual chunk
        audio_chunk = audio[i:i + chunk_length]
        
        # Export chunk to temporary file
        temp_chunk_path = os.path.join(output_folder, "temp_chunk.wav")
        audio_chunk.export(temp_chunk_path, format="wav")
        
        # Process the chunk with Spleeter and save to temp folder
        temp_output_folder = os.path.join(output_folder, "temp_output_folder")
        separator.separate_to_file(temp_chunk_path, temp_output_folder)
        
        # Load processed accompaniment (ignoring vocals)
        processed_chunk_path = os.path.join(temp_output_folder, "temp_chunk", "accompaniment.wav")
        processed_chunk = AudioSegment.from_file(processed_chunk_path, format="wav")
        
        # Append processed chunk to list
        processed_chunks.append(processed_chunk)

    # Concatenate all processed chunks
    final_audio = sum(processed_chunks)

    # Export final processed audio
    final_audio_path = os.path.join(output_folder, "accompaniment-new.wav")
    final_audio.export(final_audio_path, format="wav")


def time_str_to_seconds(time_str):
    h, m, s_ms = time_str.split(':')
    return (int(h) * 3600) + (int(m) * 60) + float(s_ms)


def replace_audio_segments(
    video_path='Ghostbusters (1984).mkv',
    audio_path='output/accompaniment-new.wav',
    output_path='Ghostbusters (1984)-out.mkv',
    segments=[('00:05:00.000', '00:05:10.000'), ('00:10:00.000', '00:10:10.000')],
):
    # Load the original video and its audio
    video_path = os.path.join(os.path.dirname(__file__), video_path)
    audio_path = os.path.join(os.path.dirname(__file__), audio_path)
    output_path = os.path.join(os.path.dirname(__file__), output_path)
    video = VideoFileClip(video_path)
    original_audio = video.audio

    # Initialize variables
    final_audio_segments = []
    last_end = 0

    # Load the accompaniment audio


    # Load the accompaniment
    accompaniment = AudioFileClip(audio_path)

    for start, end in segments:
        # Convert the start and end times to seconds
        start = time_str_to_seconds(start) # - (300 / 1000)
        end = time_str_to_seconds(end) # + (300 / 1000)

        # Append original audio up to the start of the new segment
        final_audio_segments.append(original_audio.subclip(last_end, start))

        # Append the accompaniment for the segment
        new_audio_segment = video.audio.volumex(0.0).subclip(start, end)

        # new_audio_segment = accompaniment.subclip(start, end)

        final_audio_segments.append(new_audio_segment)

        # Update the last_end for the next iteration
        last_end = end

    # Append remaining original audio
    final_audio_segments.append(original_audio.subclip(last_end))

    # Concatenate all the audio segments
    final_audio = concatenate_audioclips(final_audio_segments)

    # Set the new audio to the original video
    video = video.set_audio(final_audio)

    # Before converting, find the right codec - ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 input.mkv
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")

def main(path="output.txt"):
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, "r", encoding="ISO-8859-1") as f:
        result = parse_audio_ouput(f.read())
        lines_with_prof = detect_profanity(result)
        segments_to_mute = []
        for i, line in enumerate(lines_with_prof):
            if line["is_profanity"]:
                context = list(map(lambda x: x['text'], lines_with_prof[i-5:i+5]))
                print(" ".join(context) + " (" + line['text'] + ")")
                segments_to_mute.append((line["start_time"], line["end_time"]))
        print(segments_to_mute)
        # prepare_background_audio()
        output_path: str = 'Ghostbusters (1984)-out.mkv'
        output_path = os.path.join(os.path.dirname(__file__), output_path)
        replace_audio_segments(
            video_path='Ghostbusters (1984).mkv',
            audio_path='output/accompaniment-new.wav',
            output_path=output_path,
            segments=segments_to_mute,
        )

if __name__ == "__main__":
    main()

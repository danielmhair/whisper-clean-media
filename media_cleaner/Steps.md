git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
./models/download-ggml-model.sh base.en
apt install make
sudo apt update
sudo apt install build-essential
sudo apt install g++
make

# copied over remove_clip from 8tb hard drive

apt install python3-pip
pip install moviepy ffmpeg pydub
apt install ffmpeg

# Running the actual command

cd samples
python3 convert_to_wav.py
/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/Ghostbusters (1984).mkv
/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output.wav
./main -m ./models/ggml-base.en.bin -f ./samples/output.wav -ml 1

# Need to clean up the audio to be full words
./main -m ./models/ggml-base.en.bin -f ./samples/output.wav -ml 1 >> output.txt

# Now that we have the audio, we need to clean the transcription to have full words

python3 clean_transcription.py

# Finished cleaning words (09/05/2023)
- Anything that starts with parenthesis combine until you find end parenthesis
- Same for brackets
- For lines that start only has [ wait until it has ]

# Searched for words that are profane and made a list and their associated time slots

~pip install profanity-check~
- Due to `ImportError: cannot import name 'joblib' from 'sklearn.externals' (/usr/local/lib/python3.8/dist-packages/sklearn/externals/__init__.py)`
pip install alt-profanity-check
pip install sklearn --upgrade


# Then find the best way to remove the word from the audio and create the original format (video or audio file) with the cleaned audio

pip install spleeter

python3 remove_profanity.py


# Full Steps
python3 convert_to_wav.py
/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/Ghostbusters (1984).mkv
/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output.wav
./main -m ./models/ggml-base.en.bin -f ./samples/output.wav -ml 1 >> output.txt
python3 remove_profanity.py

# Next: The audio needs to go through a vocal separator before transcription
## Use Ultimate Vocal Remover?
https://github.com/Anjok07/ultimatevocalremovergui/blob/v5-beta-cml/README.md#ultimate-vocal-remover-v5-command-line-beta


# Next: Use WhisperX instead of whisper.cpp? Might be more accurate...
https://github.com/m-bain/whisperX



# Next: Cleanvid for removing profanity from video using srt files. Should I just generate an srt?
https://github.com/mmguero/cleanvid/tree/main

# Remove Not-Safe-For-Work Images from video

https://github.com/GantMan/nsfw_model
https://github.com/infinitered/nsfwjs#host-your-own-model
https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1
https://github.com/vladmandic/nudenet
https://github.com/notAI-tech/NudeNet/

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

## Try out nsfw model
- https://github.com/GantMan/nsfw_model
  - https://github.com/infinitered/nsfwjs#host-your-own-model
  - https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1

### Upgraded to 3.10
sudo apt install wget build-essential libreadline-gplv2-dev libncursesw5-dev \
     libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz 
tar xzf Python-3.10.8.tgz 
cd Python-3.10.8 
./configure --enable-optimizations 
make altinstall 
poetry env use 3.10
rm -rf Python-3.10.8.tgz Python-3.10.8

poetry add tensorflow@2.9.0
poetry add nsfw-detector
./download_nsfw_model.sh
poetry add opencv-python

# Try Deep Nude as other wasnt the best
- JS Version: https://github.com/vladmandic/nudenet
  - Python Version: https://github.com/notAI-tech/NudeNet/

pip install --upgrade nudenet
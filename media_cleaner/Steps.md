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
/mnt/c/Users/danie/Workspace/whisper.cpp/samples/JurassicWorldCampCretaceous-s01e01.mkv
/mnt/c/Users/danie/Workspace/whisper.cpp/samples/output.wav
./main -m ./models/ggml-base.en.bin -f ./samples/output.wav -ml 1

# Need to clean up the audio to be full words
./main -m ./models/ggml-base.en.bin -f ./samples/output.wav -ml 1 >> output.txt

# Now that we have the audio, we need to clean the transcription to have full words

python3 clean_transcription.py

# Remove Not-Safe-For-Work Images from video

https://github.com/GantMan/nsfw_model
https://github.com/infinitered/nsfwjs#host-your-own-model
https://shift.infinite.red/avoid-nightmares-nsfw-js-ab7b176978b1
https://github.com/vladmandic/nudenet
https://github.com/notAI-tech/NudeNet/

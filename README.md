# Split audio file on silences and transcribe

A Python script using [Pydub](https://github.com/jiaaro/pydub) and Google Speech API via [SpeechRecongition](https://github.com/Uberi/speech_recognition) to split an MP3 file into separate .wav files and transcribe the contents.

- Assumes a 1 seocnd silence between clips.
- Transcribes the first 5 seconds of each clip.
- Creates an ```output``` dir in the current directory.
- Outputs an ```index.csv``` of filenames and contents.

This was a quick diversion project and was built to work on one source file, so YMMV.

### Run with Docker
```
docker run --rm -v "$(pwd)":/src:rw -it $(docker build -q .) input_file.mp3
```

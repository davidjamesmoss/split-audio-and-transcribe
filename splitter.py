import os
import argparse
import csv
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

output_path = './src/output'
if not os.path.exists(output_path):
    os.mkdir(output_path)

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

input_audio = AudioSegment.from_mp3(f'./src/{args.input_file}')
print('Splitting audio file...')
audio_clips = split_on_silence(input_audio, min_silence_len=1000, silence_thresh=-40, keep_silence=500)

print('Transcribing clips...')
r = sr.Recognizer()
with open(f'{output_path}/index.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['Number', 'Filename', 'Contents'])

    for i, clip in enumerate(audio_clips, 1):
        output_file = f'{output_path}/clip{i}.wav'

        clip.export(output_file, format="wav")
        with sr.AudioFile(output_file) as source:
            audio = r.record(source, duration=5)
            try:
                sr_output = r.recognize_google(audio)
            except sr.UnknownValueError:
                sr_output = 'unknown'

        print(f'{i}: {sr_output}')
        filename = sr_output[0:50].strip().replace(' ', '_').lower()
        filename = f'{i}_{filename}.wav'

        spamwriter.writerow([i, filename, sr_output])
        os.rename(output_file, f'{output_path}/{filename}')

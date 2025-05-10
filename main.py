from TTS.api import TTS
import winsound

import multiprocessing
from time import sleep

import keyboard
import pyperclip

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

def Read(text="No text has been provided."):
    winsound.PlaySound(tts.tts_to_file(text=text, file_path="output.wav", speaker_wav="sample.mp3", language="en"), winsound.SND_ASYNC)
    
print('Reader Loaded, press esc to exit.')

if __name__ == '__main__':
    while True:

        if keyboard.is_pressed('esc'):
            break
        elif keyboard.is_pressed('ctrl+b'):
            Read(pyperclip.paste())
        
        sleep(0.1)
import speech_recognition as sr
import webbrowser
from time import ctime
import time
from gtts import gTTS
import playsound
import os
import random
# initialise a recogniser
r = sr.Recognizer()

# get string and make a audio file to be played
def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# listen for audio and convert it to text:
def record_audio(ask = False):
    with sr.Microphone() as sourse:
        if ask:
            alexis_speak(ask)
        audio = r.listen(sourse)
        voice_data = ''
        try:
            # convert audio to text
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('sorry could not recognize your voice')
        except sr.RequestError:
            alexis_speak('sorry my speech service is down')
        return voice_data
    

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('here is the location ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexis_speak('How can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)
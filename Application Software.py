from tkinter import*
import speech_recognition as sr
import pyttsx3
from datetime import datetime

root = Tk()
root.geometry("500x500")

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How Can I Help You....?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_date = ''
        
        try:
            voice_data = speech_recognisor.recognize_google(audio, language = 'en-in')
            
        except sr.UnknownValueError:
            print("Please Repeat I Did Not Get That")
            speak("Please Repeat I Did Not Get That")
            
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My Name Is Apurbasi")
        print("My Name Is Apurbasi")
        
    if "time" in voice_data:
        speak("Current Time Is :")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(curent_time)
        print(current_time)
        
r_audio()
root.mainloop()
            


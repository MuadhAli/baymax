#!/usr/bin/python3
from turtle import delay
import speech_recognition as sr
import datetime, time
import os, sys
import webbrowser
import pyttsx3
import wikipedia
import re
import requests
import pyaudio
import pyautogui as pg
# from ecapture import ecapture as ec
import json
import requests
import random
from tkinter import *
import pygame

r = sr.Recognizer()
   


def voice_Recognizer():
    recognize_words = ' '
    try:
        with sr.Microphone() as source:   
            print("\nPlease wait. Calibrating microphone...")   
            # listen for 2 seconds and create the ambient noise energy level   
            r.adjust_for_ambient_noise(source, duration=2)  
            r.dynamic_energy_threshold = True    
            print("Listening...")  
            audio = r.listen(source) 
        recognize_words = r.recognize_google(audio).lower().replace("'", "")
        print("Baymax thinks you said '" + recognize_words + "'")
    except sr.UnknownValueError:
        listen = voice_Recognizer()
        return listen
    except sr.WaitTimeoutError:
        pass
    except sr.RequestError:
        print('FACING NETWORK ERROR!')
    return recognize_words

def speak(message):
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'win32':
        tts_engine = pyttsx3.init('sapi5')
        voices = tts_engine.getProperty('voices')
        # print(voices[1].id)
        tts_engine.setProperty('voice', voices[0].id)
        tts_engine.say(message)
        tts_engine.runAndWait()
    elif sys.platform == 'Linux' or sys.platform == 'linux' or sys.platform == 'Ubuntu':
        #espeak
        tts_engine = 'espeak'
        print("Baymax: " + ' ' + message + '')
        return os.system(tts_engine + ' "' + message + '"')

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("Hello I'm Beymax. I am your personal virtual assistant, how can I help you?")       

def date():
    currentdate = datetime.datetime.now()
    result = currentdate.strftime("%d %b %Y %A")
    print(result)
    speak(result)
    
def currenttime():
    result = time.strftime("%I:%M:%S %A")
    print(result)
    speak(result)

def googleSearch(recognize_words):
    cleanword = recognize_words.replace("google", "")
    webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))
    result = 'Opening your query in google search engine sir'
    print(result)
    speak(result)

# def wiki():
#     speak('Searching Wikipedia...')
#     words = recognize_words.replace("wikipedia", "")
#     results = wikipedia.summary(words, sentences=3)
#     speak("According to Wikipedia")
#     print(results)
#     speak(results)

def weather():
    cleanword = "Hows the weather"
    webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))
    result = 'Opening weather status in google search engine sir'
    print(result)
    speak(result)

def location(recognize_words):
        data = recognize_words.split(" ")
        location = ""
        location = location.split(" ")
        for i in range(2, len(data)):
            location.append(data[i])
        place = "  ".join(location)
        result = "Hold on sir, I will show you."
        print(result)
        speak(result)
        webbrowser.open("https://www.google.nl/maps/place/" + place)

def openWebsite(recognize_words):
    reg_ex = re.search('open (.+)', recognize_words)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain + ".com"
        webbrowser.open(url)
        speak("done...")
    else:
        speak("website not exist")

def newsReport():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            print("Today's top ten Headline are : ")
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            print("Next news : ")
            speak("Next news : ")
        print(to_speak)
        speak(to_speak)

def poweroff():
    pg.hotkey('alt','ctrl','t')
    pg.sleep(2)
    pg.write("poweroff")

def noteDown():
    text_to_note = recognize_words.replace("write down", "")
    pg.hotkey('alt','ctrl','t')
    pg.sleep(2)
    pg.write("nano note.txt")
    pg.sleep(2)
    pg.press('enter')
    pg.write(text_to_note)
    pg.hotkey('ctrl','s')
    pg.hotkey('ctrl','x')

def capture_image():
    pg.hotkey('ctrl','alt','t')
    pg.sleep(2)
    pg.write("raspistill -o img.jpg")
    pg.sleep(1)
    pg.press('enter')
      
def identifier():
    pg.hotkey('ctrl','alt','t')
    pg.sleep(2)
    pg.write("sudo python3 test.py")
    pg.sleep(1)
    pg.press('enter')
    pg.sleep(45)
    pg.hotkey('alt','f4')

def whatsapp():
    url = "https://web.whatsapp.com/"
    webbrowser.open(url)
    speak("done sir...")

def youtube_play():
    url1 = "https://www.youtube.com/results?search_query="
    cleanword = recognize_words.replace("play", "")
    url2 = url1+cleanword
    webbrowser.open(url2)
    result = 'Opening your Video ' + cleanword + "in youtube"
    print(result)
    speak(result)

def songplay():
    pygame.mixer.init()
    list1 = [1, 2, 3]
    song_number = random.choice(list1)
    song_name = str(song_number)+".mp3"
    song_path = "/home/pi/Music/"+song_name
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()



#======================= ACCESSING COMMANDS ==============================#
if __name__ == "__main__":
    time.sleep(2)
    greeting()
    while True:
        recognize_words = voice_Recognizer()
        
        if "who are you" in recognize_words:
            print("I'm Beymax your personal virtual assistant.")
            speak("I'm  Beymax your personal virtual assistant.")
        
        elif 'hello' in recognize_words:
            print("hello sir, how are you?")
            speak("hello sir, how are you?")
        
        elif "how are you" in recognize_words:
            print("Baymax speaking....")
            speak("I'm feeling hot because of your computer temperature, no! just kidding, I am great, I assume youre also having a good time")
        
        elif "whats new" in recognize_words:
            print("Nothing. I just thought it was a bit of an overreaction. It's been a while since I've read it.")
            speak("Nothing. I just thought it was a bit of an overreaction. It's been a while since I've read it.")
        
        elif "its good" in recognize_words:
            print("It's all good. It's one of those things that makes me smile")
            speak("It's all good. It's one of those things that makes me smile")
        
        elif "thats great" in recognize_words:
            print("Thank you")
            speak("Thank you")
        
        elif "thank you" in recognize_words:
            print("you're welcome")
            speak("you're welcome")
        
        elif "you are welcome" in recognize_words:
            print("my pleasure")
            speak("my pleasure")
        
        elif "where are you from" in recognize_words:
            print("Magical place called Mangalore")
            speak("Magical place called Mangalore")

        elif "who is your owner" in recognize_words:
            print("My masters are Nouman, Muadh, Rabeeh, Sanad, you can contact them through github as Pace 20's")
            speak("My masters are now-maan, muaadh, rabeeh, sa-na-d, you can contact them through github as Pace 20's")
        
        elif "goodbye" in recognize_words or "good bye" in recognize_words or "bye" in recognize_words or "see you later" in recognize_words:
            print("See you later, bye")
            speak("See you later, bye")
            quit()
        
        elif "whats the date" in recognize_words:
            date()
        
        elif "whats the time" in recognize_words:
            currenttime()
        
        elif "google" in recognize_words:
            googleSearch(recognize_words)
        
        elif "where is" in recognize_words:
            location(recognize_words)   
        
        elif "open" in recognize_words:
            openWebsite(recognize_words)
        
        elif "read out todays headlines" in recognize_words:
            newsReport()
        
#===================== ADDITIONAL FEATURES ======================#

        elif "power off" in recognize_words:
            poweroff()
        
        elif "write down" in recognize_words:
            noteDown()
        
        # elif "camera" in recognize_words or "take a photo" in recognize_words:
        #     ec.capture(0,"robo camera","img.jpg")


        elif "photo" in recognize_words or "capture" in recognize_words or "selfie" in recognize_words:
            capture_image()
        
        elif "identify me" in recognize_words or "who am i" in recognize_words or "recognise me" in recognize_words:
            identifier()

        elif "whats the weather" in recognize_words or "weather" in recognize_words:
            weather()

        elif "acha hai" in recognize_words or "achcha hai" in recognize_words:
            speak("Bahooth achcha haai")

        elif "show me whatsapp" in recognize_words or "my whatsapp" in recognize_words:
            whatsapp()
        
        elif "youtube" in recognize_words:
            youtube_play()

        elif "play music" in recognize_words:
            songplay()
        
        elif "music off" in recognize_words or "music of" in recognize_words or "off" in recognize_words:
            stop_song()
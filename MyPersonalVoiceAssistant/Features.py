'"this page contains all the feature functions of the voice assistance which it will use to make different action.."'

# improting the necessary files required to run
# import section start  

import pyttsx3
import datetime
import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
from Intro import Text
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import keyboard
import mouse
import pyautogui as pag
import pyttsx3
from time import sleep
import requests
import subprocess as sp
from AppPath import Paths
import psutil

# import section end

# news api configure area
NEWS_API_KEY = "a04ec0a56eb64dbe89744814d0c47432"
OPENWEATHER_APP_ID = "3932348382eddf47ba21fe5a50913ba4"

# varible set for the voice rate and volume.
x = 160
v = 1.0

'"creating engine and using speech api to make the assistant to speak."'
engine = pyttsx3.init('sapi5')

# now getting the voices property from this engine
voices = engine.getProperty('voices')

'"The below line is used to find the number of voices in my system . There are currently 4 voices."'
# print(voices[1].id)

'"now we will set the property of voices actually here we are choosing whether we want male voice or female"'
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', x)

'" Below is the speak function which will make system to output the voice"'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# feature functions area
def search_on_google(str): 
    speak(Text[7])
    pywhatkit.search(str)


# coding and cp platforms
def search_on_codeforces(str):
    result = "https://codeforces.com//profile//" + str

    speak(Text[7])
    web.open(result)

def search_contest():
    speak(Text[7])
    web.open("https://codeforces.com//contests")
    

def OpenLeetCode():
    speak(Text[7])
    web.open("https://leetcode.com//problemset//all//?difficulty=MEDIUM&page=1")

def LeetCodeProfile():
    speak(Text[7])
    web.open("https://leetcode.com/user8782zV/")



#social apps and websites
def OpenProfile():
    speak(Text[7])
    web.open("https://www.linkedin.com//in//niteesh-kumar-0a949b126//")


def OpenLinkedIn():
    speak(Text[7])
    web.open("https://www.linkedin.com//feed//")
    
def SearchLinkedIn(term):
    speak(f"Searching {term}")
    speak(Text[1])
    
    result = "https://www.linkedin.com//in//" + term + "//"
    speak("This is what i found sir..")
    web.open(result)

# youtube section
def YouTubeSearch(word):
    '"result variable contains the url for the youtube"'
    result = "https://www.youtube.com//results?search_query=" + word

    speak("I found this on YouTube sir...")
    web.open(result)

    
def PlayOnYoutube(word):
    result = "https://www.youtube.com//results?search_query=" + word
    speak(Text[0])
    speak(f"Playing {word}..")
    pywhatkit.playonyt(result)

#wikipedia section
def SearchWikipedia(term):
    results = wikipedia.summary(term, sentences=2)
    speak(Text[2])
    speak(results)

#finding my id address
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    ip_address["ip"]
    speak(Text[2])
    speak(f"this is your ip address sir !! {ip_address['ip']}")

# opening of the apps and system files 
def OpenCmd():
    try:
        os.system("%windir%\system32\cmd.exe")
    
    except Exception as e:
        speak("Not available sir !!")

def open_camera():
    try:
        sp.run('start microsoft.windows.camera:', shell=True)

    except Exception as e:
        speak("Camera not available sir")

def OpenNotePad():
    try:
        os.startfile(Paths['notepad'])

    except Exception as e:
        speak("Cannot open notepad sir..")

def OpenSublime():
    try:
        os.startfile(Paths['sublime-text'])
    
    except Exception as e:
        speak("Cannot open sublime text sir...")

def OpenEclipse():
    try:
        os.startfile(Paths['eclipse'])
    
    except Exception as e:
        speak("Cannot open eclipse ide , sir")
    
def OpenPaint():
    try:
        os.startfile(Paths['paint'])
    
    except Exception as e:
        speak("Cannot open paint , sir")

def open_music():
    try:
        directory = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"
        os.startfile(directory)
        
    except Exception as e:
        speak("Cannot Play the music sir..")

def Openmsword():
    try:
        os.startfile(Paths['msword'])
    
    except Exception as e:
        speak("Cannot open MS word , sir")
    
def devc():
    try:
        os.startfile(Paths['devc'])
    
    except Exception as e:
        speak("Cannot open dev c++ ide , sir")

def Openxamp():
    try:
        os.startfile(Paths['xamp'])
    
    except Exception as e:
        speak("Cannot open xamp control pannel , sir")

# key board actions
def SwitchTabs():
    keyboard.press("alt + tab")
    keyboard.release("alt + tab")

def OpenTaskManager():
    os.system("%windir%\\system32\\taskmgr.exe //7")

#whatsapp automation
def send_whatsapp_message(number, message):
    speak(Text[2])
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message )
    speak("Message sent sir!")


# def multiple_whatsapp_message():

def OpenWhatsapp():
    web.open("https://web.whatsapp.com/")


def OpenGmail():
    web.open("https://mail.google.com/mail/u/0/")

def OpenSDESheet():
    web.open("https://docs.google.com/spreadsheets/d/1PNvcsVmkb7YR5Bqk3OgVvUIa6_4OElKToTc-oQgo-yk/edit#gid=1111792435")


# defining the headline function
def get_latest_news():
    try:
        news_headlines = []
        res = requests.get( f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    
        articles = res["articles"]
        
        for article in articles:
            news_headlines.append(article["title"])
    
        speak("Todays Headlines are: ")
        speak(news_headlines[:5])
        

    except Exception as e:
        speak("Sir !! I am unable to find the news right now please try later !!!")

def get_weather_report(city):
    try:
        res = requests.get( f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
        
        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]

        speak("The weather report is : ")
        feels_like = res["main"]["feels_like"]
        speak(weather) 
        speak( f"Maximum temperature {temperature}℃ !! and Minimum Temperature is {feels_like}℃" )

    except Exception as e:
        speak("Sorry sir , could not find the wether for the city you have asked.")

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        speak ( res["joke"] )

    except Exception as e:
        speak( "Can't find any thing")

# for closing any app
def CloseApp(name):
    speak(Text[1])
    for proc in psutil.process_iter():
        if proc.name() == name:
            speak("Closing process: " + name)
            if(check_process_exist_by_name(name)):
                speak("Closing of: " + name + " sucess")
                os.system("taskkill /f /im " + name + ".exe")
            else:
                speak("Closing of: " + name + " failed")
            

def check_process_exist_by_name(name):
    for proc in psutil.process_iter():
        if proc.name() == name:
            return True
 
    return False

def  Close():
    keyboard.press_and_release("alt + f4")

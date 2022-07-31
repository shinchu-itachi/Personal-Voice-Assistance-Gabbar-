'"Welcome to the main page of the this project. This file will contain the structure of complete prjoect."'
# to play song  using the gabbar , give command Gabbar play SongName
# improting the necessary files required to run
# import section start  
import os
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser as web
import Intro
import Features
import keyboard
import mouse
import webbrowser as web
import pywhatkit
from AppPath import Paths
from Intro import OpeningCallsResonse1Hindi , Check , IpAdd ,  Weather , striver , News , lovebabbar , AppraisalGabbar , IntroText , OpeningCalls , OpeningCallsResponse1Eng , OpeningCallsResponse2Eng , OpeningCallsResponse2Hindi , OpeningCallsResponse3Eng , OpeningCallsResponse3Hindi , CloseGabbar ,  Text , QuestionEng , QuestionHindi , GoodBye , IntroText , NiteeshHindi , NiteeshQuestion , SearchBox , OpeningCalls , AskingGabbarEng , AskingGabbarHindi
from Features import YouTubeSearch , PlayOnYoutube , search_on_google , search_on_codeforces , search_contest, OpenLeetCode , OpenCmd , LeetCodeProfile , OpenLinkedIn , SearchLinkedIn , OpenProfile
from Features import OpenCmd , send_whatsapp_message , open_camera , OpenNotePad, OpenEclipse , Openmsword , OpenSublime , devc  , OpenPaint , Openxamp
from Features import  OpenGmail , find_my_ip , OpenSDESheet, OpenWhatsapp , CloseApp
from Features import SwitchTabs , open_music , SearchWikipedia , get_random_joke, get_latest_news ,  Close , OpenTaskManager , get_weather_report


# import section end


# varible set for the voice rate and volume.
x = 160
v = 1.0
time = int(datetime.datetime.now().hour)
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

'"Below function will wish the user"'
def wish():
    hour = time
    if ( hour >= 0 and hour < 12):
        speak("Good Morning , Niteesh")
    elif ( hour >= 12 and hour < 19):
        speak("Good Noon , Niteesh")
    elif ( hour >= 19 and hour < 24):
        speak("Good Evening , Niteesh ")

'"Below function is used to take the input from the user through the help of mic as source "'
def takeCommand():
    # taking the user input as speech and returning string as output
    r = sr.Recognizer()  # will help in recognizing the voice
    with sr.Microphone() as source:
        print( "Listening.... ")
        r.pause_threshold = 1 # doing so with this line we are trying to wait for 1 seconds atleast to have input
        # since this thing can give error so we will use try except block
        audio = r.listen(source)
        

        try:
            print("Recongnizing")
            query = r.recognize_google(audio, language="en-In")
            print("In here")
            print("User Said : - " , query)
            

        except Exception as e:
            return "none"  # we are returning normal string if dont find any thing


        return query.lower()

if __name__ == "__main__":
    while True:
        query = takeCommand()
        
        # gabbar section
        if  query in QuestionEng:
            speak(Text[3])        
        
        elif query in QuestionHindi:
            speak(Text[4])
        
        elif query in NiteeshHindi:
            speak(Text[6])
        
        elif query in NiteeshQuestion:
            speak(Text[5])

        elif  query in AppraisalGabbar:
            speak("Dhanywad!.Sir ji!! Yeh aapki he dain hai..")

        # below section contains the features of the Gabbar
        # google section
        elif 'spotify' in query:
            speak("Ok sir ! Just a Question ? Do you want to search specific artist or song ! Then please let me know???")
            res = takeCommand()
            if 'yes' in res:
                speak("Please tell the song name or the artist")
                res = takeCommand()
                if res :
                    speak("Ok sir ! playing the related song...")
                    path = "https://open.spotify.com/search/" + res
                    web.open(path)

            else:    
                speak("Opening the spotify for you")
                web.open("https://open.spotify.com/")
            

        elif 'on google' in query or 'on chrome' in query:
            Query = query.replace("gabbar search", "")
            query = Query.replace("on google", "")
            speak(f"Searching {query} on google")
            search_on_google(query)

        elif 'wikipedia' in query:
            Query = query.replace("gabbar search" , "")
            query = Query.replace("on wikipedia" , "")
            speak(f"Searching {query} on wikipedia")
            SearchWikipedia(query)
        
        # youtube section
        elif 'on youtube' in query:
            Query = query.replace("gabbar search","")
            query = Query.replace("on youtube","")
            speak(f"searching {query} on youtube...")
            YouTubeSearch(query)

        elif 'play' in query:
            Query = query.replace("gabbar play", "")
            query = Query.replace("on youtube", "")
            PlayOnYoutube(query)
       
        
        # codeforces section
        elif 'on codeforces' in query:
            Query = query.replace("gabbar search", "")
            query = Query.replace("on codeforces", "")
            speak(f"Ok sir , Searching {query} on codeforces....")
            search_on_codeforces(query)
        
        elif 'codeforces profile' in query:
            Query = query.replace("gabbar open my", "")
            query = Query.replace("codeforces profile", "")
            speak(f"Ok sir, Opening yours codeforces profile page....")
            search_on_codeforces("Sinchu.itachi")

        elif 'open codeforces contest page' in query:
            Query = query.replace("gabbar open codeforces contest page", "")
            speak("Ok sir , Opening the contest page")
            search_contest()

        
       

        # leetcode section
        elif 'leetcode profile' in query:
            Query = query.replace("gabbar open", "")
            query = Query.replace("leetcode profile", "")
            speak("Ok sir, Opening yours leetcode profile page")
            LeetCodeProfile()
            
        elif 'open leetcode' in query:
            Query = query.replace("gabbar open", "")
            query = Query.replace("leetcode", "")
            speak("Ok sir, Opening leetcode....")
            OpenLeetCode()

        #linked in section
        elif 'linkedin profile' in query:
            Query = query.replace("gabbar open my linkedin account" , "")
            speak(f"Ok sir.. Opening yours linkedin account")
            OpenProfile()
        
        elif 'open linkedin' in query:
            OpenLinkedIn()

        elif 'on linkedin' in query:
            Query = query.replace("gabbar search" , "")
            query = Query.replace("on linkedin" , "")
            SearchLinkedIn(query)


        # for closing chrome any app 
        elif 'close the chrome' in query:
            query = query.replace("gabbar close the","")
            if 'youtube' in query:
                CloseApp(chrome)
                
            else:   
                CloseApp(query)
        
        # closing all app
        elif 'close' in query:
            speak("Ok sir..")
            Close()

        # doing system task section
        elif 'copy this' in query:
            Query = query.replace("gabbar", "")
            query = Query.replace("copy this", "")
            speak("Ok sir, You said :- ")
            speak(query)

        elif 'open cmd' in query:
            speak("Opening Command Prompt sir")
            OpenCmd()

        elif 'open camera' in query:
            speak("Ok sir, Opening Camera...")
            open_camera()

        elif 'open music' in query:
            speak("Ok sir, Opening Music")
            open_music()
        
        elif 'open notepad' in query:
            speak("Ok sir , Opening Notepad for you")
            OpenNotePad()

        elif 'open sublime' in query:
            speak("Ok sir , Opening the Sublime text editor for you")
            print(Paths['sublime-text'])
            OpenSublime()
        
        elif 'open eclipse' in query:
            speak("Ok sir , Opening Eclipse ide for you sir")
            OpenEclipse()

        
        elif 'open paint' in query:
            speak("Ok sir, opening paint ")
            OpenPaint()
        
        elif 'open ms word' in query:
            speak("Ok sir , opening ms word for you")
            Openmsword()

        elif 'open dev' in query:
            speak("ok sir , opening dev c++ ide")
            devc()
        
        
        elif 'open xamp' in query:
            speak("ok sir , opening xampp control pannel for you")
            Openxamp()
        

        #social media section
        elif 'send message on whatsapp' in query:
            speak("Ok sir..!")

            while True:
                speak("Ok sir !!! Tell me the number to whom you are sending the message")
                number = takeCommand()
                speak(f"Is the number {number} correct sir??")
                res = takeCommand()
                if 'yes' in res:
                    speak("Got the Reciever")
                   
                    while True:
                        speak("What message has to be sent sir!")
                        message = takeCommand()
                        speak(f"This is the message which i will send sir ! {message}")
                        speak("Is it correct ?")
                        res = takeCommand()
                        if 'yes' in res:
                            speak("ok sir")
                            message = message.replace ("gabbar send" , "")
                            send_whatsapp_message(number , message)
                            break
                        
                        else:
                            speak("Lets do it again sir!!")
                            continue
                else:
                    speak("Sorry sir !! You have to try again!!")
                    continue
                break
           
        elif 'open whatsapp' in query:
            speak("Ok sir..")
            speak(Text[2])
            OpenWhatsapp()
        
        elif 'open gmail' in query:
            speak("Ok sir")
            speak(Text[2])
            OpenGmail()
        
        elif 'sheet' in query :
            speak("Ok sir")
            speak("Which s d e sheet you want to open!? Love Babbar's or Striver's!")
            response = takeCommand()
            if response in lovebabbar:
                speak("Ok sir , Openin Love babbar's s d e sheet")
                OpenSDESheet()
            elif response in striver:   
                speak("Ok sir , opening striver's S D E SHEET")
                web.open("https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/")


        #keyboard functionality 
        elif 'switch' in query:
            speak("Ok sir..")
            SwitchTabs()
        
        elif 'task manager' in query:
            speak("Ok sir..")
            OpenTaskManager()
        
        elif IpAdd[0] in query or IpAdd[1] in query:
            i = 0
            flag = 0
            while i < 3:
                speak("Tell me one thing which only you I know about you sir??")
                res = takeCommand()
                if Check[0] in res:
                    flag = 1
                    find_my_ip()
                    break
            
                else:
                    speak("Wrong information.. You got 2 more attempt after that the system will be shut")
                    i += 1

            if not flag:
                speak("You are not authorised to have this details!! And using me is only allowed to Niteesh sir !! So i m shutting down")
                keyboard.press_and_release('alt+f4')

                

        # new and other stuffs
        elif News[0] in query:
            speak("Ok sir..")
            get_latest_news()

        elif News[1] in query:
            speak("Ok sir..")
            get_latest_news()

        elif Weather[0] in query:
            speak("Ok sir...")
            speak("Please enter the city name whose whether you want ")
            name = input ("Enter the city name :- ")
            speak(f"finding the weather report of city {name}")
            speak(Text[2])
            get_weather_report(name)

        elif Weather[1] in query:
            speak("Ok sir...")
            speak("Please enter the city name whose whether report you want ")
            name = input ("Enter the city name :- ")
            speak(f"finding the weather report of city {name}")
            speak(Text[2])
            get_weather_report(name)
        
        elif 'joke' in query:
            speak("Ok sir!! Ready for the laughter therapy..")
            get_random_joke()

        # below section is for setting change
        elif 'speak slowly' in query:
            speak("..Oh , I see ..... Ok sir ! Tell me what is causing you the problem .. My Speech or Volume")
            response = takeCommand()
            if 'speech' in response:
                speak("Ok..Sir.. Roger That..")
                while True:
                    volume = x - 10
                    engine.setProperty('rate', volume)
                    speak("Is it fine sir??")
                    res = takeCommand()
                    if 'ok' in res:
                        speak("Ok sir , my speech rate has been reset for you....")
                        break
                
                    elif 'not fine' in res:
                        x -= 10
                        speak("Ok sir ... Reducing it...")  
            elif 'nothing' in respons:
                speak("Ok sir! Seems everything is fine.")
        

        # below section is for the greeting and further responses
        elif query in AskingGabbarHindi:
            speak(IntroText[5])

        elif query in AskingGabbarEng or 'thankyou' in query:
            speak(IntroText[6])

        elif query in OpeningCalls:
            wish()
            speak(IntroText[0])
        
        elif query in OpeningCallsResponse1Eng:
            speak(IntroText[2])
        
        elif query in OpeningCallsResonse1Hindi:
            speak(IntroText[7])

        elif query in OpeningCallsResponse2Eng:
            speak(IntroText[3])   
        
        elif query in OpeningCallsResponse2Hindi:
            speak(IntroText[8])
        
        elif query in OpeningCallsResponse3Eng:
            speak(IntroText[4])
        
        elif query in OpeningCallsResponse3Hindi:
            speak(IntroText[9])

        #random statements
        elif 'apna time aaega' in query:
            speak("Jaroor sir !! Apna time aaega..")




        # closing or signing off
        elif query in CloseGabbar:
            speak("Ok sir , hope to see you soon. Bye!!")
            keyboard.press_and_release('alt + f4')
            exit(0)
        
        elif 'take rest' in query:
            speak("..Thankyou sir !! ..You to take rest ..... ")
            keyboard.press_and_release("alt + f4")
            exit(0)   
        
        

        # this is to handle only if gabbar is called    
        elif 'Gabbar' in query or 'gabbar' in query:    
            speak(IntroText[1]) 

           
        

        # if nothing matches aur unbound values while capturing voice from the user
        else:
            SearchBox.append(query)
            print(SearchBox)
            speak("Sorry sir , but I could not understand") 
                   

    

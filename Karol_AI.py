import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
        
    elif hour >=12 and hour<18:
        speak("Good AfterNoon!")
        
    else :
        speak("Good Evening!")

    speak("Hey! I am karol , your persional assistant. How may I help you?")

def takeCommand():
   
    """it takes microphone input from user and returns  strings output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold= 400
        audio= r.listen(source)
    try:
        print("Recoznizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")


    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'Password')
    server.sendmail('mail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query= takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query= query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open Gmail' in query:
            webbrowser.open("mail.gooogle.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif "who made you" in query:
            speak("Kush is my creator ,He made me as a project")
            
        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs[0])    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            
            strTime = date
            time.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        # elif 'open chrome' in query:
        #     chromepath = 

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "reciver@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")    

        elif 'exit' in query:
             exit()
                

import sys
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import string
import smtplib
import speedtest
from googletrans import Translator, constants
import random
from password_generator import PasswordGenerator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    # customized according to indian standard time
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning")
        print("Good Morning")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon")
        print("Good Afternoon")

    elif hour >= 17 and hour < 21:
        speak("Good Evening")
        print("Good Evening")

    else:
        speak("Good Night")
        print("Good Night")

    speak("How may I help you sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recoganizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"

    return query


def myipl():
    speak('What do you want to search?')
    speak('You can ask about matches,stats or points table.')
    myq = takecommand().lower()
    if "matches" in myq:
        webbrowser.open('https://www.iplt20.com/matches', new=0)
    elif "stats" in myq:
        webbrowser.open('https://www.iplt20.com/stats/2023', new=0)
    elif "points" in myq:
        webbrowser.open('https://www.iplt20.com/points-table/men/2023', new=0)


def iwantweather():
    speak('please tell your query?')
    loc = takecommand().lower()
    webbrowser.open(
        f'https://www.accuweather.com/en/search-locations?query={loc}', new=0)


def mySearch():
    speak('What word do you want to search?')
    word = takecommand().lower()
    webbrowser.open(f'https://www.dictionary.com/browse/{word}', new=0)


def mytranslate():
    speak('What do you want to translate?')
    val = takecommand().lower()
    webbrowser.open(
        f'https://translate.google.com/?hl=en&sl=auto&tl=en&text={val}&op=translate', new=0)


if __name__ == '__main__':
    wishme()
    # greet the user based on time (IST),
    # wikipedia, youtube, google, gfg, lms,
    # gmail, calculator, time, unit converter,
    # maps, dictionary, translate, otp and password generator,
    # ipl info, internet connection speed, program shutdown command

    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("https://youtube.com/", new=0)

        elif "google" in query:
            webbrowser.open("https://www.google.com/", new=0)

        elif "gfg" in query:
            webbrowser.open("https://www.geeksforgeeks.org/", new=0)

        elif "lms" in query:
            webbrowser.open("https://lms.thapar.edu/moodle/", new=0)

        elif "gmail" in query:
            webbrowser.open("https://www.google.com/gmail/about/", new=0)

        elif "time" in query:
            strTime = datetime.datetime.now().strftime('%Hhours:%Mminutes:%Sseconds')
            speak(f'The current time is {strTime}')

        elif "ipl" in query:
            myipl()

        elif "otp" in query:
            speak('You can use this as your OTP')
            for i in range(6):
                number = random.randrange(0, 10)
                speak(number)
                print(number, end=' ')

            print()

        elif "password" in query:
            speak('You can use this as yout password')
            pwo = PasswordGenerator()
            pwo.minlen = 10
            pwo.maxlen = 10
            pwo.minuchars = 2
            pwo.minlchars = 3
            pwo.minnumbers = 2
            pwo = pwo.generate()
            print(pwo)

        elif "calculator" in query:
            webbrowser.open("https://www.calculator.net/", new=0)

        elif "maps" in query:
            webbrowser.open('https://www.google.com/maps/', new=0)

        elif "weather" in query:
            iwantweather()

        elif "converter" in query:
            webbrowser.open('https://www.unitconverters.net/', new=0)

        elif "dictionary" in query:
            mySearch()

        elif "translate" in query:
            mytranslate()

        elif "speed" in query:
            speak('Yes,Please wait a moment')
            st = speedtest.Speedtest()
            d = st.download()/(10**6)
            u = st.upload()/(10**6)
            print(f'Download speed {"{0:.3f}".format(d)} Mb/s')
            print(f'Upload speed {"{0:.3f}".format(u)} Mb/s')
            speak(f'Download speed {"{0:.3f}".format(d)} megabits per second')
            speak(f'Upload speed {"{0:.3f}".format(u)} megabits per second')

        if "system" in query:
            speak("Shut Down")
            exit()

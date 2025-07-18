import pyttsx3
import speech_recognition as sr
import random
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voice.id)
    engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content =" "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio,language='en-in')
            print("You said........ = " + content)
        except Exception as e:
            print("Buddy Try again...")

    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome,How can i help you.")
        elif "play music" in request:
            speak("play secrets ")
            song = random.randint(1,5)
            if song == 1:
              webbrowser.open("")
            elif song == 2:
                 webbrowser.open("https://www.youtube.com/watch?v=ziTHTlmPdhQ&list=RDziTHTlmPdhQ&start_radio=1")
            elif song == 3:
                 webbrowser.open("https://www.youtube.com/watch?v=-2RAq5o5pwc&list=RD-2RAq5o5pwc&start_radio=1")


main_process()
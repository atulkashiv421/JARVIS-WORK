import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import os  # Required for launching Windows apps

# Speak function using pyttsx3
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.setProperty("rate", 150)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

# Voice command input using microphone
def command():
    content = " "
    while content.strip() == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)  # improves accuracy
            audio = r.listen(source)
        try:
            content = r.recognize_google(audio, language='en-in')
            print("You said: " + content)
        except Exception as e:
            print("Buddy, try again...")
    return content

# Main assistant process loop
def main_process():
    while True:
        request = command().lower()

        if "hello jarvis" in request:
            speak("Hello sir, how can I help you?")

        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=ziTHTlmPdhQ&list=RDziTHTlmPdhQ&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=ziTHTlmPdhQ&list=RDziTHTlmPdhQ&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=-2RAq5o5pwc&list=RD-2RAq5o5pwc&start_radio=1")

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + now_time)

        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + now_date)

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task:
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
            else:
                speak("Please say the task after saying new task.")

        elif "speak task" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                    if tasks:
                        speak("Work we have to do today is: " + tasks)
                    else:
                        speak("You have no tasks today.")
            except FileNotFoundError:
                speak("No task file found.")

        elif "show work" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                    if tasks:
                        notification.notify(
                            title="Today's Work",
                            message=tasks
                        )
                    else:
                        speak("You have no tasks written down.")
            except FileNotFoundError:
                speak("Task file not found.")

        elif "open camera" in request:
            speak("Opening camera")
            os.system("start microsoft.windows.camera:")

        elif "open" in request:
            app = request.replace("open", "").strip()
            if app:
                speak("Opening " + app)
                webbrowser.open(f"https://www.{app}.com")
            else:
                speak("Please specify what to open.")

# Start the assistant
main_process()

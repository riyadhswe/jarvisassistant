import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import winshell
import wolframalpha

engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty('volume', 10.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is : ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    print(".....................................................")
    print(".......................Jarvis Robot ....................")
    print(".....................................................")
    # time()
    # date()
    # Greeting
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir!!!!!!")
    speak("Jarvis at your service.Please tell me how can i help you today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............................................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconizing...........................................")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print(".....................................................")
        print("....................Say something....................")
        print(".....................................................")
        return "None"
    return query


def cpu():
    print(".....................................................")
    print(".........................Cpu.........................")
    print(".....................................................")
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    print('CPU is at     :', usage)
    print("Battery is at :", battery.percent)
    speak('CPU is at' + usage)
    speak("Battery is at")

    speak(battery.percent)


def joke():
    print(".....................................................")
    print(".........................joke........................")
    print(".....................................................")
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishme()
    while True:
        query = TakeCommand().lower()  # all command stored in lower Case
        if 'time' in query:  # tell us time
            print(time())
            time()


        elif 'date' in query:  # tell us date
            print(date())
            date()

        elif 'wikipedia' in query:  # find in wikipedia
            import wikipedia

            speak("Searching")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(".....................................................")
            print("......................wikipedia......................")
            print(".....................................................")
            print(result)
            speak(result)

        elif 'joke' in query:
            joke()





        elif 'search youtube' in query:  # Open chrome
            print(".....................................................")
            print("...................search youtube....................")
            print(".....................................................")
            speak("What should I search?")
            print("What should I search?")
            search_terms = TakeCommand().lower()
            speak("Here i go to youtube")
            wb.open('https://www.youtube.com/results?search_query=' + search_terms)

        elif 'search google' in query:  # Open chrome
            print(".....................................................")
            print("...................search google.....................")
            print(".....................................................")
            speak("What should I search?")
            print("What should I search?")
            search_terms = TakeCommand().lower()
            speak("Here i go to Google")
            wb.open('https://www.google.com/search?q=' + search_terms)

        elif 'cpu' in query:  # Open cpu
            cpu()

        elif 'go offline' in query:  # Open cpu
            speak("Going offline Sir")
            quit()

        elif 'how are you' in query:  # Open cpu
            speak("I am fine and you?")


        elif 'how are you' in query:  # Open cpu
            speak("I am fine and you?")

        elif 'who are you' in query:  # Open cpu
            speak("I am Jarvis")




        elif 'write a note' in query:
            print(".....................................................")
            print(".....................write a note....................")
            print(".....................................................")
            speak("What should i write,Sir?")
            notes = TakeCommand()
            file = open('file.txt', 'w')
            file.write(notes)
            speak("Done taking Note Sir")

        elif 'my note' in query:
            print(".....................................................")
            print(".....................Your Note is ...................")
            print(".....................................................")
            speak('Your Note is : ')
            file = open('file.txt', 'r')
            print(file.read())

        elif 'screenshot' in query:
            print(".....................................................")
            print("....................screenshot Done .................")
            print(".....................................................")
            pyautogui.hotkey('win', 'printscreen')
            speak('Done Sir')

        elif 'folder' in query:
            print(".....................................................")
            print("....................screenshot Open .................")
            print(".....................................................")
            pyautogui.hotkey('win', 'printscreen')
            msword = 'C:/Users/riyad/Pictures/Screenshots'
            os.startfile(msword)
            speak('open  Sir')


        elif 'open youtube' in query:
            speak('okay')
            wb.open('www.youtube.com')

        elif 'open facebook' in query:
            speak('okay')
            wb.open('www.facebook.com')


        elif 'open google' in query:
            speak('okay')
            wb.open('www.google.co.in')


        elif 'creator' in query:
            speak("Riyadh")


        elif 'open gmail' in query:
            speak('okay')
            wb.open('www.gmail.com')


        elif 'shutdown' in query:
            speak('okay')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.press('enter')




        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
            except:
                speak("Recycle Bin already empty")
                TakeCommand()
        elif "what is your name" in query:
            speak("Jarvis 1.0")

        elif "what is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()


        elif "where is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "who is" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "where we are actually right now" in query:
            try:
                speak("Kurigram , Rangpur ,Bangladesh")
            except:
                print("No results")
                TakeCommand()



        elif "how" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "can" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "who" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()

        elif "do you" in query:
            try:
                client = wolframalpha.Client("7PLQXV-UVR3WQPTYU")
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("No results")
                TakeCommand()



        # calculation
        elif "calculate" in query:
            try:
                app_id = "7PLQXV-UVR3WQPTYU"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except:
                TakeCommand()



        elif "creator" in query:
            speak("Riyadh")

        elif "introduce yourself" in query:
            speak("I am Jarvis 1.0 , Personal AI assistant , "
                  "I am created by Riyadh ")

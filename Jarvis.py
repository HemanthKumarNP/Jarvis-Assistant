import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

#engine.say('Jarvis is ready')
#engine.say('How can I help You?')
#engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def user_speech():
    command=""
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis','')
                #talk(command)
    except:
        pass
    return command

def run_jarvis():
    command = user_speech()
    print(command)
    song = command.replace('play','')
    if 'play' in command:
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' +time)
    elif 'search' in command:
        person = command.replace('search','')
        try:
            info = wikipedia.summary(person, 4)
            print(person)
            try:
                # Try to print info using sys.stdout to handle Unicode characters
                sys.stdout.buffer.write(info.encode('utf-8'))
            except UnicodeEncodeError:
                print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on {}.".format(info))
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in relationship with wifi')
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk("Sorry i didn't Understood")

while True:
    run_jarvis()
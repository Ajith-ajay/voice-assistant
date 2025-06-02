from voice_engine import speak
import speech_recognition as sr
import datetime
import shutil
import smtplib

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
 
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
 
    else:
        speak("Good Evening Sir !")  
 
    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)
    

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    print("Welcome Mr.",uname)
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    # print("#####################".center(columns))
    # print("Welcome Mr.", uname.center(columns))
    # print("#####################".center(columns))
    
    speak("How can i Help you, Sir")


def takeCommand():
    """
    Listens to the user's voice input and converts it to text.
    Returns 'None' if the speech was not recognized.
    """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        # Adjust to ambient noise for better recognition
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1 
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "None"

    return query

 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()
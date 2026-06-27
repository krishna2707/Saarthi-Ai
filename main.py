import speech_recognition as sr
import pyttsx3
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from websites import websites
 


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-playback-state user-modify-playback-state"
    )
)


def speak(text):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[0].id)
     engine.say(text)
     engine.runAndWait()
     print("hello")
     

def browse(tab):
      if tab in websites:
        speak(f"Opening {tab} ")
        webbrowser.open_new_tab(websites[tab])
      else:
          speak("Website doesnt exist")

def song(songname):
    try:
        devices = sp.devices()
        print(devices)
        results = sp.search(q=songname, type="track", limit=3)
        track = results["tracks"]["items"][0]
        uri = track["uri"]
        sp.start_playback(uris=[uri])
        speak(f"Playing {songname}")
    except:
        print("No device is connected")

        
def time():
    hour=datetime.now().strftime("%H")
    minutes=datetime.now().strftime("%M")
    speak(f"The current time is {hour} hours and {minutes} minutes")
     
def date():
     todaydate=datetime.now().strftime("%d")
     day=datetime.now().strftime("%A")
     year=datetime.now().strftime("%Y")
     month=datetime.now().strftime("%B")
     speak(f"Today is {day} {todaydate} of {month} of year {year}")

     

def process(command):
    if(command.startswith("play")):
        song(command.removeprefix("play").strip())
    elif(command.startswith("open")):
        browse(command.split(" ")[1])
    elif("time" in command):
         time()
    elif("date" in command):
         date()


if __name__=="__main__":
        try:
         r = sr.Recognizer()
         while(True):
            with sr.Microphone() as source:
              print("Recognising!")
              audio = r.listen(source)
            wakeword= r.recognize_google(audio)
            print(wakeword)
            if(wakeword.lower()=="krishna"):
               speak("Boliye")
               with sr.Microphone() as source:
                 print("Speak")
                 audio = r.listen(source)
                 command=r.recognize_google(audio)
                 print(command)
                 process(command.lower())

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
import speech_recognition as sr
import pyttsx3
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-playback-state user-modify-playback-state"
    )
)
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    devices = sp.devices()
    print(devices)
    audio = r.listen(source)

websites = {
    "youtube": "https://www.youtube.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "claude": "https://claude.ai",
    "chatgpt": "https://chatgpt.com",
    "instagram": "https://www.instagram.com",
    "github": "https://github.com",
    "leetcode": "https://leetcode.com",
    "gmail": "https://mail.google.com"
}

def browse(tab):
      engine.say(f"Opening {tab} ")
      engine.runAndWait()
      webbrowser.open_new_tab(websites[tab])

def song(songname):
    try:
        results = sp.search(q=songname, type="track", limit=5)
        track = results["tracks"]["items"][0]
        uri = track["uri"]
        sp.start_playback(uris=[uri])
        engine.say(f"Playing {songname}")
        engine.runAndWait()
    except:
        print("No device is connected")

def process(command):
    if(command.startswith("play")):
        song(command.removeprefix("play").strip())
    elif(command.startswith("open")):
        browse(command.split(" ")[1])

if __name__=="__main__":
        try:
            command= r.recognize_google(audio)
            print(command)
            process(command.lower())

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
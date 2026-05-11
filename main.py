# Simple Voice Assistant in Python

import os
import ctypes

# Suppress ALSA error messages 
'''
	Hides ALSA (Linux sound system) error messages
	normally flood the terminal when Python programs use audio libraries 
	like speech_recognition, PyAudio, or pyttsx3.
'''
ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
                                       ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
def py_error_handler(filename, line, function, err, fmt): pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
try:
    asound = ctypes.cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(c_error_handler)
except:
    pass

# Import necessary libraries
import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Setting up tuntun mausi
def setup_tuntun_voice():
    engine.setProperty('voice', 'en+f3')  # Female voice
    engine.setProperty('rate', 155)       # Speaking speed
    engine.setProperty('volume', 1.0)     # Max volume

# Function for speaking using pyttsx3 
def speak(text):
    setup_tuntun_voice() 
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    # First check normal conversation
    """
    Handles casual conversation before command execution.
    Returns True if conversation was handled, False if not.
    """
    c_lower = c.lower()

    # Greetings
    if "hi" in c_lower or "hello" in c_lower or "hey" in c_lower:
        speak("Namaste ji!")
        return True

    elif "how are you" in c_lower:
        speak("Main ekdum badhiya!!")
        return True

    elif "how was your day" in c_lower or "how has your day been" in c_lower:
        speak("My day was wonderful, especially now that I'm talking to you!")
        return True

    elif "what are you doing" in c_lower:
        speak("Making laddoos and helping you out, as always!")
        return True

    elif "who are you" in c_lower:
        speak("I am Laddoo specialist aur aapki pyari assistant!")
        return True

    elif "thank you" in c_lower:
        speak("Arey koi baat nahi ji!")
        return True

    elif "bye" in c_lower:
        speak("Byeeee jii")
        
    # Commands 
    elif "open google" in c_lower:
        webbrowser.open("https://www.google.com")
        speak("Google khol diya!")

    elif "open youtube" in c_lower:
        webbrowser.open("https://www.youtube.com")
        speak("YouTube khol diya!")

    elif "open linkedin" in c_lower:
        webbrowser.open("https://www.linkedin.com")
        speak("LinkedIn khol diya!")

    elif "open github" in c_lower:
        webbrowser.open("https://www.github.com")
        speak("GitHub khol diya!")

    elif c_lower.startswith("search for"):
        query = c_lower.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"{query} search kar diya!")

    elif "tell me a joke" in c_lower:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "what's the time" in c_lower or "what is the time" in c_lower:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"curremtly the time is {current_time}")

    elif "what's the date" in c_lower or "what is the date" in c_lower:
        from datetime import datetime
        today = datetime.today()
        current_date = today.strftime("%d %B %Y")
        speak(f"today is {current_date}")

    elif "exit" in c_lower or "quit" in c_lower:
        speak("Alvida! Aapka din shubh ho!")
        exit(0)

    else:
        speak("Sorry, I didn't understand that command. Please try again.")
        return
    

if __name__ == "__main__":
    speak("Tuntun Mausi is my name...")
    while True:
        # Initialize the speech recognizer
        #Listen for the word "Tuntun Mausi"
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Google
        try:
            # Python accessing you Microphone ie source
            with sr.Microphone() as source:
                # Adjusting background noise
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                # Recording you voice (waits 2 sec for speech, then records for 5 sec)
                audio = r.listen(source,timeout = 2,phrase_time_limit = 5)

            # Converting the voice to text     
            word = r.recognize_google(audio)
            # Activating Assistant
            if "tuntun mausi" in word.lower():
                speak("Ha ji!")
                speak("Tuntun Mausi is ready to help you...")
                # Listen for the command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.3)
                    audio = r.listen(source, timeout=10, phrase_time_limit=15)
                    command = r.recognize_google(audio)
                # Process the Command using processCommand function 
                processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


import text_to_speech
import speech_to_text
import datetime
import webbrowser
import os
import wikipedia
import pyjokes
import random
import urllib.parse

# =========================
# COMMAND FUNCTIONS
# =========================

def greet():
    return "Hey! How can I help you?"

def my_name():
    return "My name is Virtual Assistant."

def good_morning():
    return "Good morning!"

def tell_time():
    now = datetime.datetime.now()
    return f"The time is {now.hour} hour {now.minute} minute."

def tell_date():
    today = datetime.datetime.now().date()
    return f"Today's date is {today}."

def shutdown():
    os.system("shutdown /s /t 1")
    return "Shutting down the system."

def restart():
    os.system("shutdown /r /t 1")
    return "Restarting the system."

def open_google():
    webbrowser.open("https://google.com")
    return "Google is open."

def open_youtube():
    webbrowser.open("https://youtube.com")
    return "YouTube is open."

def play_music():
    webbrowser.open("https://gaana.com")
    return "Enjoy your music on Gaana.com"

def tell_joke():
    return pyjokes.get_joke()

def inspirational_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Dream big and dare to fail.",
        "Keep going, you're doing great!"
    ]
    return random.choice(quotes)

def open_notepad():
    os.system("notepad")
    return "Opening Notepad."

def open_calculator():
    os.system("calc")
    return "Opening Calculator."

def wikipedia_search(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "Sorry, I couldn't find anything on Wikipedia."

def google_search(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Here are the Google search results for '{query}'."

def youtube_search(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Here are YouTube search results for '{query}'."


# =========================
# COMMAND MAPPING
# =========================

commands = {
    ("hello", "hi", "hye"): greet,
    ("what is your name",): my_name,
    ("good morning",): good_morning,
    ("time", "current time"): tell_time,
    ("date", "today date"): tell_date,
    ("shutdown",): shutdown,
    ("restart",): restart,
    ("google", "open google"): open_google,
    ("youtube", "open youtube"): open_youtube,
    ("play music", "song"): play_music,
    ("joke",): tell_joke,
    ("quote",): inspirational_quote,
    ("open notepad",): open_notepad,
    ("open calculator",): open_calculator,
}


# =========================
# MAIN ACTION FUNCTION
# =========================

def Action(send=None):
    if send:
        user_data = send.lower()
    else:
        text_to_speech.text_to_speech("Listening...")
        user_data = speech_to_text.speech_to_text().lower()

    # Wikipedia search
    if "wikipedia" in user_data:
        query = user_data.replace("wikipedia", "").strip()
        response = wikipedia_search(query)
        text_to_speech.text_to_speech(response)
        return response

    # YouTube search
    if "play" in user_data and "youtube" in user_data:
        query = user_data.replace("play", "").replace("on youtube", "").strip()
        response = youtube_search(query)
        text_to_speech.text_to_speech(response)
        return response

    # Google search fallback
    if user_data.startswith("search for"):
        query = user_data.replace("search for", "").strip()
        response = google_search(query)
        text_to_speech.text_to_speech(response)
        return response

    # Loop through commands dictionary
    for triggers, func in commands.items():
        if any(trigger in user_data for trigger in triggers):
            response = func()
            text_to_speech.text_to_speech(response)
            return response

    # If nothing matches, fallback to Google search
    response = google_search(user_data)
    text_to_speech.text_to_speech("Here are some results from Google.")
    return response

import pyttsx3 

def text_to_speech(text):
    
    engine = pyttsx3.init()
# Set speaking rate
    rate = engine.getProperty('rate')     #speaking rate
    engine.setProperty('rate',rate-70) #higher value- slower rate

# List available voices
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(i, voice.name, voice.id)

# Set female voice (choose an index based on the list)
    engine.setProperty('voice', voices[2].id)  # usually index 1 is female, but it can vary
    engine.say(text)
    engine.runAndWait()

   
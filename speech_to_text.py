import speech_recognition as sr

#converting voice into text
def speech_to_text(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        audio = r.listen(source) 
        r.adjust_for_ambient_noise(source, duration=1)  # Optional: reduce background noise
    try: 
        voice_data = "" 
        voice_data = r.recognize_google(audio) 
        print(voice_data) 
        return voice_data 
    except sr.UnknownValueError: 
        print("Voice not recognized") 
    except sr.RequestError: 
        print("Requesting your voice")
    

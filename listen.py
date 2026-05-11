import speech_recognition as sr

def listen_command():
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    
    except Exception:
        return "Could not understand audio"


if __name__ == "__main__":
    
    print(listen_command())
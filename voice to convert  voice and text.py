
import pyttsx3
import speech_recognition as sr

listener=sr.Recognizer()

speak=pyttsx3.init()

def says(Text_mod):

    speak.say(Text_mod)   
    
    speak.runAndWait()

try:
    
    with sr.Microphone() as source:
        
        print("Listening....")
        
        voice=listener.listen("#########")
        Text=listener.recognize_google(voice)
        
        
        
        if "hey dude" in Text:
            if "voice" in Text:
                
                k=Text.replace("hey dude","")
                Text_mod=k.replace("voice","")
                print(Text_mod)
                says(Text_mod)
            
            
            else:
                k=Text.replace("hey dude","")
                print(k)    

except:
    pass    




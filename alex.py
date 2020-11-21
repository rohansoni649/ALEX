import pyttsx3
import datetime
import wikipedia

#to extract the current hour and wish accordingly
hour = datetime.datetime.now().hour
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning")
elif hour>=12 and hour<18:
    pyttsx3.speak("Good Afternoon")
else:
    pyttsx3.speak("Good Evening")

pyttsx3.speak("Hi I am Alex. How May I help you?")

def takeCommand():
    #it takes command from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        #r.pause_threshold = 1
        audio = r.listen(source)
#try-catch will be heplful if the voice is not properly heard by the API
    try:
        print("recognizing......")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print("Can you please say that again......")
        return "None"
    return query
    
if __name__ == "__main__":
    while True:
        #lower case will be taked into consideration for seaching results properly
        query = takeCommand().lower()
        
        #to search in wikipedia 
        if 'wikipedia' in query:
            pyttsx3.speak("Searching wikipedia....")
            #replace the wikipeadia keyword with the blank
            query = query.replace("wikipedia","")
            #extract 2 sentences from the wikipedia page summary
            results = wikipedia.summary(query, sentences=2)
            pyttsx3.speak("According to wikipedia....")
            print(results)
            pyttsx3.speak(results)

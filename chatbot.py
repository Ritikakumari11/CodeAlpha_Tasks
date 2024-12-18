import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia  
import webbrowser
import os
import pyjokes  
import requests  
import sys

# Reconfigure the output encoding to UTF-8 to avoid encoding errors in Windows console
sys.stdout.reconfigure(encoding='utf-8')

engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Speak the provided audio string."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Wish the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
        
    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis. Please tell me how may I assist you?")

def takeCommand():
    """Take voice input from the user and return it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def tellJoke():
    """Tell a random joke."""
    try:
        joke = pyjokes.get_joke()
        speak(joke)
    except Exception as e:
        speak("Sorry, I couldn't fetch a joke at the moment.")

def fetchWeather(city):
    """Fetch the current weather for a specified city."""
    try:
        api_key = "your_openweather_api_key"  # Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            weather = data["main"]
            temp = weather["temp"]
            pressure = weather["pressure"]
            humidity = weather["humidity"]
            description = data["weather"][0]["description"]
            
            speak(f"The current temperature in {city} is {temp} degrees Celsius.")
            speak(f"The weather is described as {description} with a humidity of {humidity}% and pressure of {pressure} hPa.")
        else:
            speak("City not found. Please try again.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather details at the moment.")

def searchWikipedia(query):
    """Search and return a summary from Wikipedia."""
    try:
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)  # Output the results safely in the console
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("The query is ambiguous. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No results found. Try another query.")
    except Exception as e:
        speak("I couldn't fetch information. Please try again.")
        print(f"Error: {e}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'hello' in query:
            speak("Hello sir. Please tell me how may I help you now!") 
            
        elif 'wikipedia' in query:
            speak("What should I search on Wikipedia?")
            query = takeCommand().lower()  # Ask the user for what to search for
            if query != "none":
                searchWikipedia(query)
            else:
                speak("I didn't understand your query. Please try again.")
                
        elif 'open youtube' in query:
            speak("What should I search on YouTube?")
            search_query = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            
        elif 'open google' in query:
           speak("What should I search on Google?")
           search_query = takeCommand()
           webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'tell me a joke' in query:
            speak("A Random Joke Is this one:")
            tellJoke()
            
        elif 'weather' in query:
            speak("Please tell me the city name.")
            city_name = takeCommand()
            fetchWeather(city_name)
            
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, Sir!. Have a great day!")  
            break
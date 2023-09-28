import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
from openaitest import text_to_speech

def ai(prompt):
    openai.api_key = apikey
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text= (response["choices"][0]["text"]).strip()
    with open(f"hello.txt", "w") as f:
        f.write(text)
    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("On it.")
            query = r.recognize_google(audio,language="en-in")
            print(f"You Said:{query}")
            return query
        except Exception as e:
            return "I didn't get it, Say it again."

def say(text):
    os.system(f"say {text}")

if __name__=='__main__':
    say("I am here, what is it?")
    x = 1
    while x:
        print("Listening...")
        query = takeCommand()
        web = query.split()
        if len(web)==2:
            if f"Open {web[1]}".lower() in query.lower():
                webbrowser.open(F"https://{web[1]}.com")
                say(f"Opening {web[1]} Now")
                x = 0
        if "app" in query.lower() or "open" in query.lower():
            os.system(f"open /System/Applications/{web[1]}.app")
        if "Exit".lower() in query.lower():
            x = 0
        say(query)
        if "hello".lower() in query.lower():
            ai(query)
            file_object = open("hello.txt", "r")
            contents ="GPT"+ file_object.read() 
            print(contents)
            text_to_speech(contents)
            # say(answer)

    say("See you again, Bye.") 
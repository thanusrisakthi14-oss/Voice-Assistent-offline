import speech_recognition as sr
import pyttsx3
import asyncio
from googletrans import Translator

def speak(text,language='en'):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    voices=engine.getProperty("voices")
    if language == "en":
        engine.getProperty("voices",voices[0].id)
    else:
        engine.getProperty("voices",voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Speak in english pls....")
        audio=recognizer.listen(sourse)
    try:
        print("....")
        text=recognizer.recognize_google(audio,language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"API Error{e}")

async def translate_text(text,target_language="es"):
    translator=Translator()
    translation=await translator.translate(text,des=target_language)
    print(f"Translated Text: {translation.text}")
    return translation.text


def display_language_op():
    print("Avaliable Languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print(" 4.Bengali (bn)")
    choice=input("Enter the target language (1-4): ")
    language_dict={
        "1":"hi"
        "2":"ta"
        "3":"te"
        "4":"bn"
    }

    return language_dict.get(choice,"es")
async def main():
    target_language=display_language_op()
    orginal_text=speech_to_text()
    if orginal_text:
        translated_text=await translate_text(orginal_text,target_language=target_language)
        speak(translated_text,languages="en")
        print("Translated spoken out.....")


if __name__=="__main__":
    asyncio.run(main())        

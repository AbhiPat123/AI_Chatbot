# Reference and thanks to: https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/

# PCKAGES TO INSTALL:
    # - Numpy               - basic functionality on numbers
    # - SpeechRecognition   - for text to Speech
    #    - pipwin       - then install pyAudio using 'pipwin install pyaudio'
    #       - pyAudio          - to work with recognizer
    # - gTTS                - speech to text and speak it out
    # - transformers        - to build language models
    # - tensorflow          - ""

import numpy as np

import speech_recognition as sr

from gtts import gTTS
import os

import datetime
import time

from messages_string import *

# Chatbot class
class ChatBot():
    # constructor
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name

    def get_text(self):
        return self.text

    # bot's way to convert speech to text
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("Listening...")
             audio = recognizer.listen(mic)
        try:
            # Sphinx, Google, Google Cloud, Wit.ai, Bing, Azure, Houndify, IBM - each has their own recognize_...(audio) function
            # NOTE:- each of them has different number of parameters like credentials to use their service
            self.text = recognizer.recognize_google(audio)      # uses Google
            print("Your Bot " + self.name + " --> ", self.text)
        #except:
        #    print("Your Bot " + self.name + " -->  There is an ERROR!")
        # better exception that are not needed for now
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio. Speak loud and clear!")
        #except sr.RequestError as e:
        #    print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # bot's way to convert speech to text
    @staticmethod
    def text_to_speech(text):
        # convert the text to english voice (lang and slow are by default the values shown here)
        speaker = gTTS(text=text, lang="en", slow=False)

        # save spoken mp3 file in current directory
        speaker.save("res.mp3")

        # start mp3 player
        os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
        # wait for the system to start mp3 app
        time.sleep(1)
        # finally remove mp3 file
        os.remove("res.mp3")

    # a function that wake's up bot for use
    # text - a string of message from user
    def wake_up(self, text):
        return True if self.name.lower() in text.lower() else False

    # bot gives the current time
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

# Start execution
if __name__ == "__main__":
    # create a Dev bot
    dev_bot = ChatBot(name="Dev")

    while True:

        # convert speech to text if anything is spoken
        dev_bot.speech_to_text()

        try:
            # get the text heard by dev_bot
            dev_bot_txt = dev_bot.get_text()
        except:
            continue

        # wake up the Dev bot if it hears Dev in text
        if dev_bot.wake_up(dev_bot_txt) is True:
            res = "Hello I am " + dev_bot.name + " the AI chatbot, what can I do for you?"
        # give the time if that is asked
        elif "time" in dev_bot_txt.lower():
            res = dev_bot.action_time()
        # say wecome if Thanks is conveyed
        elif any(i in dev_bot_txt.lower() for i in req_messages["thank"]):
            res = np.random.choice(resp_messages["welcome"])
        else:
            res = ""

        # convert to speech only if it has some text to speak out
        if res:
            dev_bot.text_to_speech(res)

        # reset result variable
        res = ""

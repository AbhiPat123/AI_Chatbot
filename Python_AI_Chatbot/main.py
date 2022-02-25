# Reference and thanks to: https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/

# PCKAGES:
    # - Numpy               - basic functionality on numbers
    # - SpeechRecognition   - for text to Speech
    #    - pyAudio          - to work with recognizer
    #        - pipwin       - then install pyAudio using 'pipwin install pyaudio'
    # - gTTS                - speech to text and speak it out
    # - transformers        - to build lanugage models
    # - tensorflow          - ""

import numpy as np

import speech_recognition as sr



# Chatbot class
class ChatBot():
    # constructor
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name

    # bot's way to convert speech to text
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("Listening to you speak...")
             audio = recognizer.listen(mic)
        try:
            # Sphinx, Google, Google Cloud, Wit.ai, Bing, Azure, Houndify, IBM - each has their own recognize_...(audio) function
            # NOTE:- each of them has different number of parameters like credentials to use their service
            self.text = recognizer.recognize_google(audio)      # uses Google
            print("Your Bot " + self.name + " --> ", self.text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio!")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Start execution
if __name__ == "__main__":
    # create a Dev bot
    dev_bot = ChatBot(name="Dev")
    
    # make the bot listen and convert to text
    while True:
        dev_bot.speech_to_text()

    # NEXT CREATE wake_up function

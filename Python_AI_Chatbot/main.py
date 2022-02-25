# Reference and thanks to: https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/

# PCKAGES:
    # - Numpy               - basic functionality on numbers
    # - SpeechRecognition   - for text to Speech
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
             print("listening...")
             audio = recognizer.listen(mic)
        try:
             self.text = recognizer.recognize_google(audio)
             print("me --> ", self.text)
        except:
             print("me -->  ERROR")

# Start execution
if __name__ == "__main__":
    dev_bot = ChatBot(name="Dev")
    

"""main module: add something later """

import os
import cv2
import speech_recognition as sr
import tkinter as tk
import customtkinter

# NOTE: The GUI is being developed by @AcademicalWeapon on his PC since cba to create a codespace

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
except Exception as e:
    print(e)
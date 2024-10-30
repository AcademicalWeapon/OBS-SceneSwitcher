# OBS Scene Switcher

## What is OBS Scene Switcher?

Automatic Python Script that changes the Scene when detecting Audio/Images that should preferably not be seen by the Public. It uses the Libraries Speech Recogntion for Audio, CV2 for Visual/Image Recogniton and Tkinter/Customtkinter for some UI.

## Why use OBS Scene Switcher?

During Streaming, many unpredictable things will occur. Be it for example accidently saying a Racial Slur at a certain Bridge or accidentatlly showing your Face when you are one of those "No Face" Streamers (Eugh...). Point is, this Program is useful for when you want to hide or Censor things that you don't want your Audience to seen. Just like Oscar Wilde said it: "Expect the Unexpected."

## Requirements

- OBS Websocket Plugin & .env File containing your API Key
- A Scene that's called STANDBY (You can changes the name in the connections.py Module)

## Importat Notes

### Use Python 3.12.7:

It is recommended to use Python 3.12.7 in order to not get any Errors.
Because the Library 'aifc' was removed in python 3.13.0, the Library Speech Recognition will not work and throw in a RuntimeError.
Specifically, this: "RuntimeError: 'aifc' was slated for removal after Python 3.13 alpha"
If this Issue is resolved in future Python versions (or the Library gets Updated), then just ignore this and continue using Python 3.whatever.

## Also, the Program has to be constantly running:

I am not gonna make it run in the Background. 1. Cba to program that and 2. Idk how to even do that.

### Links, Socials & More

- If you don't have the Websocket Plugin, install it from here: https://github.com/obsproject/obs-studio
- My Website: https://www.ivelinivanov.de
- My Discord: https://discord.gg/x2CXhwa5

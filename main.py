"""main module: add something later """

import os
import tkinter as tk
import customtkinter as ctk
import SceneSwitch as SS
import AudioImageDet as AID

# NOTE: The GUI is being developed by @AcademicalWeapon on his PC since cba to create a codespace

# Loads the Keywords File
KEYWORDS = AID.LoadKeywords("keywords.txt")

# Start the Audio Detection
AID.AudioDetection(KEYWORDS)

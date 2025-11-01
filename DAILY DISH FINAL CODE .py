# DailyDish is a meal plan suggestion tool using GUI with Tkinter.

#This code chooses a random recipe from a predefined dictionary,and prompts the user with a GUI window with options for recipes to make and the ingredients needed, with a checklist to tick off ingredients as they are gathered.

import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# this dictionary holds recipe names as keys and lists of ingredients as values

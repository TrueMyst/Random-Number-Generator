import random
import tkinter as tk
from tk import *
import requests
from PIL import Image, ImageTk

# Creating the Root
root = tk.Tk()
root.title("Random Number Generator v0.1.2")
root.geometry("430x300")
root.resizable(width = False, height  = False)

# Setting the Icon
ico = Image.open('random.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Creating a Random Number Generator Function
def generate_number():
	num = random.randrange(1, 100)
	base3.config(text = num)

# Creating the Base
base = tk.Label(root, text = "Click below to generate a Random Number", font = ("Bahnschrift", 16))
base.pack(pady = 20)

base2 = tk.Button(text="Generate!", font=("Verdana", 14), bg = "#e1e1e1", command=generate_number)
base2.pack(pady = 10)

base3 = tk.Label(text = "👋", font=("Cambria", 26))
base3.pack(pady = 15)

base4 = tk.Label(text = "Made by Myst <3", font = ("Cambria", 8))
base4.pack(pady = 30)

root.mainloop()
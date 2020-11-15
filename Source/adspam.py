import tkinter as tk
import os
import random
import PIL
import time
import sys
from PIL import ImageTk, Image


interval = input("Input image time interval > ")

try:  # converts user entry to a decimal value
    interval = float(interval)
    print("Running...")
except:  # if the user entry is not valid, the program exits
    print("Entry Error")
    time.sleep(2)
    sys.exit()


def showing():  # displays image
    path = os.path.join("imgdir", random.choice(os.listdir("imgdir")))
    # selects random image from "imgdir" to display

    image = PIL.Image.open(path)
    width, height = image.size

    window = tk.Tk()
    window.title("!!! IMPORTANT !!!")
    window.geometry(f"{width}x{height}")

    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    window.attributes("-topmost", True)
    window.after(60000, lambda: window.destroy())
    window.mainloop()
    # destroys window automatically if not closed


while True:
    time.sleep(interval)
    rand_select = int(random.random() * 10)
    # selects a random number over an interval

    if rand_select == 5:  # if the correct number is generated, an image will be displayed
        try:
            showing()
        except:
            pass

from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.geometry("1920x1080")

def on_f11(event) :
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

root.bind('<F11>', on_f11)



root.mainloop()
from tkinter import *

wide = int(input("Enter the width of your frame:"))
high = int(input("Enter the height of your frame:"))

print("1. Label Frame \n2.Frame")
iN = int(input("Enter >>>"))

if iN == 1:
    if wide >0 and high>0:
        root = Tk()
        root.geometry('1920x1000')

        label_f = LabelFrame(
        root,
        text = 'Your desired Label Frame',
        width = wide,
        height = high  
        )
        label_f.pack(padx=10, pady=50)
        
        root.mainloop()
else:
    if wide >0 and high>0:
        root = Tk()
        root.geometry('1920x1000')

        frame = Frame(
        root,
        
        width = wide,
        height = high  
        )
        frame.config(bg='BLACK')
        frame.pack(padx=10, pady=50)
        
        root.mainloop()
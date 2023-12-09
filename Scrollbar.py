from tkinter import *

root = Tk()
root.title('Scrollbar Practise')
root.geometry('500x600')

canvas = Canvas(root, bg='RED')
canvas.pack(fill=BOTH, expand=True)
canvas.config(height=6000)

scroll = Scrollbar(canvas)
scroll.pack(fill=Y)

scroll.config(command= canvas.yview)

root.mainloop()
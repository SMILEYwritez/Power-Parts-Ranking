from tkinter import *
from PIL import ImageTk, Image
import sys 

bckground = '#A9A9A9'
foeground = 'WHITE'
lbackground =  '#CA0123'

root = Tk()
root.title('Power Parts Ranking')
root.geometry('1080x600')
root.attributes('-fullscreen', True)
root.config(bg=bckground)

def on_f11(event): #To make it go fullscreen and out of fullscreen on pressing f11
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

root.bind('<F11>', on_f11)

power_button = ImageTk.PhotoImage(Image.open("png-clipart-computer-icons-logo-button-power-symbol-button-logo-desktop-wallpaper-thumbnail-removebg-preview (1).png"))

label_Frame = LabelFrame(
    root,
    width=1920,
    height=125
)
label_Frame.config(bg='#CA0123')
label_Frame.pack_propagate(False)
label_Frame.columnconfigure(0, weight = 0)


label = Label(label_Frame, text='Power Parts Ranking',font=('EB Corp Bold',56))
label.config(background='#CA0123', fg='WHITE')

power_button_label=Label(
    label_Frame,
    bg='#CA0123', 
    fg='WHITE',
    width=50,    
    height=50,
    image=power_button    
)

def on_image_click(event):
    sys.exit(0)

power_button_label.place(relx=0.95, rely=0.25)
power_button_label.bind('<Button-1>', on_image_click)

label.grid(column=0, row=0)
label.pack(side='left',pady=15,padx=100)
label_Frame.pack(padx=0, pady=10)

component_frame = Frame(
    root,
    width=500,
    height=1000,
    bg=bckground
)

component_frame.pack_propagate(False)

button_motherboard= Button(component_frame, text='Motherboard', font=('Arial', 26))
button_motherboard.pack(padx= 45, pady= 30)
button_motherboard.config(width=12, bg='WHITE')

button_cpu = Button(component_frame, text='Processor', font=('Arial', 26))
button_cpu.pack(padx = 60, pady = 10)
button_cpu.config(width=12, bg='WHITE')

button_ram = Button(component_frame, text='RAM', font=('Arial', 26))
button_ram.pack(padx = 75, pady = 30)
button_ram.config(width=12, bg='WHITE')

button_gpu = Button(component_frame, text='Graphic Card', font=('Arial', 26))
button_gpu.pack(padx = 75, pady = 10)
button_gpu.config(width=12, bg='WHITE')


button_ps = Button(component_frame, text='Power Supply', font=('Arial', 26))
button_ps.pack(padx = 75, pady = 30)
button_ps.config(width=12, bg='WHITE')

button_cpuc = Button(component_frame, text='AIR Cooler', font=('Arial', 26))
button_cpuc.pack(padx = 75, pady = 10)
button_cpuc.config(width=12, bg='WHITE')

component_frame.pack(pady=20)

options = ['Motherboard', 'Processor', 'Air Cooler', 'RAM', 'Graphic Card', 'Power Suplly']
variable = StringVar()
variable.set('Select Option')

caret_down_black=ImageTk.PhotoImage(Image.open("caret_down_edited-removebg-preview (2).png"))

select_option = OptionMenu(
    label_Frame, variable, *options
)

select_option.config(
    bg=lbackground,
    fg='WHITE',
    activebackground='#800020',
    border=0,
    highlightthickness=0,
    highlightbackground='#800020',
    indicatoron=0,
    font=('Arial',30)
)
select_option.pack(padx=0)

root.mainloop()
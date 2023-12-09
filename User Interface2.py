from tkinter import *  
from PIL import Image, ImageTk
import sys

bckground = '#A9A9A9'
foeground = 'WHITE'
lbackground =  '#CA0123'

root = Tk()
root.title('Power Parts Ranking')
root.geometry('1080x6000')
root.attributes('-fullscreen', True)

def on_f11(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

root.bind('<F11>', on_f11)

#Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

main_canvas = Canvas(
    root, bg=bckground, yscrollcommand= scrollbar.set
)
main_canvas.pack(expand=True,fill='y')
main_canvas.config(width=1920, highlightthickness=0, border=0, height=6000)
main_canvas.pack_propagate(False)
scrollbar.config(command=main_canvas.yview)

label_frame = LabelFrame(
    main_canvas, bg=lbackground, width=1920,height=85
)

label = Label(label_frame, text='Power Parts Ranking', font=('Khula Light', 35))
label.pack(padx=80, side='left')
label.config(
    bg=lbackground, 
    fg='WHITE',
    border=0,
    highlightthickness=0
)

power_button = ImageTk.PhotoImage(Image.open("White power button.png"))
power_button_hower = ImageTk.PhotoImage(Image.open("png-clipart-computer-icons-logo-button-power-symbol-button-logo-desktop-wallpaper-thumbnail-removebg-preview(2).png")) 
motherboard = ImageTk.PhotoImage(Image.open("motherboard.png"))

power_button_label = Label(
    label_frame, bg=lbackground, width=50, height=50, image=power_button
)

def on_enter(event):
    power_button_label.config(
        image=power_button_hower
    )

def on_leave(event):
    power_button_label.config(
        image=power_button
    )

def on_image_click(event):
    sys.exit(0)

power_button_label.place(relx=0.96, rely=0.15)

power_button_label.bind('<Enter>', on_enter)
power_button_label.bind('<Leave>', on_leave)
power_button_label.bind('<Button-1>', on_image_click)

options = ['Motherboard', 'Processor', 'Air Cooler', 'RAM', 'Graphic Card', 'Power Supply']
variable = StringVar()
variable.set("Select Component")

component_option = OptionMenu(
    label_frame, variable, *options
)

component_option.config(
    bg=lbackground,
    fg='WHITE',
    activebackground='#800020',
    activeforeground='WHITE',
    border=0,
    highlightthickness=0,
    indicatoron=0,
    font=('Khula Light',26)
)

component_option['menu'].config(
    bg='#C41E3A',
    fg='WHITE',
    activebackground='#D22B2B',
    font=('Khula Light',22),
    border=0,
    activeborder=0,
    bd=0,            # Set this to 0 to remove the border
    relief='flat'
)
component_option.place(relx=0.375, rely=0.2)

label_frame.pack_propagate(False)
label_frame.pack(pady=10)

#Motherboard
mb_canvas = Canvas(
    main_canvas , bg ='WHITE' 
)
mb_canvas.config(
    width = 1920, 
    highlightthickness=0,
    border=5,
    height=375
)
#Motherboard
mb_canvas.create_image(1280,23, anchor=N, image=motherboard)
mb_canvas.create_text(175,50, text='Motherboard', font=('Arial',36), fill=lbackground)
mb_canvas.create_text(580,190, text='''
    A motherboard is the main circuit board of a computer and is also known as the mainboard or system board. 
    It is a crucial component that houses and connects various essential hardware components of a computer 
    system. The motherboard provides a platform for the CPU (Central Processing Unit), 
    RAM (Random Access Memory), storage devices, expansion cards, and other essential components to 
    communicate with each other.
''', 
    font=('Khula Light',18), fill=lbackground)
mb_canvas.pack_propagate(False)
mb_canvas.pack(padx=50, pady=50)

#Processor
cpu_canvas = Canvas(
    main_canvas , bg ='WHITE' 
)
cpu_canvas.config(
    width = 1920, 
    highlightthickness=0,
    border=5,
    height=375
)

cpu_canvas.create_image(1280,23, anchor=N, image=motherboard)
cpu_canvas.create_text(175,50, text='Processor', font=('Arial',36), fill=lbackground)
cpu_canvas.create_text(580,190, text='''
    A motherboard is the main circuit board of a computer and is also known as the mainboard or system board. 
    It is a crucial component that houses and connects various essential hardware components of a computer 
    system. The motherboard provides a platform for the CPU (Central Processing Unit), 
    RAM (Random Access Memory), storage devices, expansion cards, and other essential components to 
    communicate with each other.
''', 
    font=('Khula Light',18), fill=lbackground)
cpu_canvas.pack_propagate(False)
cpu_canvas.pack(padx=50, pady=25)



root.mainloop()
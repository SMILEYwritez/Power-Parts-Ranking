from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x300")

main_frame = Frame(root, bg='WHITE')
main_frame.pack(fill=BOTH, expand = True)
main_frame.columnconfigure(0, weight = 1)
main_frame.rowconfigure(0, weight = 1)

options = ['First', 'Second', 'Third']
variable = StringVar()
variable.set('Select Option')

caret_down_black=ImageTk.PhotoImage(Image.open("caret_down_edited-removebg-preview (2).png"))

select_option = OptionMenu(
    main_frame, variable, *options
)

select_option.config(
    bg="#6330FF",
    fg='White',
    activebackground="#cbbaff",
    activeforeground="BLACK",
    font=('Arial',16),
    border = 0,
    highlightthickness=1,
    highlightbackground="#cbbaff",
    pady=20,
    indicatoron = 0,
    #image = caret_down_black,
    #compound=RIGHT
)
select_option.grid(column=0, row=0, sticky=N+EW, padx=70,pady=10)

select_option['menu'].config(
    bg='#6330FF',
    fg='White',
    activebackground='#cbbaff',
    activeforeground='BLACK',
    font=('Arial',16),
    border=0,
    activeborder=5
)

caret_down_label=Label(
    select_option,
    text='idk',
    bg='#6330ff',
    width=25,
    height=25,
    border=0,
    highlightthickness=0,
    image=caret_down_black
)
caret_down_label.place(relx=0.87, rely=0.35)

def on_enter(event):
    caret_down_label.config(
        bg='#cbbaff'
    )
def on_leave(event):
    caret_down_label.config(
        bg='#6330ff'
    )
select_option.bind('<Enter>', on_enter)
select_option.bind('<Leave>', on_leave)

def on_label_click(event):
    select_option['menu'].post(event.x_root, event.y_root)
    select_option.focus_set()

caret_down_label.bind('<Button-1>', on_label_click)

root.mainloop()
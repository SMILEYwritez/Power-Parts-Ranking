from tkinter import  *

root = Tk()
root.geometry("1920x1080")
root.title("Power Parts Ranking")
label = Label(text="Power Parts Ranking", fg='Green', font=('Hedvig Letter Serif',55))
label.config(bg= 'Light Blue')
label.pack(padx=10, pady=10)
root.configure(bg='#121212')



options = ["Option1", "Option2 Option3 Option4 ", "Option3"]
clicked = StringVar()
clicked.set( "Option1" )

drop_down_menu = Frame(root)
drop_down_menu.columnconfigure(0, weight=1)
drop_down_menu.columnconfigure(1, weight=1)
drop_down_menu.columnconfigure(2, weight=1)
drop_down_menu.columnconfigure(3, weight=1)
drop_down_menu.columnconfigure(4, weight=1)
drop_down_menu.columnconfigure(5, weight=1)
wid = len(max(options))

drop_down_menu.config(width=wid)

drop = OptionMenu(drop_down_menu, clicked, *options)
drop.grid(row= 0, column= 0)

drop_down_menu.pack(fill='x')

root.mainloop()
import customtkinter
from tkinter import*

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
# app.geometry('720x480')
app.title('Entry Panel')

frame = customtkinter.CTkFrame(app, bg_color='green', corner_radius=10)
frame.pack()

user_id = customtkinter.CTkEntry(frame, placeholder_text= 'Enter Username')
user_id.place(relx=.5, rely=.2, anchor= customtkinter.CENTER )

pass_id = customtkinter.CTkEntry(frame, placeholder_text= 'Enter Password', show = '*')
pass_id.place(relx=.5, rely= .4, anchor= customtkinter.CENTER)

username = 'turtle'
password = 'turtle'

def button_event():
    if (user_id.get()== username) and (pass_id.get() == password):
        text_var.set('Connencted')
    else:
        text_var.set("Wrong password  or userid")
buttton = customtkinter.CTkButton(frame, text ='BUTTON' , command= button_event)
buttton.place(relx=.5, rely=.6,anchor= customtkinter.CENTER )

text_var = StringVar()
label= customtkinter.CTkLabel(frame, corner_radius=8, textvariable= text_var, text_color= 'red'  )
label.place(relx=.5, rely=.75, anchor = customtkinter.CENTER)

app.mainloop()

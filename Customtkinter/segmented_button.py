import customtkinter, tkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
app = customtkinter.CTk()
app.title('combobox')

frame  = customtkinter.CTkFrame(app, corner_radius=50, width=400, height=300)
frame.pack(padx=20, pady=20)


name_entry = customtkinter.CTkEntry(frame, placeholder_text="Name", width =250)
name_entry.place(relx=.5, rely=.2, anchor= customtkinter.CENTER)


surname_entry = customtkinter.CTkEntry(frame, placeholder_text="Surame" , width =250)
surname_entry.place(relx=.5, rely=.3, anchor= customtkinter.CENTER)

age_entry = customtkinter.CTkEntry(frame, placeholder_text="Age" , width =250)
age_entry.place(relx=.5, rely=.4, anchor= customtkinter.CENTER)



def segmented_btn_event(value):
    name = str(name_entry.get())
    surname = str(surname_entry.get())
    age = str(age_entry.get())
    text_var.set('')
    if value == 'NAME' :
        text_var.set(f'Name : {name}')
    if value == 'SURNAME' :
       text_var.set(f'Surname : {surname}')
    if value == 'AGE' :
       text_var.set(f'Age : {age}')

segemented_btn = customtkinter.CTkSegmentedButton(frame,values =['NAME', 'SURNAME', 'AGE'], command= segmented_btn_event, )
segemented_btn.place(relx=.5, rely =.6, anchor= customtkinter.CENTER)



text_var = tkinter.StringVar(value='')
label = customtkinter.CTkLabel(frame, textvariable = text_var, fg_color='yellow', text_color='black' , width=150, corner_radius=10)

label.place(relx=.5, rely=.8, anchor = customtkinter.CENTER)

app.mainloop()

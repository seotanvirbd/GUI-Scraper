import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
app = customtkinter.CTk()
app.title('combobox')

frame  = customtkinter.CTkFrame(app, corner_radius=50, width=400, height=300)
frame.pack(padx=10, pady=30)


frame_width = frame.winfo_reqwidth()
frame_height = frame.winfo_reqheight()
print(f"Frame Width: {frame_width} pixels")
print(f"Frame Height: {frame_height} pixels")

name_entry = customtkinter.CTkEntry(frame, placeholder_text="Name", width =250)
name_entry.place(relx=.5, rely=.2, anchor= customtkinter.CENTER)
print(name_entry.winfo_reqwidth())

surname_entry = customtkinter.CTkEntry(frame, placeholder_text="Surame" , width =250)
surname_entry.place(relx=.5, rely=.3, anchor= customtkinter.CENTER)

option_var = customtkinter.StringVar(value='MALE')
gender_combobox= customtkinter.CTkComboBox(frame, values=['MALE', 'FEMALE'], variable= option_var , width =250)
gender_combobox.place(relx=.5, rely=.4, anchor= customtkinter.CENTER)

def btn_event():
    name = str(name_entry.get())
    surname = str(surname_entry.get())
    gender = str(gender_combobox.get())
    text_var.set(f'Name : {name} \n Surname : {surname} \n Gender : {gender}')
btn = customtkinter.CTkButton(frame,text= 'Button' , command= btn_event )
btn.place(relx=.5, rely =.5, anchor= customtkinter.CENTER)

# to see the width of a widget
btn_width= btn.winfo_reqwidth()
print(f"btn Width: {btn_width} pixels")

text_var = StringVar()
label = customtkinter.CTkLabel(frame, textvariable = text_var, fg_color='yellow', text_color='black' , width=150, corner_radius=10)

label.place(relx=.5, rely=.7, anchor = customtkinter.CENTER)
# to see the width of a widget
label_width = label.winfo_reqwidth()
print(f"Label Width: {label_width} pixels")

app.mainloop()

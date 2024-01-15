import customtkinter
import requests
from bs4 import BeautifulSoup
import os
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry('700x400')
app.title("Airbnb Image Downloader")


entry = customtkinter.CTkEntry(app, placeholder_text='Enter A Link', width=400)
entry.place(relx=.5, rely=.1, anchor=customtkinter.CENTER)

folder_entry = customtkinter.CTkEntry(
    app, placeholder_text='Enter Folder Name', width=400)
folder_entry.place(relx=.5, rely=.25, anchor=customtkinter.CENTER)


def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_divs = soup.find_all('div', {'data-testid': 'card-container'})
    print(len(all_divs))

    for i, div in enumerate(all_divs):
        image_link = div.find('img')['src']
        image_name = div.find(
            'div', {'data-testid': 'listing-card-title'}).text

        with open(image_name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(image_link)
            f.write(im.content)
        print('Writing: ', i+1, image_name)
        label.configure(text=f" Writing -{i+1} {image_name}")
        label.update()


def download_button():
    x = entry.get()
    y = folder_entry.get()
    imagedown(x, y)
    label.configure(text='Download Completed')


button = customtkinter.CTkButton(
    app, text='Start Download', command=download_button, anchor=customtkinter.CENTER)
button.place(relx=.35, rely=.4)

text_var = StringVar()
label = customtkinter.CTkLabel(app, text='Airbnb Image Downloader', )
label.place(relx=.45, rely=.6, anchor=customtkinter.CENTER)


app.mainloop()

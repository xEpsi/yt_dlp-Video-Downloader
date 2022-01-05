from __future__ import unicode_literals
import time
import subprocess
from tkinter import *
from tkinter import ttk
import os
from time import sleep

try:
    import yt_dlp
    
except Exception:

    from ctypes import windll   
    windll.user32.MessageBoxW(0, "The program is going to automatically install the required modules. Some CMD windows will show up, and then it will run normally. Press OK to continue.",
                              "Not So Fatal Error: Missing Python Modules", 0)


    os.system('cmd /c "pip install yt_dlp"')
    import yt_dlp

with open("config.txt", "r") as f:
    config = str(f.read())      # Get user options for later (Download path and quality)
exec(config)

if 'downloadPath' not in locals():
    downloadPath = os.path.expanduser('~\Downloads')
if downloadPath == 'DEFAULT':
    downloadPath = os.path.expanduser('~\Downloads')
if 'chosenQuality' not in locals():
    chosenQuality = "best"
  

# Config.txt variable names: downloadPath, chosenQuality

window = Tk()
window.geometry('1000x500')
window.config(bg='white')
window.title('Much Cool Youtube Downloader by dsc.bio/Epsi')
windowlogo = PhotoImage(file='logo.png')
window.iconphoto(False, windowlogo)

Label(window, text='Youtube Video Downloader!!!!', font=(
    'Comic Sans MS', 30), bg="red").pack(padx=5, pady=50)

video_link = StringVar()

Label(window, text='Enter video link: ', font=(
    'Comic Sans MS', 20, 'italic'), bd=4).place(relx=0.05, rely=0.2)
Entry_link = Entry(window, width=50, font=20,
                   textvariable=video_link, bd=4).place(relx=0.05, rely=0.28)


def videoDownload():
    ydl_opts = {
        'format': chosenQuality,    
        
        'noplaylist': True,
        'threads': 16,
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        'outtmpl': downloadPath + '/%(title)s.%(ext)s',
        'P': downloadPath
    }
    url = video_link.get()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    Label(window, text='Download Completed', font=('Comic Sans MS',
          25, 'bold'), bg='lightgreen').place(relx=0.3, rely=0.4)
    Label(window, text=f'Check {downloadPath} to see your downloaeded video!!!', font=(
        "Comic Sans MS", 15), fg="lightgreen").place(relx=0.3, rely=0.5)
  

Label(window, text=f'Settings:\n\nQuality:\n{chosenQuality}\n\nDownload path:\n{downloadPath}', font=('Comic Sans MS',
                                                             16), anchor='w').place(relx=0.4, rely= 0.4)

Label(window, text=f'Change the settings in config.txt!', font=('Comic Sans MS',
                                                             14)).place(relx=0.35, rely= 0.83)
  

Button(window, text="Download", font=("Comic Sans MS", 25, "bold"),
       bg="gray", command=videoDownload).place(relx=0.05, rely=0.6)

window.mainloop()

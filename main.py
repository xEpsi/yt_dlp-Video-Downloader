theme = "DarkAmber" #Open themes.py and choose the theme you like the most! Replace 
                    #DarkAmber with the theme of your choice (keep the quotation marks)

# --------------- IMPORTS ---------------#

try:
    import yt_dlp
    import PySimpleGUI as sg
    import os
    import ctypes
    import platform
    import resources.logo as logo
    import requests
except Exception:
    from ctypes import windll   
    windll.user32.MessageBoxW(0, "The program is going to automatically install the required modules. Some CMD windows will show up, and then it will run normally. Press OK to continue.", "Not so fatal error: Missing Python modules", 0)
    os.system('cmd /c "pip install yt_dlp"')
    os.system('cmd /c "pip install PySimpleGUI"')
    import yt_dlp
    import PySimpleGUI as sg
    import os
    import ctypes
    import platform
    import resources.logo as logo
    import requests


# --------------- MAIN PROGRAM --------------- #

sg.DEFAULT_FONT = 'Calibri' # You can change that if you want

sg.theme(str(theme)) 

if int(platform.release()) >= 8:    # Prevents blurry text & buttons by making the program DPI aware
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

layout = [
    [sg.Text("Video+ Downloader", font='Calibri 25', auto_size_text=True)],
    [sg.Text("Enter video link:", font="Calibri 12"), sg.InputText(key='-link-')],
    [sg.Button("Download"), sg.Button("Quit")],
    [sg.Text("\nOptions:", font='Calibri 18 bold', auto_size_text=True)],
    [sg.Text("Quality:", font="Calibri 12"), sg.Combo(["Best video with audio (recommended)","Worst video with audio", "Best video without audio", "Worst video without audio", "Best audio only", "Worst audio only"], default_value="Best video with audio (recommended)", readonly=True, key="-quality-")],
    [sg.Text("Download location:", font="Calibri 12"),sg.Text("", font="Calibri 12 bold"), sg.FolderBrowse("Choose Folder", key="-folder-")],
    [sg.Output(size=(60,5))]
]

tray = sg.SystemTray(menu=[[],"Hi"],data_base64=logo.logo)
window = sg.Window("Youtube+ Video Downloader by Epsi", layout, resizable=False, icon=logo.logo, titlebar_icon=logo.logo, finalize=True)

def videoDownload(quality, folder, link):
    ydl_opts = {
        'format': quality,
        'noplaylist': True,
        'no-mtime': True,
        'newline': True,
        'sponsorblock-mark': 'all',
        'no-colors': True,
        'outtmpl': folder + '/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

print("This is the console. Download progress will appear here.")

while True: # Main Loop

    event, values = window.read()
    
    if event == 'Download':
        
        if values["-folder-"] == '':
            tray.show_message("Error", "You must choose a download path", time=(50,3000))
        
        if values["-quality-"] == '':
            tray.show_message("Error", "You must choose a video quality", time=(50,3000))

        if values["-link-"] == '':
            tray.show_message("Error", "You must choose a download link", time=(50,3000))

        try:
            response = requests.get(values["-link-"])
            link=str(values["-link-"])
        except Exception:
            tray.show_message("Error", "Invalid URL", time=(50,3000))

        folder=str(values["-folder-"])

        if str(values["-quality-"]) == "Best video with audio (recommended)":
            quality = "best"
        elif str(values["-quality-"]) == "Worst video with audio":
            quality = "worst"
        elif str(values["-quality-"]) == "Best video without audio":
            quality = "bestvideo"
        elif str(values["-quality-"]) == "Worst video without audio":
            quality = "worstvideo"
        elif str(values["-quality-"]) == "Best audio only":
            quality = "bestaudio"
        elif str(values["-quality-"]) == "Worst audio only":
            quality = "worstaudio"
        else:
            tray.show_message("Error", "Invalid Quality", time=(50,3000))
        try:
            videoDownload(quality, folder, link)
            print("Download success")
            tray.show_message("Success", "Downloaded video", time=(50,3000))
        except Exception as e:
            print(e)
            pass

    if event in ('Quit',sg.WIN_CLOSED):
        break

window.close()






















































#huh
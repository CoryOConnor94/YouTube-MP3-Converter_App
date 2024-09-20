import yt_dlp
from tkinter import *
from tkinter import messagebox


def convert_to_audio():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audiofile.mp3'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_entry.get()])


# Create root window
root = Tk()
root.title("YouTube Converter")
root.geometry('800x600')

canvas = Canvas(root, width=500, height=400)
canvas.pack(side=TOP)
top_image = PhotoImage(file='Youtube-to-mp3.png')
canvas.create_image(300, 200, image=top_image)
title_label = Label(root, text="Convert YouTube video to MP3", font=('Helvetica', 14, 'bold'))
title_label.pack(side=TOP)
subtitle_label = Label(root, text="Enter YouTube URL below to retrieve audio", font=('Calibri', 14, 'italic'))
subtitle_label.pack(side=TOP)


url_entry = Entry(root, width=90)
url_entry.pack(side=TOP)

file_name_label = Label(root, text="Enter Name of File", font=('Calibri', 12, 'italic'), pady=5)
file_name_label.pack(side=TOP)

file_name_entry = Entry(root, width=50)
file_name_entry.pack(side=TOP)

button = Button(root, text="Convert", command=convert_to_audio, width=20)
button.pack(side=TOP)

root.mainloop()


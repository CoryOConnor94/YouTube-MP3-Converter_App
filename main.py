import yt_dlp
from datetime import datetime as dt
from tkinter import *
from tkinter import messagebox

# Get current time and date
now = dt.now()
formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")


def convert_to_audio(youtube_url, track_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{track_name}.mp3'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(youtube_url)
        messagebox.showinfo(title='Download Success!', message=f'File Saved as {track_name}.mp3')


def button_clicked():
    try:
        youtube_url = url_entry.get()
    except Exception as e:
        messagebox.showerror(title='URL Not Found!', message='URL not found. Please enter valid YouTube URL')
    else:
        track_name = file_name_entry.get()
        if track_name == '':
            track_name = f'{formatted_time}'

        url_entry.delete(0, END)
        file_name_entry.delete(0, END)
        convert_to_audio(youtube_url, track_name)


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

button = Button(root, text="Convert", command=button_clicked, width=20)
button.pack(side=TOP)

root.mainloop()


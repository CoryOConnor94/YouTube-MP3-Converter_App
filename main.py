from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox, END
from datetime import datetime as dt
import yt_dlp  # Import the YouTube downloader library

# Get current time and date
now = dt.now()
formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

def convert_to_audio(youtube_url, track_name):
    """
    Downloads and converts a YouTube video to an MP3 file.

    Parameters:
        youtube_url (str): The URL of the YouTube video.
        track_name (str): The desired name of the output MP3 file.
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best quality audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3 format
            'preferredquality': '192',  # Set quality to 192 kbps
        }],
        'outtmpl': f'{track_name}.mp3'  # Output file naming convention
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])  # Download the YouTube video
        messagebox.showinfo(title='Download Success!', message=f'File Saved as {track_name}.mp3')
    except Exception as e:
        messagebox.showerror(title='Download Failed!', message=f'Error: {str(e)}')


def button_clicked():
    """
    Handles the button click event to retrieve the YouTube URL and file name,
    then calls the conversion function.
    """
    try:
        youtube_url = url_entry.get()  # Get URL from input field
    except Exception:
        messagebox.showerror(title='URL Not Found!', message='Please enter a valid YouTube URL')
        return

    track_name = file_name_entry.get().strip()  # Get file name from input field

    # Use default name if no file name is provided
    if not track_name:
        track_name = f'{formatted_time}'

    url_entry.delete(0, END)  # Clear the URL entry field
    file_name_entry.delete(0, END)  # Clear the file name entry field

    convert_to_audio(youtube_url, track_name)  # Call the function to download and convert


# Create the main application window
root = Tk()
root.title("YouTube Converter")
root.geometry('800x600')

# Create a canvas for displaying an image
canvas = Canvas(root, width=500, height=400)
canvas.pack(side='top')
top_image = PhotoImage(file='Youtube-to-mp3.png')
canvas.create_image(300, 200, image=top_image)

# Create and pack title labels
title_label = Label(root, text="Convert YouTube video to MP3", font=('Helvetica', 14, 'bold'))
title_label.pack(side='top')
subtitle_label = Label(root, text="Enter YouTube URL below to retrieve audio", font=('Calibri', 14, 'italic'))
subtitle_label.pack(side='top')

# Entry field for YouTube URL
url_entry = Entry(root, width=90)
url_entry.pack(side='top')

# Label and entry field for file name
file_name_label = Label(root, text="Enter Name of File", font=('Calibri', 12, 'italic'), pady=5)
file_name_label.pack(side='top')
file_name_entry = Entry(root, width=50)
file_name_entry.pack(side='top')

# Button to start conversion
button = Button(root, text="Convert", command=button_clicked, width=20)
button.pack(side='top')

# Start the GUI event loop
root.mainloop()




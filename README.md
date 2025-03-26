# YouTube to MP3 Converter
![img.png](img.png)
## Overview
The **YouTube to MP3 Converter** is a Python application that allows users to download and convert YouTube videos into MP3 audio files using `yt_dlp`. The application provides a simple GUI built with Tkinter for user interaction.

## Features
- Download and convert YouTube videos to MP3 format.
- Automatically assigns a timestamp-based filename if no name is provided.
- Simple and user-friendly graphical interface.
- Displays success or error messages upon completion.

## Installation

### Prerequisites
Ensure you have Python installed. You will also need `yt-dlp` and `tkinter`.

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/youtube-to-mp3.git
   ```
2. Navigate to the project directory:
   ```sh
   cd youtube-to-mp3
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application
To start the converter, run:
```sh
python app.py
```

## Usage
1. Enter a valid YouTube URL in the input field.
2. Optionally, enter a custom file name. If left blank, the file will be named using the current timestamp.
3. Click the "Convert" button to start the conversion.
4. The MP3 file will be saved in the same directory as the script.

## Dependencies
- `yt-dlp`
- `tkinter`

Install them using:
```sh
pip install yt-dlp
```


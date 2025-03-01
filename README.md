
![image](https://github.com/user-attachments/assets/bef9402e-8ed7-45d9-ae0e-7d4c83665558)



# M3U Playlist Viewer with Stream Playback

This Python program allows you to view and play channels from an M3U playlist. It uses `tkinter` for the graphical user interface (GUI) and `ffmpeg` (specifically `ffplay`) to play video streams. The program loads an M3U playlist from a URL, displays the available channels in a table, and allows users to select and play a stream by double-clicking on a channel.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. **ffmpeg** installed on your system. 
   - The `ffplay` executable must be installed in the `C:\ffmpeg\` directory, and the relevant files should be extracted from the `bin` folder.
   
   If `ffmpeg` is not installed, download it from [FFmpeg's official website](https://ffmpeg.org/download.html) and place the extracted files in the `C:\ffmpeg\bin` directory.

## Installation

1. **Install Python dependencies:**
   The script requires the following Python libraries:
   - `tkinter`: This is used for the graphical user interface (GUI).
   - `urllib`: For downloading the playlist.
   - `subprocess`: To execute commands for playing streams.

   You can install the required dependencies using `pip` if you don't have them already:

   ```bash
   pip install tk
   ```

2. **Download the `ffmpeg` binaries:**
   - Download the latest version of FFmpeg from the official website: [FFmpeg Downloads](https://ffmpeg.org/download.html).
   - Extract the ZIP file to `C:\ffmpeg\`, and ensure that the `ffplay.exe` file is located in `C:\ffmpeg\bin\`.

## Usage

1. Run the script by executing the following command:

   ```bash
   python m3u_playlist_viewer.py
   ```

2. The GUI will open, displaying a table with the available channels from the M3U playlist. You can:
   - **Search** for specific channels using the search bar at the top.
   - **Select a channel** by double-clicking on a channel name in the table to begin playback.
   - **Loading bar** will indicate when the stream is being loaded, and the status label will show various statuses such as "Loading...", "Streaming in progress...", or "Playback finished."

3. To stop the stream, you can interrupt the process (e.g., using Ctrl+C in the terminal) while the playback is ongoing.

## Features

- **M3U Playlist Parsing:** The program downloads and parses the M3U playlist to extract channel names and media URLs.
- **Channel Filtering:** Users can filter channels by typing in the search bar.
- **Stream Playback:** The program uses `ffplay` from `ffmpeg` to stream the selected media.
- **Loading Indicator:** The GUI shows a loading bar while a channel is being prepared for streaming.
- **User-Friendly Interface:** The GUI is created with `tkinter` and includes features like a search bar, clickable table of channels, and a status label.

## Troubleshooting

- **ffplay not found:** If the script can't find `ffplay`, ensure that `ffmpeg` is installed in the `C:\ffmpeg\bin` directory and that the path to `ffplay.exe` is correct.
- **Connection errors:** If the playlist URL or the stream URL is unreachable, the program will show error messages (e.g., "Connection Error" or "Error 403: Access Forbidden").

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

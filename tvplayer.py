import subprocess
import urllib.request
import tkinter as tk
from tkinter import ttk
import threading

# Download the m3u8 playlist
def download_playlist(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8').splitlines()
    except Exception as e:
        print(f"Error downloading playlist: {e}")
        return []

# Parse the playlist and create records
def parse_playlist(playlist):
    channels = []
    for i in range(len(playlist)):
        if playlist[i].startswith('#EXTINF'):
            record = {}
            record['name'] = playlist[i].split(',')[-1].strip()
            record['media'] = playlist[i+1].strip()
            channels.append(record)
    return channels

# Function to play the stream
def playstream(m3u8_url, loading_bar, status_label):
    # Path to ffplay (adjust for your system)
    command = r'C:\ffmpeg\ffplay.exe'
    command_with_url = f'{command} {m3u8_url}'

    # Start the loading bar and update status
    loading_bar.start()
    status_label.config(text="Loading...")

    # Check the availability of the URL before playing (e.g., check HTTP status)
    try:
        with urllib.request.urlopen(m3u8_url) as response:
            if response.status == 403:
                status_label.config(text="Error 403: Access Forbidden")
                loading_bar.stop()
                return
            if response.status != 200:
                status_label.config(text=f"Error {response.status}: Access Problem")
                loading_bar.stop()
                return
    except Exception as e:
        status_label.config(text=f"Connection Error: {str(e)}")
        loading_bar.stop()
        return

    # Execute the command using subprocess to play the stream
    process = subprocess.Popen(command_with_url, shell=True)
    try:
        # Wait for the process to finish
        status_label.config(text="Streaming in progress...")
        process.wait()
        status_label.config(text="Playback finished.")
    except KeyboardInterrupt:
        # Handle interruption (Ctrl+C) and stop the process
        process.terminate()
        status_label.config(text="Playback interrupted.")
    finally:
        # Stop the loading bar after the process finishes
        loading_bar.stop()

# Function to start playback on click
def on_record_click(media_url, loading_bar, status_label):
    # Start the playback process in a separate thread
    threading.Thread(target=playstream, args=(media_url, loading_bar, status_label), daemon=True).start()

# Function to filter channels
def filter_channels(channels, search_query):
    return [channel for channel in channels if search_query.lower() in channel['name'].lower()]

# Create GUI with Tkinter
def create_gui(channels):
    root = tk.Tk()
    root.title("M3U Playlist")

    # Style the window
    root.configure(bg="#f0f0f0")

    # Add a loading bar widget
    loading_bar = ttk.Progressbar(root, mode="indeterminate")
    loading_bar.pack(pady=10)

    # Information label
    status_label = tk.Label(root, text="Select a channel", font=("Arial", 12), bg="#f0f0f0")
    status_label.pack(pady=10)

    # Search for channels
    search_var = tk.StringVar()
    def on_search_change(*args):
        search_query = search_var.get()
        filtered_channels = filter_channels(channels, search_query)
        update_table(filtered_channels)

    search_entry = ttk.Entry(root, textvariable=search_var, width=40)
    search_entry.pack(pady=10)
    search_var.trace("w", on_search_change)

    # Table with records
    tree = ttk.Treeview(root, columns=("Name", "Media"), show="headings", height=15)
    tree.heading("Name", text="Channel Name", anchor="w")
    tree.heading("Media", text="Media URL", anchor="w")

    # Style the table
    tree.column("Name", width=300, anchor="w")
    tree.column("Media", width=400, anchor="w")

    # Function to update the table
    def update_table(filtered_channels):
        for row in tree.get_children():
            tree.delete(row)
        for channel in filtered_channels:
            tree.insert("", "end", values=(channel['name'], channel['media']))

    # Initially fill the table with all channels
    update_table(channels)

    # Function that calls on_record_click when a record is selected
    def on_select(event):
        selected_item = tree.selection()[0]
        media_url = tree.item(selected_item, 'values')[1]
        on_record_click(media_url, loading_bar, status_label)

    # Bind the click function to the treeview
    tree.bind("<Double-1>", on_select)

    # Add vertical scrollbar
    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")

    # Display the window
    tree.pack(expand=True, fill="both")
    root.mainloop()

# Main program part
playlist_url = "https://iptv-org.github.io/iptv/index.m3u"
playlist = download_playlist(playlist_url)
channels = parse_playlist(playlist)

# Create GUI with the records
create_gui(channels)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        move_file()


def move_file():
    """Move all image file from folder_to_track to folder_destination"""
    for filename in os.listdir(folder_to_track):
        for ext in valid_extensions:
            if filename.endswith(ext):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)


folder_to_track = input("Enter path to the folder to track: ")
folder_destination = input("Enter path to the destination folder: ")
valid_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".gif", ".png", ".svg", ".svgz", ".avif", ".webp",
                    ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic",
                    ".ind", ".indd", ".indt"]
move_file()
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

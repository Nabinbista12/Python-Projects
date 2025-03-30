import os
import shutil
from pathlib import Path
import logging

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

def organize_file(directory):
    try:
        directory = Path(directory)
        print(directory)
        
        if not directory.exists():
            print(f"Error: The directory '{directory}' does not exist")
            return
    except Exception as err:
        print("Error Occured")

organize_file("E:\20th\py\Projects\projects for python\4_file_organizer.py")
f = "hi"
print(f"{f}")


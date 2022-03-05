from re import L
import tkinter as tk
from tkinter.filedialog import askdirectory
from main import *
from config import *

root = tk.Tk()

canvas = tk.Canvas(root, width = 800, height = 600)
canvas.grid(columnspan=3, rowspan=3)

camera_folders = []
screenshot_folders= []
highquality_folders = []

Backup_Cameras = Backup(camera_folders, 'Camera')
Backup_Screenshots = Backup(screenshot_folders, 'Screenshots')
Backup_HighQuality = Backup(highquality_folders, 'High Quality Camera')

def backup_func(type):
    if type == 'Backup Camera':
        Backup_Cameras.backup_all()
    elif type == 'Backup Screenshot':
        Backup_HighQuality.backup_all()
    elif type == 'Backup Highquality':
        Backup_HighQuality.backup_all()
    elif type == 'Backup to HDD':
        Backup.backup_to_hdd()
    elif type == 'Execute All':
        Backup_Cameras.backup_all()
        Backup_HighQuality.backup_all()
        Backup_HighQuality.backup_all()
        # Backup.backup_to_hdd()

class Label:
    def __init__(self, rely):
        self.rely = rely
        self.text = tk.StringVar()
        self.text.set("Click browse to add folders")
        self = tk.Label(root, bg='white', textvariable = self.text) 
        self.place(relx=0, rely=rely, relwidth=0.8, relheight=0.15)
    def change_text(self, textvariable):
        self.text.set(textvariable)

def browse_button_func(type):
    folder = askdirectory(title="Choose Folder")
    if folder:
        if type == 'camera':
            camera_folders.append(os.path.normpath(folder))
            camera_label.change_text("\n".join(camera_folders))
        elif type == 'screenshot':
            screenshot_folders.append(os.path.normpath(folder))
            screenshot_label.change_text("\n".join(screenshot_folders))
        elif type == 'highquality':
            highquality_folders.append(os.path.normpath(folder))
            highquality_label.change_text("\n".join(highquality_folders))

class Button_Browse:
    def __init__(self, rely, type):
        self.rely = rely
        self = tk.Button(root, text= 'Browse', command= lambda: browse_button_func(type), font="Raleway", bg="#20bebe", fg="white", height=2, width=15) 
        self.place(relx=0.8, rely=rely, relwidth=0.2, relheight=0.15)

class Button_Backup:
    def __init__(self, relx, type):
        self = tk.Button(root, text=type, command=backup_func(type), font="Raleway", bg="#20bebe", fg="Blue", height=2, width=15) 
        self.place(relx=relx, rely=0.9, relwidth=0.2, relheight=0.1)


camera_label = Label(0.05)
screenshot_label = Label(0.25)
highquality_label = Label(0.45)

camera_browse_button = Button_Browse(0.05, 'camera')
screenshot_browse_button = Button_Browse(0.25, 'screenshot')
highquality_browse_button = Button_Browse(0.45, 'highquality')


camera_backup_button = Button_Backup(0.025, 'Backup Camera')
screenshot_backup_button = Button_Backup(0.275, 'Backup Screenshot')
highquality_backup_button = Button_Backup(0.525, 'Backup Highquality')
# backup_hdd_button = Button_Backup(0.775, 'Backup to HDD')
execute_all_button = Button_Backup(0.775, 'Execute All')
root.mainloop()
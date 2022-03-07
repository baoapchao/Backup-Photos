from re import L
import tkinter as tk
from tkinter.filedialog import askdirectory
from main import *
from config import *



camera_folders = []
# screenshot_folders= []
# highquality_folders = [] 

backup_dict = {1 : {'name' : 'Camera', 'folders' : camera_folders} ,
        2 : {'name' : 'Screenshots'} ,
        3 : {'name' : 'High Quality Camera'} , 
        4 : {'name' :'backup-hdd'}
            }


window = tk.Tk()
window.title("Backup Photos in Fashion!")
window.geometry("800x600")

class Text:
    def __init__(self, rely):
        self.text_variable = tk.StringVar()
        self = tk.Label(textvariable = self.text_variable)
        self.place(relx=0, rely=rely, relwidth=0.8, relheight=0.15)
        # self.insert(tk.END, "Click browse to add folders")
    def change_text(self, text):
        self.text_variable.set(text)

camera_text = Text(0.05)
# screenshot_text = Text(0.25)
# highquality_text = Text(0.45)



def browse_button_func(backup_id):
    folder = askdirectory(title="Choose Folder")
    if folder:
        folder = os.path.normpath(folder)
        backup_dict[backup_id]['folders'].append(folder)
        camera_text.change_text("\n".join(backup_dict[backup_id]['folders']))

def backup_func(backup_id):
    Backup.backup_all(backup_dict[backup_id]['folders'] , backup_dict[backup_id]['name'])

class Button_Browse:
    def __init__(self, rely, backup_id):
        self.rely = rely
        self = tk.Button(window, text= 'Browse', command= lambda: browse_button_func(backup_id), height=2, width=15) 
        self.place(relx=0.8, rely=rely, relwidth=0.2, relheight=0.15)

class Button_Backup:
    def __init__(self, relx, backup_id):
        self = tk.Button(window, text='Backup ' + backup_dict[backup_id]['name'], command= lambda: backup_func(backup_id), height=1, width=15) 
        self.place(relx=relx, rely=0.9, relwidth=0.2, relheight=0.1)

camera_browse_button = Button_Browse(0.05, 1)

camera_backup_button = Button_Backup(0.025, 1)
# screenshot_backup_button = Button_Backup(0.275)
# highquality_backup_button = Button_Backup(0.525)



# backup_hdd_button = Button_Backup(0.775)
# execute_all_button = Button_Backup(0.775)
window.mainloop()
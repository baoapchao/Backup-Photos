import tkinter as tk
from tkinter.filedialog import askdirectory
from main import *
from config import *
from tkinter import ttk

destination_dir = ''
lst_source_dir = []

window = tk.Tk()
window.title("Backup Photos in Fashion!")
window.geometry("800x600")
try:
    window.iconbitmap(bitmap='apple.ico')
except:pass

label1 = tk.Label(text= 'Choose source folders (You can browse many times)')
label1.grid(row=1, column=1)

label2 = tk.Label(text= 'Choose destination folders')
label2.grid(row=3, column=1)

text_variable1 = tk.StringVar()
label_selected_source_dirs = tk.Label(textvariable = text_variable1, bg = 'white', width = 50)
label_selected_source_dirs.grid(row=2, column=2)

text_variable2 = tk.StringVar()
label_selected_dest_dirs = tk.Label(textvariable = text_variable2, bg = 'white', width = 50)
label_selected_dest_dirs.grid(row=4, column=2)

def source_browse_button_func():
    folder = askdirectory(title="Choose Folder")
    if folder:
        global lst_source_dir 
        folder = os.path.normpath(folder)
        lst_source_dir.append(folder)
        text_variable1.set("\n".join(lst_source_dir))

def dest_browse_button_func():
    folder = askdirectory(title="Choose Folder")
    if folder:
        global destination_dir
        folder = os.path.normpath(folder)
        destination_dir = folder
        text_variable2.set(destination_dir)

def reset_button_func():
    global lst_source_dir
    global destination_dir
    # global text_variable1
    # global text_variable2
    lst_source_dir = []
    destination_dir = ''
    text_variable1.set('')
    text_variable2.set('')

def info_box():
    tk.messagebox.showinfo(title='Folder Info', message = get_folder_info(destination_dir))

button_source_browse = tk.Button(window, text= 'Browse', command= lambda: source_browse_button_func()) 
button_source_browse.grid(row=2, column=1)

button_dest_browse = tk.Button(window, text= 'Browse', command= lambda: dest_browse_button_func()) 
button_dest_browse.grid(row=4, column=1)

button_get_info = tk.Button(window, text= 'Info', width = 10,  command= lambda: info_box()) 
button_get_info.grid(row=4, column=3)

button_backup = tk.Button(window, text='Backup', width = 10, command= lambda: backup_all(lst_source_dir, destination_dir)) 
button_backup.grid(row=5, column=3)

button_tidy = tk.Button(window, text='Organize', width = 10, command= lambda: tidy_folders(destination_dir)) 
button_tidy.grid(row=6, column=3)

button_reset = tk.Button(window, text='Reset', width = 10, command= lambda: reset_button_func()) 
button_reset.grid(row=7, column=3)

# combobox = ttk.Combobox(window, values=['values 1', 'value 2'])
# combobox.grid(row=7, column=3)

if __name__ == '__main__':
    window.mainloop()


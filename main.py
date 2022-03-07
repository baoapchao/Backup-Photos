import os
import shutil
from datetime import datetime,date
# import pandas as pd
from config import *

def get_unique_list(lst:list):
    unique_list = list(dict.fromkeys(lst))
    return unique_list

def get_modification_date(filepath):
    t = os.path.getmtime(filepath)
    exact_time = datetime.fromtimestamp(t)
    year = exact_time.strftime('%Y')
    month = exact_time.strftime('%m')
    day = exact_time.strftime('%d')
    return date(int(year), int(month), int(day))

def get_earliest_modification_date(lst_date:list):
    min_date = min(lst_date)
    min_date_standardized = min_date.strftime('%D')
    return min_date_standardized

def get_latest_modification_date(lst_date:list):
    max_date = max(lst_date)
    max_date_standardized = max_date.strftime('%D')
    return max_date_standardized

def copy_to_dest(destination_directory, file, source_file_directory):
    if os.path.exists(destination_directory):pass
    else:
        os.makedirs(destination_directory)
    destination = fr'{destination_directory}\{file}'
    shutil.copy2(source_file_directory, destination) 

def copytree_to_dest(hdd_directory, destination_folder_name, source_folder_directory):
    # if os.path.exists(destination_dir):pass
    # else:
    #     os.makedirs(destination_dir)
    destination = fr'{hdd_directory}\{destination_folder_name}'
    shutil.copytree(source_folder_directory, destination) 

def get_folder_info(directory):
    lst_extensions = []
    lst_dates = []
    for dirpath, dirs, files in os.walk(directory):
        if files != []:
            for file in files:
                filename, file_extension = os.path.splitext(fr'{dirpath}\{file}')
                lst_extensions.append(file_extension)
                lst_dates.append(get_modification_date(fr'{dirpath}\{file}'))
    print('FOLDER INFO')
    print('List of extensions:\t', get_unique_list(extension.lower() for extension in lst_extensions))
    print('Earliest modification date:\t', get_earliest_modification_date(lst_dates))
    print('Latest modification date:\t', get_latest_modification_date(lst_dates))

class Backup:
    # def __init__(self, source_directory_root, media_extensions, camera_folder_names, destination_directory_root, start_backup_date):
    start_backup_date_actual = date(start_backup_date[0], start_backup_date[1], start_backup_date[2])
    def __init__(self):
        pass
    def backup_all(lst_dir:list, destination_folder_name):  
        global camera_folders 
        global screenshot_folders
        global highquality_folders

        for dir in lst_dir:
            for dirpath, dirs, files in os.walk(dir):
                if files != []:
                    for file in files:
                        source_file_dir = fr'{dirpath}\{file}'
                        destination_dir = fr'{destination_root_directory}\{destination_folder_name}'
                        filename, file_extension = os.path.splitext(source_file_dir)
                        if file_extension.lower() in media_extensions and get_modification_date(source_file_dir) >= Backup.start_backup_date_actual:
                            copy_to_dest(destination_dir, file, source_file_dir)

    def backup_to_hdd():
        copytree_to_dest(hdd_directory, '_ALL BAO', source_folder_directory)

# Backup_Cameras = Backup('Camera')

# Backup_Screenshots = Backup('Screenshots')

# Backup_HighQuality = Backup('High Quality Camera')

# Backup.backup_all(['F:\_BACKUP ALL PHOTOS\Source\Camera'], 'Camera')
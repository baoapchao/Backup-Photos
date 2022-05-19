import os
import shutil
from datetime import datetime,date
# import pandas as pd
from config import *

def get_unique_list(lst):
    unique_list = list(dict.fromkeys(lst))
    unique_list.sort()
    return unique_list

def get_modification_date(filepath):
    t = os.path.getmtime(filepath)
    exact_time = datetime.fromtimestamp(t)
    year = exact_time.strftime('%Y')
    month = exact_time.strftime('%m')
    day = exact_time.strftime('%d')
    return date(int(year), int(month), int(day))

def get_earliest_modification_date(lst_date):
    min_date = min(lst_date)
    return min_date.strftime('%D')

def get_latest_modification_date(lst_date):
    max_date = max(lst_date)
    return max_date.strftime('%D')

def copy_to_dest(destination_directory, file, source_file_directory):
    year = datetime.strftime(get_modification_date(source_file_directory), '%Y')
    month = datetime.strftime(get_modification_date(source_file_directory), '%m')
    destination_divided_directory = os.path.join(destination_directory,year+'-'+month.zfill(2))
    if os.path.exists(destination_divided_directory):pass
    else:
        os.makedirs(destination_divided_directory)
    destination = os.path.join(destination_divided_directory,file)
    shutil.copy2(source_file_directory, destination) 

def move_to_dest(destination_directory, file, source_file_directory):
    year = datetime.strftime(get_modification_date(source_file_directory), '%Y')
    month = datetime.strftime(get_modification_date(source_file_directory), '%m')
    destination_divided_directory = os.path.join(destination_directory,year+'-'+month.zfill(2))
    if os.path.exists(destination_divided_directory):pass
    else:
        os.makedirs(destination_divided_directory)
    destination = os.path.join(destination_divided_directory,file)
    shutil.move(source_file_directory, destination) 

def remove_empty_folders(directory):
    walk = list(os.walk(directory))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

def tidy_folders(directory):
    for dirpath, dirs, files in os.walk(directory):
        if files != []:
            for file in files:
                source_file_dir = os.path.join(dirpath,file)
                filename, file_extension = os.path.splitext(source_file_dir)
                if file_extension.lower() in media_extensions and get_modification_date(source_file_dir) >= start_backup_date_actual:
                    move_to_dest(directory, file, source_file_dir)
    remove_empty_folders(directory)

def copytree_to_dest(hdd_directory, destination_folder_name, source_folder_directory):
    # if os.path.exists(destination_dir):pass
    # else:
    #     os.makedirs(destination_dir)
    destination = os.path.join(hdd_directory,destination_folder_name)
    shutil.copytree(source_folder_directory, destination) 

def get_folder_info(directory):
    lst_extensions = []
    lst_dates = []
    for dirpath, dirs, files in os.walk(directory):
        if files != []:
            for file in files:
                filepath = os.path.join(dirpath,file)
                filename, file_extension = os.path.splitext(filepath)
                lst_extensions.append(file_extension)
                lst_dates.append(get_modification_date(filepath))
    return f"""
    List of extensions:\n
    {','.join(get_unique_list(extension.lower() for extension in lst_extensions))}\n
    Earliest modification date: {get_earliest_modification_date(lst_dates)}\n
    Latest modification date: {get_latest_modification_date(lst_dates)}
    """

start_backup_date_actual = date(start_backup_date[0], start_backup_date[1], start_backup_date[2])

def backup_all(lst_source_dir, destination_dir):  
    for dir in lst_source_dir:
        for dirpath, dirs, files in os.walk(dir):
            if files != []:
                for file in files:
                    source_file_dir = os.path.join(dirpath,file)
                    # destination_dir = fr'{destination_root_directory}\{destination_folder_name}'
                    filename, file_extension = os.path.splitext(source_file_dir)
                    if file_extension.lower() in media_extensions and get_modification_date(source_file_dir) >= start_backup_date_actual:
                        copy_to_dest(destination_dir, file, source_file_dir)

# def backup_to_hdd():
#     copytree_to_dest(hdd_directory, '_ALL BAO', source_folder_directory)

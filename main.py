import os
import shutil
from datetime import datetime,date
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

def get_min_date(lst_date):
    min_date = min(lst_date)
    return min_date

def get_max_date(lst_date):
    max_date = max(lst_date)
    return max_date

def get_folder_info(folderpath):
    lst_extensions = []
    lst_dates = []
    for dirpath, dirs, files in os.walk(folderpath):
        if files != []:
            for filename in files:
                source_filepath = os.path.join(dirpath, filename)
                source_filename_wo_ext, source_file_ext = os.path.splitext(filename)
                lst_dates.append(get_modification_date(source_filepath))
                lst_extensions.append(source_file_ext)
    lst_extension = get_unique_list(extension.lower() for extension in lst_extensions)
    latest_modification_date = get_max_date(lst_dates)
    earliest_modification_date = get_min_date(lst_dates)
    return lst_extension, latest_modification_date, earliest_modification_date

def copy_to_dest(source_filepath, destination_folderpath):
    if os.path.exists(destination_folderpath):pass
    else:
        os.makedirs(destination_folderpath)
    source_filename = os.path.basename(source_filepath)
    destination_filepath = os.path.join(destination_folderpath, source_filename)
    shutil.copy2(source_filepath, destination_filepath)

def move_to_dest(source_filepath, destination_folderpath):
    if os.path.exists(destination_folderpath):pass
    else:
        os.makedirs(destination_folderpath)
    source_filename = os.path.basename(source_filepath)
    destination_filepath = os.path.join(destination_folderpath, source_filename)
    shutil.move(source_filepath, destination_filepath)

def copy_to_formatted_folderpath(source_filepath, destination_parent_folderpath):
    destination_foldername = datetime.strftime(get_modification_date(source_filepath), backup_foldername_format)
    destination_folderpath = os.path.join(destination_parent_folderpath, destination_foldername)
    copy_to_dest(source_filepath, destination_folderpath)

def move_to_formatted_folderpath(source_filepath, destination_parent_folderpath):
    destination_foldername = datetime.strftime(get_modification_date(source_filepath), backup_foldername_format)
    destination_folderpath = os.path.join(destination_parent_folderpath, destination_foldername)
    move_to_dest(source_filepath, destination_folderpath)

def remove_empty_folders(directory):
    walk = list(os.walk(directory))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

def get_incremental_directories(directory, start_dt):
    incremental_directories = []
    for dirpath, dirs, files in os.walk(directory):
        if dirs != []:
            for dir in dirs:
                if (datetime.strptime(dir, '%Y-%m')).date() >= start_dt:
                    folder_path = os.path.join(dirpath,dir)
                    incremental_directories.append(folder_path)
    return incremental_directories

def print_folder_info(folderpath):
    lst_extension, latest_modification_date, earliest_modification_date = get_folder_info(folderpath)
    return f"""
    List of extensions:\n
    {','.join(lst_extension)}\n
    Earliest modification date: {earliest_modification_date}\n
    Latest modification date: {latest_modification_date}
    """

def incremental_backup_photo_to_dest(source_folderpath, destination_parent_folderpath, incremental_boolean):
    lst_extension, latest_modification_date, earliest_modification_date = get_folder_info(destination_parent_folderpath)
    for dirpath, dirs, files in os.walk(source_folderpath):
        if files != []:
            for filename in files:
                source_filepath = os.path.join(dirpath, filename)
                source_filename_wo_ext, source_file_ext = os.path.splitext(filename)
                print(source_filepath)
                print(get_modification_date(source_filepath))
                if source_file_ext.lower() not in media_extensions or (get_modification_date(source_filepath) < latest_modification_date and incremental_boolean == 1):
                    pass
                else:
                    copy_to_formatted_folderpath(source_filepath, destination_parent_folderpath)


def tidy_folders(folderpath):
    for dirpath, dirs, files in os.walk(folderpath):
        destination_parent_folderpath = folderpath
        if files != []:
            for filename in files:
                source_filepath = os.path.join(dirpath, filename)
                source_filename_wo_ext, source_file_ext = os.path.splitext(filename)
                if source_file_ext.lower() in media_extensions:
                    move_to_formatted_folderpath(source_filepath, destination_parent_folderpath)
    remove_empty_folders(folderpath)
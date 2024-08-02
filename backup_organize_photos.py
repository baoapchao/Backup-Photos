from main import *
from config import default_backup_foldername_format

print('What is the source folder path?')
source_folderpath = input()

print('What is the destination path?')
destination_folderpath = input()

print(f'(Y/N) Do you want custom date format (default date format is {default_backup_foldername_format}?')
is_custom_date_format = input()

if is_custom_date_format == 'Y':
    print(fr'What is the date format (E.g: %Y-%m-%d)?')
    date_format = input()
elif is_custom_date_format == 'N':
    date_format = default_backup_foldername_format
else:
    raise Exception("Sorry, Y or N only")

print('Want incremental loading? 1 for yes and 0 for no')
incremental_boolean = int(input())

incremental_backup_photo_to_dest(source_folderpath, destination_folderpath, incremental_boolean, date_format)
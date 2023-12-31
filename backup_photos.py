from main import *

print('What is the source folder path?')
source_folderpath = input()

print('What is the destination path?')
destination_folderpath = input()

print('Want incremental loading? 1 for yes and 0 for no')
incremental_boolean = int(input())

incremental_backup_photo_to_dest(source_folderpath, destination_folderpath, incremental_boolean)
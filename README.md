### Description
This tool allows you to organize your media files in a date-formatted folder name.\
For example: If the folder name format is set to be '%Y-%m', the media files that were modified on 25-Jul-2024 will be moved to the folder '2024-07'.

### Usage
1. In cmd, run command: python -m backup_photos
2. Input source folder path
3. Input destination path
4. Input 1 if you want incremental loading to shorten the execution time or 0 if you want a full load
5. The media files will be moved and organized in the destination path

### Remark
1. Check the config.py file for configuration of the media file extensions and the date format of the organize folder.
2. There are other scripts for checking folder info, tidy folder without moving to a new parent path, etc.
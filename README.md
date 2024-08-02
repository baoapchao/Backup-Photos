### Description
This tool allows you to organize your media files in a date-formatted folder name.\
For example: If the folder name format is set to be '%Y-%m', the media files that were modified on 25-Jul-2024 will be moved to the folder '2024-07'.

### Prerequisites
1. Python installed
2. Check the config.py file for configuration of the media file extensions and the date format of the organize folder.

### Features
1. print_folder_info.py
2. tidy_folder.py
3. backup_organize_photos.py
4. explode_folder.py (opposite of tidy_folder_dateformatted_folders)

### Example folder structure 
The subfolders contain media files, such as images and videos, organized by month and year (`%Y-%m' date format):

/Media  
    /2022-01  
        image1.jpg  
        image2.png  
        video1.mp4  
    /2022-02  
        image1.jpg  
        image2.png  
        video1.mp4  
    /2022-03  
        image1.jpg  
        image2.png  
        video1.mp4  
    ...  
    /2022-12  
        image1.jpg  
        image2.png  
        video1.mp4  
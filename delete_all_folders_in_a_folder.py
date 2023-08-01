import os
import shutil
import math

def delete_all_loaded_folders(folder_path):
    try:
        # List all directories in the folder
        directories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

        # Loop through the directories and delete them one by one
        for folder_name in directories:
            folder_path_to_delete = os.path.join(folder_path, folder_name)
            shutil.rmtree(folder_path_to_delete)
            print(f"Deleted folder and its contents: {folder_path_to_delete}")

        print("All loaded folders in the folder have been deleted.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Replace 'folder_path' with the path to the folder containing the subfolders you want to delete.
folder_path = "C:\\smartwatch\\dividedfiles"
delete_all_loaded_folders(folder_path)
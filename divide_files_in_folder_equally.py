import os
import shutil
import math

def divide_files_into_groups(source_folder, destination_folder, num_groups):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)
    num_files = len(files)

    if num_files == 0:
        print("Source folder is empty. No files to divide.")
        return

    files_per_group = math.ceil(num_files / num_groups)

    for group_index in range(num_groups):
        start_idx = group_index * files_per_group
        end_idx = min((group_index + 1) * files_per_group, num_files)
        group_files = files[start_idx:end_idx]

        group_folder = os.path.join(destination_folder, f"group_{group_index + 1}")
        os.makedirs(group_folder, exist_ok=True)

        for file_name in group_files:
            source_file_path = os.path.join(source_folder, file_name)
            destination_file_path = os.path.join(group_folder, file_name)
            shutil.copy(source_file_path, destination_file_path)
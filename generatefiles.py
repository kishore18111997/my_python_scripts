import os

def generate_empty_files(folder_path, num_files):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i in range(1, num_files + 1):
        file_name = f"empty_file_{i}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as f:
            pass

if __name__ == "__main__":
    folder_path = "C:\\smartwatch\\randomfiles"  # Replace this with the actual path of your folder
    num_files = 5068

    generate_empty_files(folder_path, num_files)

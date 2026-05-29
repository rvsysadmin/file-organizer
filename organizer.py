import os
import shutil

# Folder path jahan files organize karni hain
FOLDER_PATH = "./test_folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".doc", ".docx", ".txt"]
}

def create_folders():
    for folder in FILE_TYPES.keys():
        if not os.path.exists(os.path.join(FOLDER_PATH, folder)):
            os.makedirs(os.path.join(FOLDER_PATH, folder))

def organize_files():
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(FOLDER_PATH, folder_name, file))
                    print(f"Moved: {file} → {folder_name}")
                    moved = True
                    break

            if not moved:
                print(f"Skipped: {file}")

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Organization Complete 🚀")

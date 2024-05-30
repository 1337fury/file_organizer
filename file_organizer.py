import os
import shutil

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')

def organize_files():
    if not os.path.exists(DOWNLOADS_FOLDER):
        print(f"Directory {DOWNLOADS_FOLDER} does not exist.")
        return

    FILE_TYPES = {
        'PDFs': ['.pdf'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.txt', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac']
    }

    for folder, extensions in FILE_TYPES.items():
        folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file_name in os.listdir(DOWNLOADS_FOLDER):
            file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
            if os.path.isfile(file_path):
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, folder_path)
                    print(f"Moved: {file_name} to {folder}")

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")

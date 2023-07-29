import os


extensions = {
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "svg": "Images",
    "exe": "Executables",
    "msi": "Executables",
    "mp3": "Audio",
    "wav": "Audio",
    "zip": "Compressed",
    "rar": "Compressed",
    "7z": "Compressed",
    "mp4": "Video",
    "txt": "Documents",
    "pdf": "Documents",
    "docx": "Documents",
    "doc": "Documents",
    "torrent": "Torrents",
    "xlsx": "Documents",
    "csv": "Documents",
    "pptx": "Documents",
}

def main():
    download_foulder_path = os.path.expanduser("~\Downloads")
    for item in os.listdir(download_foulder_path):

        item_path = os.path.join(download_foulder_path, item)

        if not os.path.isfile(item_path):
            continue

        file_extension = item.split(".")[-1]

        foulder_name = extensions[file_extension] if file_extension in extensions else "Other"
        destination = os.path.join(download_foulder_path, foulder_name)


        if not os.path.exists(destination):
            create_new_foulder_in_downloads(foulder_name)
            print(f"Created {foulder_name} foulder")

        os.rename(item_path, os.path.join(destination, item))
        print(f"Moved {item} to {foulder_name} foulder")



def create_new_foulder_in_downloads(foulder_name):

    # Replace 'path_to_downloads_folder' with the actual path to the "Downloads" folder
    downloads_folder_path = os.path.expanduser("~\Downloads")


    # Name of the new folder you want to create
    new_folder_name = foulder_name

    # Full path of the new folder
    new_folder_path = os.path.join(downloads_folder_path, new_folder_name)

    # Create the new folder inside the "Downloads" folder
    os.mkdir(new_folder_path)


if __name__ == "__main__":
    main()

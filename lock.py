import zipfile
import os
import shutil

def zip_folders(folder_paths):
    for folder_path in folder_paths:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            continue
        
        # Ensure that the given path is a folder
        if not os.path.isdir(folder_path):
            print(f"'{folder_path}' is not a folder.")
            continue
        
        zip_name = os.path.basename(folder_path) + '.zip'  # Use the folder name as the zip file name
        
        try:
            # Create a ZipFile object in write mode
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Iterate through all the files in the folder
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        # Get the full path of the file
                        file_path = os.path.join(root, file)
                        # Add the file to the zip archive
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
            
            # Move the zip file to the same directory as the original folder
            shutil.move(zip_name, os.path.join(os.path.dirname(folder_path), zip_name))
            
            # Delete the original folder
            shutil.rmtree(folder_path)
            
            print(f"Folder '{folder_path}' has been zipped successfully as '{zip_name}' and replaced with the zip file.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
folder_paths = ['WhatsApp']  # Change this to the list of folder paths you want to zip

zip_folders(folder_paths)

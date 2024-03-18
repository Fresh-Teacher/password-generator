import zipfile
import os

def unzip_folder(zip_file):
    # Check if the zip file exists
    if not os.path.exists(zip_file):
        print(f"The zip file '{zip_file}' does not exist.")
        return
    
    # Ensure that the given path is a zip file
    if not zipfile.is_zipfile(zip_file):
        print(f"'{zip_file}' is not a valid zip file.")
        return
    
    try:
        # Determine the extraction directory and filename
        extract_to = os.path.splitext(zip_file)[0] + '_unlocked'
        
        # Create the extraction directory if it doesn't exist
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
        
        # Open the zip file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Extract all contents to the specified directory
            zip_ref.extractall(extract_to)
        
        print(f"Zip file '{zip_file}' has been successfully extracted to '{extract_to}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
zip_file = 'All Documents - Copy.zip'  # Change this to the path of the zip file

unzip_folder(zip_file)

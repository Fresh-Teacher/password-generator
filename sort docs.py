import os
import shutil

def categorize_files(folder_path):
    # Create folders if they don't exist
    folders = ['Lesson notes', 'Schemes of Work', 'Past Papers']
    for folder in folders:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
    
    # Loop through files in the folder
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Convert file name to lowercase
            file_name_lower = file_name.lower()
            # Check keywords and move files to respective folders
            if 'notes' in file_name_lower:
                move_and_categorize(folder_path, file_name, 'lesson notes', file_name_lower)
            elif 'schemes' in file_name_lower:
                move_and_categorize(folder_path, file_name, 'schemes of work', file_name_lower)
            else:
                move_and_categorize(folder_path, file_name, 'past papers', file_name_lower)

def move_and_categorize(folder_path, file_name, category_folder, file_name_lower):
    # Move the file to the respective category folder
    shutil.move(os.path.join(folder_path, file_name), os.path.join(folder_path, category_folder, file_name))
    # Go to the category folder
    category_folder_path = os.path.join(folder_path, category_folder)
    # Create class folders
    classes = ['baby', 'middle', 'top', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
    for class_folder in classes:
        os.makedirs(os.path.join(category_folder_path, class_folder), exist_ok=True)
    # Categorize the file into the appropriate class folder
    for class_folder in classes:
        if class_folder in file_name_lower:
            # Remove dot if present in class folder name
            class_folder = class_folder.replace('.', '')
            shutil.move(os.path.join(category_folder_path, file_name), os.path.join(category_folder_path, class_folder, file_name))
            break

# Specify the folder path
folder_path = 'WhatsApp'

# Call the function to categorize files
categorize_files(folder_path)

print("Files categorized successfully!")

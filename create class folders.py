import os
import shutil

class FolderOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.keywords = {
            'baby': ['baby', 'baby class'],
            'middle': ['middle', 'middle class'],
            'top': ['top', 'top class'],
            'p.1': ['p.1', 'primary one'],
            'p.2': ['p.2', 'primary two', 'p. 2'],
            'p.3': ['p.3', 'primary three', 'p. 3'],
            'p.4': ['p.4', 'primary four'],
            'p.5': ['p.5', 'primary five', 'p 5'],
            'p.6': ['p.6', 'primary six'],
            'p.7': ['p.7', 'primary seven']
        }

    def organize_files(self):
        files = os.listdir(self.folder_path)
        for file_name in files:
            matched = False
            for folder_name, keywords in self.keywords.items():
                if any(keyword.lower() in file_name.lower() for keyword in keywords):
                    matched = True
                    break
            if not matched:
                continue

            source_path = os.path.join(self.folder_path, file_name)
            destination_folder = self.find_destination_folder(file_name)
            destination_path = os.path.join(self.folder_path, destination_folder)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination_folder} folder.")

    def find_destination_folder(self, file_name):
        for folder_name, keywords in self.keywords.items():
            if any(keyword.lower() in file_name.lower() for keyword in keywords):
                return folder_name
        return 'unclassified'  # If no match found, move to a generic folder

# Example usage:
if __name__ == "__main__":
    folder_path = "WhatsApp/Schemes of Work"
    organizer = FolderOrganizer(folder_path)
    organizer.organize_files()

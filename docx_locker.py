import os
import win32com.client as win32

def lock_word_docx_with_password(docx_path, password):
    try:
        word = win32.Dispatch("Word.Application")
        doc = word.Documents.Open(docx_path)

        # Set the password to the document
        doc.Password = password

        # Save and close the document
        doc.Save()
        doc.Close()

        # Quit Word application
        word.Quit()
        print(f"Document locked with password: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")

def lock_docx_files_in_folder(folder_path, password):
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            docx_file_path = os.path.abspath(os.path.join(folder_path, filename))
            lock_word_docx_with_password(docx_file_path, password)

if __name__ == "__main__":
    folder_path = "WhatsApp/weekend homework"
    password = "336f671488"

    lock_docx_files_in_folder(folder_path, password)

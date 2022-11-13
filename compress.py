# importing module
import os
from zipencrypt import ZipFile


def get_all_file_paths(directory):
      
    # Liste des fichiers
    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # Retourner la liste des fichiers
    return file_paths 

def zip_directory(destination, password):
    pwd = bytes(password, "utf-8")
    file_paths = get_all_file_paths(destination)
    print(file_paths)
    with ZipFile(f"{destination}.zip", "w") as zip:
        for file in file_paths:
            zip.writestr(file, "plaintext", pwd=pwd )

def main():
    zip_directory("files", "hello")

if __name__ == "__main__":
    main()
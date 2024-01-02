import os
import shutil

def delete_folders_recursively(directory_path, folder_names):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in dirs:
            folder_path = os.path.join(root, name)
            if name in folder_names:
                # Remove the desired folder
                shutil.rmtree(folder_path)
                print(f"Pasta removida: {folder_path}")
            else:
                # If it is not the desired folder, continue the recursive search
                delete_folders_recursively(folder_path, folder_names)

        for file in files:
            file_path = os.path.join(root, file)
            if file in ['package-lock.json', 'yarn.lock', 'composer.lock']:
                # Remove the desired file
                os.remove(file_path)
                print(f"Arquivo removido: {file_path}")

target_directory = './'
folders_to_delete = ['node_modules', 'vendor']

delete_folders_recursively(target_directory, folders_to_delete)

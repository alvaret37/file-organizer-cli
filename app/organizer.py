import os
import shutil

def organize_files(path):
    if not os.path.exists(path):
        print(f"Caminho não encontrado: {path}")
        return

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and not file.startswith('.'):
            ext = file.split('.')[-1]
            folder = os.path.join(path, ext.upper())
            os.makedirs(folder, exist_ok=True)
            shutil.move(full_path, os.path.join(folder, file))

import os
import shutil
from pathlib import Path
def image_list(folder_path):
    all_files= os.listdir(folder_path)
    final_images = []
    for filename in all_files:
        filepath = os.path.join(folder_path, filename)
        if filepath.endswith('jpeg') or filepath.endswith('jpg') or filepath.endswith('png') or filepath.endswith('webp'):
            if os.path.isfile(filepath):
                final_images.append(filepath)
    return final_images

def check_folder(main_folder_path):
    processed = os.path.join(main_folder_path,"processed")
    unprocessed = os.path.join(main_folder_path,"unprocessed")
    if (not os.path.isdir(processed)):
        os.mkdir(processed)
        os.mkdir(os.path.join(processed,"happy"))
        os.mkdir(os.path.join(processed,"sad"))
    if (not os.path.isdir(unprocessed)):
        os.mkdir(unprocessed)
        image_transporter(main_folder_path,unprocessed)
    

            
            
def image_transporter(source,destination):
    source_image = image_list(source)
    for image in source_image:
        shutil.move(image,destination)
        
    
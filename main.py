import os
from modules import core
img_path = input("Enter your folder path for analyzing")
all_files= os.listdir(img_path)
final_images = []
for filename in all_files:
    filepath = os.path.join(img_path, filename)
    if filepath.endswith('jpeg') or filepath.endswith('jpg'):
        if os.path.isfile(filepath):
            final_images.append(filepath)
result = core.analyze(final_images)
happy_count = 0
sad_count = 0
for i in result:
    if(result[i]['dominant_emotion']=='happy'):
        happy_count += 1
    else :
        sad_count+=1
print(happy_count, sad_count)
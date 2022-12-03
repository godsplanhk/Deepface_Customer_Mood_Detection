import os
import shutil
from pathlib import Path
from modules import image_extractor,core
input_img = input("Enter your folder path for analyzing")
image_extractor.check_folder(input_img)
unprocessed = os.path.join(input_img, "unprocessed")
processed = os.path.join(input_img,'processed')
deepFace = image_extractor.image_list(unprocessed)
result = core.analyze(deepFace)
happy_count = 0
sad_count = 0
count = 0
for i in result:
    if(result[i]['dominant_emotion']=='happy'):
        happy_count += 1
        shutil.move(deepFace[count],os.path.join(processed,"happy"))
    else :
        sad_count+=1
        shutil.move(deepFace[count],os.path.join(processed,"sad"))
    count+=1
print("No. of Happy peoples are ",happy_count,"and sad are", sad_count)
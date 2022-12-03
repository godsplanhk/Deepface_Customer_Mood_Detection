from deepface import DeepFace
from modules import image_extractor
import cv2
import os
def analyze(img_path):
    result = DeepFace.analyze(img_path,actions=['age','emotion'],enforce_detection=False)
    return result
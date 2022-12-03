from deepface import DeepFace
import cv2
def analyze(img_path):
    result = DeepFace.analyze(img_path,actions=['age','emotion'])
    return result
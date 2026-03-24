import face_recognition
import numpy as np
from PIL import Image

def detect_faces(image: Image.Image) -> list:
    """
    检测图片中的所有人脸位置
    返回格式: [(top, right, bottom, left), ...]
    """
    img_array = np.array(image.convert("RGB"))
    face_locations = face_recognition.face_locations(img_array)
    return face_locations

def get_face_encodings(image: Image.Image) -> list:
    """
    获取所有人脸的128维特征编码
    返回格式: [encoding_1, encoding_2, ...]
    """
    img_array = np.array(image.convert("RGB"))
    face_encodings = face_recognition.face_encodings(img_array)
    return face_encodings

def recognize_faces(unknown_encodings: list, known_encodings: list, known_names: list) -> list:
    """
    识别人脸，返回匹配的姓名列表
    未匹配到则返回 "Unknown"
    """
    names = []
    for encoding in unknown_encodings:
        if not known_encodings:
            names.append("Unknown")
            continue
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
        names.append(name)
    return names

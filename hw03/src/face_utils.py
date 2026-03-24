import cv2
import numpy as np

# 加载 OpenCV 自带的 Haar 人脸检测器（无需 dlib）
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_faces(img_array):
    """
    检测图片中的人脸位置
    返回格式：[(top, right, bottom, left), ...]
    与原 face_recognition 接口保持一致
    """
    # 转为灰度图（Haar 检测器需要灰度输入）
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # 转换为 (top, right, bottom, left) 格式
    face_locations = []
    for (x, y, w, h) in faces:
        face_locations.append((y, x + w, y + h, x))
    
    return face_locations

def load_known_faces():
    """
    纯检测版本：不加载人脸库，返回空列表
    """
    return [], []

def recognize_faces(img_array, known_encodings, known_names):
    """
    纯检测版本：只返回人脸位置，不做识别
    """
    face_locations = detect_faces(img_array)
    # 不识别，所以名字都设为 None
    face_names = [None] * len(face_locations)
    return face_locations, face_names

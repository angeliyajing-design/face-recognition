import cv2
import numpy as np

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

def draw_face_boxes(img_array, face_locations, face_names=None):
    """
    在图片上绘制人脸框和名字（纯 OpenCV 实现）
    :param img_array: 输入图片数组 (RGB 格式)
    :param face_locations: 人脸位置列表 [(top, right, bottom, left), ...]
    :param face_names: 人脸名字列表（可选，无则只画框）
    :return: 绘制后的图片数组
    """
    # 复制图片避免修改原图
    img_with_boxes = img_array.copy()
    
    # 遍历每个人脸
    for i, (top, right, bottom, left) in enumerate(face_locations):
        # 画绿色框 (BGR 格式，OpenCV 默认)
        cv2.rectangle(img_with_boxes, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # 如果有名字，在框下方画名字标签
        if face_names and face_names[i] is not None:
            # 标签背景
            cv2.rectangle(img_with_boxes, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            # 文字
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img_with_boxes, face_names[i], (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)
    
    return img_with_boxes

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

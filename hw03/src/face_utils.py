import face_recognition
import cv2
import numpy as np

def load_known_faces(known_images_dir="known_faces/"):
    """加载已知人脸库（可选功能）"""
    known_encodings = []
    known_names = []
    import os
    for img_name in os.listdir(known_images_dir):
        if img_name.endswith((".jpg", ".png")):
            img_path = os.path.join(known_images_dir, img_name)
            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(img_name)[0])
    return known_encodings, known_names

def detect_faces(image: np.ndarray):
    """检测人脸并返回框位置"""
    face_locations = face_recognition.face_locations(image)
    return face_locations

def recognize_faces(image: np.ndarray, known_encodings, known_names):
    """识别人脸（可选功能）"""
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    face_names = []
    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
        face_names.append(name)
    return face_locations, face_names

def draw_face_boxes(image: np.ndarray, face_locations, face_names=None):
    """在图片上绘制人脸框和标签"""
    for (top, right, bottom, left), name in zip(face_locations, face_names or [""]*len(face_locations)):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        if name:
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)
    return image

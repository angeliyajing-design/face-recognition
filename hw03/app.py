import streamlit as st
import cv2
import numpy as np
from PIL import Image
from src.face_utils import detect_faces, draw_face_boxes, recognize_faces, load_known_faces

st.title("🔍 人脸检测与识别 Demo")

# 上传图片
uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.subheader("原始图片")
    st.image(image, use_column_width=True)

    # 检测人脸
    face_locations = detect_faces(img_array)
    st.info(f"检测到 {len(face_locations)} 张人脸")

    # 可选：加载人脸库并识别
    use_recognition = st.checkbox("启用人脸识别（需要 known_faces 目录）")
    if use_recognition:
        try:
            known_encodings, known_names = load_known_faces()
            face_locations, face_names = recognize_faces(img_array, known_encodings, known_names)
        except:
            st.warning("未找到 known_faces 目录或目录为空，仅显示检测框")
            face_names = None
    else:
        face_names = None

    # 绘制结果
    result_img = draw_face_boxes(img_array.copy(), face_locations, face_names)
    st.subheader("检测结果")
    st.image(result_img, use_column_width=True)

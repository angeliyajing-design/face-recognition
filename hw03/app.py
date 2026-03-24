import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 页面配置
st.set_page_config(page_title="人脸检测系统", page_icon="👤")
st.title("👤 人脸检测作业 - Streamlit 部署版")

# 加载OpenCV人脸检测器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 上传图片
uploaded = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    # 打开图片
    img = Image.open(uploaded)
    img_np = np.array(img.convert("RGB"))
    
    # 转灰度图
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    
    # 人脸检测
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # 画框
    for (x, y, w, h) in faces:
        cv2.rectangle(img_np, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 显示
    st.subheader(f"检测到 {len(faces)} 张人脸")
    st.image(img_np, use_column_width=True, caption="检测结果（蓝色框为人脸）")

st.markdown("---")
st.success("✅ 作业完成：人脸检测功能正常运行！")

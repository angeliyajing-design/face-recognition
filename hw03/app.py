import streamlit as st
from PIL import Image, ImageDraw
from src.face_utils import detect_faces, get_face_encodings, recognize_faces
import numpy as np

# 页面配置
st.set_page_config(page_title="人脸检测与识别", page_icon="👤", layout="wide")
st.title("👤 人脸检测与识别系统")

# 初始化已知人脸库（可在侧边栏扩展）
if "known_face_encodings" not in st.session_state:
    st.session_state.known_face_encodings = []
if "known_face_names" not in st.session_state:
    st.session_state.known_face_names = []

# 侧边栏：已知人脸库管理
with st.sidebar:
    st.header("📚 已知人脸库")
    st.info("可上传已知人脸图片，用于后续识别")
    uploaded_known = st.file_uploader("添加已知人脸", type=["jpg", "jpeg", "png"], key="known")
    if uploaded_known is not None:
        known_img = Image.open(uploaded_known)
        known_encoding = get_face_encodings(known_img)
        if known_encoding:
            name = st.text_input("输入该人脸姓名", key="name")
            if st.button("添加到库") and name:
                st.session_state.known_face_encodings.append(known_encoding[0])
                st.session_state.known_face_names.append(name)
                st.success(f"已添加 {name} 到人脸库")
    st.write("当前库人数：", len(st.session_state.known_face_names))
    if st.session_state.known_face_names:
        st.write("成员：", ", ".join(st.session_state.known_face_names))

# 主区域：图片上传与检测
st.subheader("📸 上传待检测图片")
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("选择图片文件", type=["jpg", "jpeg", "png"])
with col2:
    example_option = st.selectbox("或选择示例图片", ["None", "示例1（单人）", "示例2（多人）"])

# 加载图片
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
elif example_option != "None":
    st.info("示例图片功能：可替换为本地示例图路径")
    # 可取消注释并替换为你本地的示例图路径
    # if example_option == "示例1（单人）":
    #     image = Image.open("examples/single_face.jpg")
    # else:
    #     image = Image.open("examples/multi_faces.jpg")

if image is not None:
    st.subheader("原始图片")
    st.image(image, use_column_width=True, caption="原始上传图片")

    # 人脸检测
    st.subheader("🔍 检测结果")
    face_locations = detect_faces(image)
    st.success(f"检测到 **{len(face_locations)}** 张人脸")

    # 绘制人脸框
    draw_img = image.copy()
    draw = ImageDraw.Draw(draw_img)
    for (top, right, bottom, left) in face_locations:
        draw.rectangle([(left, top), (right, bottom)], outline="#FF0000", width=4)

    # 人脸识别（可选）
    if st.checkbox("✅ 启用人脸识别（需先添加人脸库）"):
        if st.session_state.known_face_encodings:
            unknown_encodings = get_face_encodings(image)
            names = recognize_faces(unknown_encodings, st.session_state.known_face_encodings, st.session_state.known_face_names)
            for i, (top, right, bottom, left) in enumerate(face_locations):
                draw.text((left, top-25), names[i], fill="#FF0000", font_size=20)
        else:
            st.warning("⚠️ 请先在侧边栏添加已知人脸库，再进行识别")

    # 展示最终结果
    st.subheader("📊 检测/识别结果")
    st.image(draw_img, use_column_width=True, caption="标注后的结果图")

# face-recognition
# 人脸检测与识别 Streamlit 应用

## 项目结构
- `src/face_utils.py`: 人脸检测、特征编码、识别核心逻辑
- `app.py`: Streamlit Web 界面入口
- `requirements.txt`: Python 依赖清单

## 功能说明
1. **人脸检测**: 基于 `face_recognition` 库检测图片中的人脸位置，并绘制红色框标注
2. **人脸特征编码**: 提取人脸 128 维特征向量
3. **人脸识别（可选）**: 与已知人脸库比对，输出识别结果标签
4. **Web 界面**: 支持上传图片或选择示例图，可视化展示检测/识别结果

## 环境准备
1. 安装 Python 3.8+
2. 安装依赖: `pip install -r requirements.txt`
3. 系统依赖: 需提前安装 `dlib`（Windows/macOS 需编译版，Linux 可通过包管理器安装）

## 运行方式
```bash
streamlit run app.py
访问本地地址 http://localhost:8501 即可使用。
人脸库准备（可选）
在 app.py 中预先加载已知人脸的编码与姓名，或通过侧边栏上传已知人脸图片构建库。
plaintext

---

## 🚀 4. 运行与验证
1. **创建目录**: 在 GitHub 仓库中新建 `hw03` 文件夹，将上述文件放入
2. **安装依赖**:
   ```bash
   pip install -r requirements.txt
启动应用:
bash
运行
streamlit run app.py
功能测试:
上传含人脸的图片，验证人脸框是否正确标

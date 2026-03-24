## 1. 项目文件
- `app.py` 主程序
- `src/face_utils.py` 人脸工具
- `requirements.txt` 依赖包

## 2. PyCharm 打开项目
1. 打开 PyCharm
2. 点击 `Open`
3. 选中 `hw03` 文件夹打开

## 3. 配置 Python 环境
1. 右上角 → **设置 ⚙️** → **Python Interpreter**
2. 点击 **Add** → **Virtualenv**
3. 选择 **New environment** → **OK**
4. 等待创建完成

## 4. 一键安装所有依赖
打开底部 **Terminal（终端）**，复制粘贴运行：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 5. 一键运行（不用配置，直接跑）
在终端里继续输入：
```bash
streamlit run app.py
```

## 6. 打开使用
运行成功后，浏览器会自动弹出
或手动打开：
http://localhost:8501

## 7. 功能说明
1. 上传图片 → 自动框出人脸
2. 侧边栏可添加已知人脸
3. 勾选识别 → 自动匹配姓名

## 8. 常见问题
- 报错 `No module named...` → 重新运行第4步
- 打不开网页 → 重启终端再运行 `streamlit run app.py`
- 安装慢/失败 → 用上面的清华镜像命令

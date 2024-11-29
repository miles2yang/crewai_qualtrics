# 基於 Python 映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製應用文件到容器
COPY . /app

# 安裝依賴
RUN pip install -r requirements.txt

# 啟動應用
CMD ["python", "app.py"]

# Introduction
這是一個能夠偵測人類的Web Application，使用方式是只要在左邊輸入框拖曳一張影像(png, jpg, jpeg)或是從地端上傳，就能夠偵測出人類並回傳結果


# Download the repositiry
```bash
git clone https://github.com/CCYehTaiwan/IdeasLab.git
```

# Architecture
```bash
|---IdeasLab
|    |---backend
|         |---main.py
|         |---yolo_inference.py
|    |---frontend
|         |---app.py
|    |---.gitignore
|    |---README.md
|    |---requirement.txt

```


## Setup virtual enviroment
```bash
python3 -m venv your_virtual_name
source your_virtual_name/bin/activate
```

## Intall package from requirement
```bash
pip install -r requirement.txt
```

## Implement the server

1. 執行frontend目錄下的app.py檔
   ```bash
   python3 app.py
   ```
2. 執行backend目錄下的main.py
   ```bash
   uvicorn main:app --reload
   ```
3. 於Web Browser上輸入http://127.0.0.1:7860/
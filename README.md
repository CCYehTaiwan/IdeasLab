# Introduction
This web application detects human figures in uploaded images. Users can simply drag and drop an image (supported formats: png, jpg, jpeg) into the input box on the left or upload it from their local storage. Detected results are then displayed on the user interface.


## Download the repositiry
```bash
git clone https://github.com/CCYehTaiwan/IdeasLab.git
```

# Architecture Overview
```bash
|---IdeasLab
     |---backend
          |---main.py
          |---yolo_inference.py
          |---save_data.py
     |---frontend
          |---app.py
     |---.gitignore
     |---README.md
     |---requirement.txt

```


## Setup virtual enviroment
```bash
python3 -m venv your_virtual_name
source your_virtual_name/bin/activate
```

## Intall Required packages
```bash
pip install -r requirement.txt
```

## Running the server

1. Start the frontend server
   ```bash
   python3 app.py
   ```
2. Start the backend server
   ```bash
   uvicorn main:app --reload
   ```
3. Open a web browser and go to http://127.0.0.1:7860/ to view the application.
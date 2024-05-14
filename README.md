# Image Detection Web Application
This server platform integrates front-end and back-end technologies, primarily designed to identify and locate people in images. The project is developed in Python and utilizes the Gradio package to create a user-friendly web interface. The application performs object detection with impressive speed and accuracy by using YOLOv8 model.

![專案封面圖](./homepage.png)

## How to use
1. Access the Application
   - Run the servers, then access the URL http://127.0.0.1:7860
2. Upload an Image
   - In the input section on the left side of the web page, click the upload button to select the image you want to detect.
3. Submit the Image
   - After selecting the image, click the "submit" button to send the image for processing. The system will then detect the people in the image.
4. View Results
   - Once processing is complete, the output section on the right will display the detected objects. Meanwhile, the coordinates of detected objects will be saved in the "backend" directory.


## Architecture Overview
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
- The system architecture is divided into two parts.
- Frontend Operations:
  - Receive the upload image and send the image to backend.
  - Receive the response from backend and present the image on UI.
- Backend Operations:
  - Inference the image by YOLOv8 model.
  - PNG, JPG, or JPEG are required for processing.
  - Save the JSON file with detection information.
  - Return image with bbox.

## Download the repository
```bash
git clone https://github.com/CCYehTaiwan/IdeasLab.git
```

## Setup virtual environment
It is recommended to install Python 3.10.X for required package installation.
```bash
python3 -m venv your_virtual_name
source your_virtual_name/bin/activate
```

## Install required packages
```bash
pip install -r requirement.txt
```

## Run the server

1. Start the frontend server
   ```bash
   python3 app.py
   ```
2. Start the backend server
   ```bash
   uvicorn main:app --reload
   ```
3. Open a web browser and access the URL http://127.0.0.1:7860/.
# Description
This web application detects human figures in uploaded images. Users can simply drag and drop an image (supported formats: png, jpg, jpeg) into the input box on the left or upload it from their local storage. Detected results are then displayed on the user interface.

![專案封面圖](./homepage.png)


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
- The system architecture is divided into two parts:
  - Frontend: Executes app.py, which initiates the Gradio interface.
  - Backend: Runs main, starting up the server at http://127.0.0.1:7860.
- Frontend Operations:
  - Creates a binary stream in memory to store input images before sending a request to the backend.
- Backend Operations:
  - Pre-loads the YOLOv8 model upon server startup to avoid repetitive loading during subsequent requests.
  - Restricts file types to PNG, JPG, or JPEG for processing.
  - Performs image detection on valid files.
  - Stores detection information in a JSON file.
  - Returns images with visual markers indicating detected locations.



## Setup virtual enviroment
```bash
python3 -m venv your_virtual_name
source your_virtual_name/bin/activate
```

## Intall Required packages
It is recommended to install Python 3.10.X for other package installation.
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
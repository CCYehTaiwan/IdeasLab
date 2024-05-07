import cv2
import torch
from PIL import Image

from ultralytics import YOLO

def inference_image(image): 
    # model for inference
    model = YOLO('yolov8n.pt', task="eval")

    with torch.no_grad():
        results = model(image)
        for img in results:
            im_array = img.plot()  # plot a BGR numpy array of predictions
            annotated_image = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB) 
    
            return annotated_image
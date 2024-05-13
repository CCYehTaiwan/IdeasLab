import os
import cv2
import torch
from PIL import Image
from save_data import *


def save_json(image_data, boxes_data, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    
    combined_info = {
        "image_info": json.loads(image_data),
        "detections": [json.loads(box) for box in boxes_data]
    }
    
    with open(os.path.join(save_dir, "combined_data.json"), "w") as f:
        json.dump(combined_info, f, indent=2)
    
    return 
    
def inference_image(model, image): 

    label = {
        "path": "",
        "shape": ()
    }
    boxes = []
    with torch.no_grad():
        results = model(image)
        for item in results:
            label["path"] = item.path
            label["shape"] = item.orig_shape
            
            for source in item.boxes:
                bbox = {
                    "cls_id": int(source.cls.detach().numpy()),
                    "coords": source.xyxy.detach().numpy().flatten().tolist()
                }
                boxes.append(bbox)
    
    image_data = ImageData(**label)
    boxes_data = [BoxesData(**box) for box in boxes]
    
    image_json = image_data.json()
    boxes_json = [box.json() for box in boxes_data]
    
    # make the saving dir for each image
    json_saving_dir = os.path.splitext(os.path.basename(item.path))[0]
    os.makedirs(json_saving_dir, exist_ok=True)
    
    save_json(image_json, boxes_json, json_saving_dir)
        
    for img in results:
        im_array = img.plot()  # plot a BGR numpy array of predictions
        annotated_image = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB) 
    
        return annotated_image
import io
import os
import requests
import gradio as gr
from PIL import Image


def predict(upload_image):
    filename = os.path.basename(upload_image)
    file_format = filename.split(".")[-1]
    
    image = Image.open(upload_image)
    
    img_bytes = io.BytesIO()
    image.save(img_bytes, format=file_format.upper())
    img_bytes.seek(0)

    file = {"file": (filename, img_bytes, f"image/{file_format}")}
    response = requests.post("http://localhost:8000/predict", files=file)
    
    if response.status_code == 200:
        try:
            img = Image.open(io.BytesIO(response.content))
            return img
        except IOError:
            return "Error: Cannot identify image file."
    else:
        return "Error: " + response.text

# setup gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="filepath", label="Upload Image"),
    outputs=gr.Image(type="pil"),
    title="YOLOv8 Object Detection",
    description="Upload an image(jpg, jpeg, png only) and the YOLOv8 model will detect objects in the image."
)

if __name__ == "__main__":
    iface.launch()

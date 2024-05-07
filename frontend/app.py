import io
import requests
import gradio as gr
from PIL import Image


def predict(image):
    # 將圖片轉換為適合發送的格式
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes.seek(0)

    # 向FastAPI後端發送請求
    file = {"file": img_bytes}
    response = requests.post("http://localhost:8000/predict", files=file)
    
    if response.status_code == 200:
        # 從回應中取得圖片數據
        try:
            img = Image.open(io.BytesIO(response.content))
            return img
        except IOError:
            return "Error: Cannot identify image file."
    else:
        return "Error: " + response.text

# 設定Gradio界面
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="YOLOv8 Object Detection",
    description="Upload an image and the YOLOv8 model will detect objects in the image."
)

if __name__ == "__main__":
    iface.launch()

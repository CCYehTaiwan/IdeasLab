import io
from PIL import Image
from yolo_inference import inference_image

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from ultralytics import YOLO

app = FastAPI()
# model for inference
model = YOLO('yolov8n.pt', task="eval")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    
    # check the type of image
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return HTTPException(status_code=400, content={"message": "Invalid file format. Please upload a PNG or JPG file."})
    
    image_data = await file.read()
    
    try:
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        annotated_image = inference_image(model, image)
    except IOError:
        raise HTTPException(status_code=500, detail="Failed to process image")
    
    img_byte_arr = io.BytesIO()
    img = Image.fromarray(annotated_image)
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    
    await file.close()
    
    return StreamingResponse(img_byte_arr, media_type='image/jpeg')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

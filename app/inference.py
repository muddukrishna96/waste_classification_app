from ultralytics import YOLO
from PIL import Image
import numpy as np
# -------------------------
# 1. Load the model ONCE
# -------------------------

# Load YOLO model only once

model = YOLO("/model/best.pt")

def run_inference(pil_image, conf_threshold: float):
    """
    Runs YOLO inference on a PIL image and returns the predicted class 
    with the highest probability above the given confidence threshold.
    If no detections, returns 'No object detected'.
    """
    # Ensure image is RGB
    img = pil_image.convert("RGB")

    # Resize to 640x640
    img_resized = img.resize((640, 640))

    # Convert PIL image -> NumPy array
    img_array = np.array(img_resized)


    # Run inference
    results = model(img_array)

    best_class = None
    best_conf = 0.0

    for r in results:
        for box in r.boxes:
            conf = float(box.conf.cpu().item())
            if conf >= conf_threshold and conf > best_conf:
                best_conf = conf
                best_class = model.names[int(box.cls)]

    if best_class:
        return best_class
    else:
        return "No object detected"

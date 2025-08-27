from ultralytics import YOLO
import cv2
import numpy as np
# -------------------------
# 1. Load the model ONCE
# -------------------------

# Load YOLO model only once

model = YOLO(r"..\..\model\best.pt")


# -------------------------
# 2. Inference Function
# -------------------------

from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO(r"..\..\model\best.pt")

def run_inference(pil_image, conf_threshold: float):
    """
    Runs YOLO inference on a PIL image and returns the predicted class 
    with the highest probability above the given confidence threshold.
    If no detections, returns 'No object detected'.
    """
    # Convert PIL -> NumPy (RGB)
    img = np.array(pil_image)
    # Convert RGB -> BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # Resize
    img_resized = cv2.resize(img, (640, 640))

    # Run inference
    results = model(img_resized)

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

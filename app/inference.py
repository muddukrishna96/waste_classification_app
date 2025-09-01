
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
# -------------------------
# 1. Load the model ONCE
# -------------------------




# Load YOLO model only once

model = YOLO("model/best.pt")
#model = YOLO(r"..\model\best.pt") # local inference
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

    predicted_classes = []

    # Draw bounding boxes on image
    for r in results:
        for box in r.boxes:
            conf = float(box.conf.cpu().item())
            if conf >= conf_threshold:
                cls = model.names[int(box.cls)]
                predicted_classes.append(cls)

                # Bounding box coords
                x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())

                # Draw rectangle
                cv2.rectangle(img_array, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Label with class + confidence
                label = f"{cls} {conf:.2f}"
                cv2.putText(img_array, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Convert back to PIL for display
    boxed_image = Image.fromarray(img_array)

    if predicted_classes:
        return predicted_classes, boxed_image
    else:
        return ["No object detected"], pil_image
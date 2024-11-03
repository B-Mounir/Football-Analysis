from ultralytics import YOLO

model = YOLO("yolov8x")  # Load model

results = model.predict(
    "input_videos/08fd33_4.mp4", save=True
)  # Inference on video

print(results[0])

print("#######################")

for box in results[0].boxes:
    print(box)
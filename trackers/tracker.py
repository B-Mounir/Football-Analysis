from ultralytics import YOLO
import supervision as spv

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTracker()

    def detect_frames(self, frames):
        """
        Detect objects in a list of frames using the model.

        Args:
            frames (list): A list of frames (images) to be processed.

        Returns:
            list: A list of detections for each frame.

        Note:
            The function processes the frames in batches of size 20 for efficiency.
            The confidence threshold for the model's predictions is set to 0.1.
        """
        batch_size = 20
        detections = []
        for i in range(0, len(frames), batch_size):
            batch_frames = frames[i : i + batch_size]
            batch_detections = self.model.predict(batch_frames, conf=0.1)
            detections += batch_detections
        detections = self.model.predict(frames)
        return detections

    def get_object_track(self, frames):
        detections = self.detect_frames(frames)
        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v:k for k,v in cls_names.items()}
            # Convert the detection to supervision format
            detection_supervision = sv.Detections.from_ultralytics(detection)
            print(detection_supervision)
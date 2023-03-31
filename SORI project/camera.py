import torch 
import cv2
import os
import numpy as np

pt_file_path = "./best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', pt_file_path)       

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.current_frame = None

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        results = model(frame)
        a = np.squeeze(results.render())

        desired_classes = {1, 2, 3}
        detected_classes = set()
        detected_counts = {c: 0 for c in desired_classes}
        
        for i, det in enumerate(results.pred):  # per image
            if len(det):
                for c in det[:, 5].unique():
                    c_int = int(c)
                    if c_int in desired_classes:
                        detected_counts[c_int] += 1
                        detected_classes.add(c_int)

            print(detected_classes)

            if detected_classes == desired_classes:
                save_dir = "photos"
                file_num = len(os.listdir(save_dir))

                for i, det in enumerate(results.pred):
                    class_idx = int(det[0, 5])
                    if class_idx in desired_classes:
                        save_path = os.path.join(save_dir, f"detected_{class_idx}_frame_{file_num}_{i}.jpg")
                        bbox = det[0, :4]
                        model.save_crop(frame, bbox, save_path=save_path)

                detected_classes.clear()

            break

        # Render result
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

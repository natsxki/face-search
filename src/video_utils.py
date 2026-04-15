import cv2
import numpy as np
from face_utils import get_face_encodings

def extract_encodings_from_video(video_path, frame_skip=5):
    cap = cv2.VideoCapture(video_path)
    
    encodings = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            rgb = frame[:, :, ::-1]
            frame_encodings, _ = get_face_encodings(rgb)
            encodings.extend(frame_encodings)

        frame_count += 1

    cap.release()

    if len(encodings) == 0:
        return None

    # Average encoding (important!)
    return np.mean(encodings, axis=0)
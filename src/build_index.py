import os
import numpy as np
import pickle
import faiss
import face_recognition

from face_utils import get_face_encodings

ALBUMS_DIR = "../data/albums"
INDEX_PATH = "../data/index/faiss.index"
META_PATH = "../data/index/metadata.pkl"


def build_index():
    face_data = []

    for root, _, files in os.walk(ALBUMS_DIR):
        for file in files:
            if file.lower().endswith((".jpg", ".png", ".jpeg")):
                path = os.path.join(root, file)
                print(f"Processing {path}")

                image = face_recognition.load_image_file(path)
                encodings, locations = get_face_encodings(image)

                for enc, loc in zip(encodings, locations):
                    face_data.append({
                        "encoding": enc,
                        "image_path": path,
                        "location": loc
                    })

    if len(face_data) == 0:
        print("No faces found.")
        return

    encodings = np.array([f["encoding"] for f in face_data]).astype("float32")

    # Build FAISS index
    index = faiss.IndexFlatL2(encodings.shape[1])
    index.add(encodings)

    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

    # Save index + metadata
    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(face_data, f)

    print(f"Indexed {len(face_data)} faces.")


if __name__ == "__main__":
    build_index()
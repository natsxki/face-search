import numpy as np
import pickle
import faiss
import face_recognition

from video_utils import extract_encodings_from_video

INDEX_PATH = "../data/index/faiss.index"
META_PATH = "../data/index/metadata.pkl"


def search_from_image(image_path, k=50):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if not encodings:
        print("No face found in query image.")
        return []

    query = encodings[0].astype("float32")
    return search(query, k)


def search_from_video(video_path, k=50):
    query = extract_encodings_from_video(video_path)

    if query is None:
        print("No face found in video.")
        return []

    query = query.astype("float32")
    return search(query, k)


def search(query_encoding, k):
    index = faiss.read_index(INDEX_PATH)

    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    distances, indices = index.search(np.array([query_encoding]), k)

    results = set()

    for idx in indices[0]:
        if idx < len(metadata):
            results.add(metadata[idx]["image_path"])

    return list(results)


if __name__ == "__main__":
    # Example usage:
    results = search_from_image("../query.jpg")

    print("Matching images:")
    for r in results:
        print(r)
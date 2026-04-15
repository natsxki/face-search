import numpy as np
import pickle
import faiss
import face_recognition

from video_utils import extract_encodings_from_video

INDEX_PATH = "../data/index/faiss.index"
META_PATH = "../data/index/metadata.pkl"
# 0.36 is the squared L2 equivalent of the standard 0.6 Euclidean threshold
DISTANCE_THRESHOLD = 0.36 # the standard face_recognition threshold for a match is a standard Euclidean distance of 0.6. Therefore, we need to filter FAISS results by a squared distance threshold of 0.36 (0.6^2)

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

    # iterate through distances and indices
    for dist, idx in zip(distances[0],indices[0]):
        if dist < DISTANCE_THRESHOLD and idx != -1 and idx < len(metadata):
            results.add(metadata[idx]["image_path"])

    return list(results)


if __name__ == "__main__":

    #Real image to test !!
    results = search_from_image("../query.jpg")

    print(f"Found {len(results)} matching images:")
    for r in results:
        print(r)
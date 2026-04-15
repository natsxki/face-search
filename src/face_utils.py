import face_recognition

def get_face_encodings(image):
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)
    return encodings, locations
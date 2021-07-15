import face_recognition
from numpy import mat
import pickle, json
import time

Widow = face_recognition.load_image_file('./img/known/Black Widow/1.jpg')
Widow_encoding = face_recognition.face_encodings(Widow)[0]

def save_scan(face_id, face_encoding):
    with open(f'{face_id}.dat','wb+') as f:
        pickle.dump(face_encoding, f)
    # with open('dataset_id.dat','wb+') as f:
    #     pickle.dump(face_id, f)

# face_encoding = numpy.empty(128,)

def import_scan(face_id):
    with open(f'{face_id}.dat','rb+') as f:
        face_encoding = pickle.load(f)
        return face_encoding
    #     print(face_encodings)
    # with open('dataset_id.dat','rb+') as f:
    #     face_id = pickle.load(f)
    #     print(face_id)

known_face_id=[
    "Black Widow"
    # saved_face_encodings
]

known_face_encodings = [
    # face_encoding
    Widow_encoding
]

def add_face(id, img_link):    
    Tony = face_recognition.load_image_file(img_link)
    Tony_encoding = face_recognition.face_encodings(Tony)[0]
    known_face_id.append(id)
    known_face_encodings.append(Tony_encoding)    


def scan_img(img_link):
    scanImg = face_recognition.load_image_file(img_link)
    face_locations = face_recognition.face_locations(scanImg)
    face_encodings = face_recognition.face_encodings(scanImg, face_locations)

    result = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)
        
        if True in matches:
            output = known_face_id[matches.index(True)]
            result.append(output)
    
    return result


# add_face("Tony Stark", './img/known/Tony Stark/1.jpg')
result = scan_img('C:/Users/nihal/Desktop/node/present/img/group/group.jpg')
print(result)
save_scan("Black Widow", Widow_encoding)
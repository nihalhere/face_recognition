import face_recognition
import pickle
from PIL import Image, ImageDraw

known_face_ids=[]
known_face_encodings = []

def save_encodings(face_ids, face_encodings):
    with open('encoding_dataset.dat','wb+') as f:
        pickle.dump(face_encodings, f)
    with open('id_dataset.dat','wb+') as f:
        pickle.dump(face_ids, f)

def import_encodings():
    with open('encoding_dataset.dat', 'rb+') as f:
        face_encodings = pickle.load(f)
    with open('id_dataset.dat', 'rb+') as f:
        face_ids = pickle.load(f)
    return face_ids, face_encodings

def add_face(id, img_link, known_face_ids, known_face_encodings):    
    img = face_recognition.load_image_file(img_link)
    face_encoding = face_recognition.face_encodings(img)[0]
    known_face_ids.append(id)
    known_face_encodings.append(face_encoding)   

def scan_img(img_link, known_face_ids, known_face_encodings):
    scanImg = face_recognition.load_image_file(img_link)
    face_locations = face_recognition.face_locations(scanImg)
    face_encodings = face_recognition.face_encodings(scanImg, face_locations)
    result = []
    pil_image = Image.fromarray(scanImg)

    # Create a ImageDraw instance
    draw = ImageDraw.Draw(pil_image)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)
        
        if True in matches:
            output = known_face_ids[matches.index(True)]
            result.append(output)
    

    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_ids[first_match_index]
        
        # Draw box
        draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

        # Draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))


    del draw
    pil_image.show()
    pil_image.save('identify.jpg')
    return result


# add_face("Black Widow", './img/known/Black Widow/1.jpg')
# add_face("Tony Stark", './img/known/Tony Stark/1.jpg')

# known_face_ids,known_face_encodings = import_encodings()
# result = scan_img('C:/Users/nihal/Desktop/node/present/img/group/group.jpg')
# print(result)

def comment():
    # Widow = face_recognition.load_image_file('./img/known/Black Widow/1.jpg')
    # Widow_encoding = face_recognition.face_encodings(Widow)[0]

    # def save_scan(face_id, face_encoding):
    # with open(f'{face_id}.dat','wb+') as f:
    #     pickle.dump(face_encoding, f)

    # def import_scan(face_id):
    #     with open(f'{face_id}.dat','rb+') as f:
    #         face_encoding = pickle.load(f)
    #         return face_encoding
    return

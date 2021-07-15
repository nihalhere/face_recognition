from flask import Flask, request
import json
import processImg

app = Flask(__name__)

known_face_ids=[]
known_face_encodings = []

imgLink = 'C:/Users/nihal/code/node/present/py/downImage.jpg'
known_face_ids, known_face_encodings = processImg.import_encodings()

@app.route('/', methods=['POST'])
def index():
    return "flask"


@app.route('/identify', methods = ['POST'])
def process_image():
    # data = request.get_json()
    data = request.get_data()
    with open('downImage.jpg','wb+') as f:
        f.write(data)
    result = processImg.scan_img(imgLink, known_face_ids, known_face_encodings)
    print(result)
    return json.dumps({"json data": result})


@app.route('/add-face/<id>', methods=['POST'])
def addFace(id):
    data = request.get_data()
    with open('downImage.jpg','wb+') as f:
        f.write(data)
    processImg.add_face(str(id), imgLink, known_face_ids, known_face_encodings)
    processImg.save_encodings(known_face_ids, known_face_encodings)
    return json.dumps({"face added": str(id)})


if __name__ == "__main__": 
	app.run(port=5000, debug=True)
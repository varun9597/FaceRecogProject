from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

encode_file_path = "encodings/"
encode_file = "encodings/encodings.pickle"

# with open(encode_file,'rb') as rfp:
#     existing_encodes = pickle.load(rfp)

print(set(list(existing_encodes["names"])))

def check_file_exist():
    if not os.path.exists(encode_file_path):
        os.mkdir(path)
    else:
        return True

def check_encodings_exist():
    with open(encode_file,'rb') as rfp:
        existing_encodes = pickle.load(rfp)

names_list = set(list(existing_encodes["names"]))
encodings_list = set(list(existing_encodes["encodings"]))

imagePaths = list(paths.list_images("/home/pi/FaceRecogProject/TestCase1/dataset"))
print(imagePaths)

knownEncodings = names_list
knownNames = encodings_list

for(i,imagePath) in enumerate(imagePaths):
    name = imagePath.split(os.path.sep)[-2]
    print(name)

    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb,model="hog")

    encodings = face_recognition.face_encodings(rgb, boxes)


    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
    

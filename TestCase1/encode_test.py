from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

encode_file_path = "encodings/"
encode_file = "encodings/encodings.pickle"
dataset_name_list = []

# with open(encode_file,'rb') as rfp:
#     existing_encodes = pickle.load(rfp)

#print(set(list(existing_encodes["names"])))

def check_file_exist():
    if not os.path.exists(encode_file_path):
        os.mkdir(path)
    else:
        return True

def check_encodings_exist():
    with open(encode_file,'rb') as rfp:
        existing_encodes = pickle.load(rfp)
        return existing_encodes
        

exist_encode = check_encodings_exist()

exisitng_names = list(set(list(exist_encode["names"])))
existing_encodings = list(exist_encode["encodings"])

#print(existing_encodings)
value = "Varun"

#if value not in list(set(list(exist_encode["names"]))):    


#names_list = set(list(existing_encodes["names"]))
#encodings_list = set(list(existing_encodes["encodings"]))

imagePaths = list(paths.list_images("/home/pi/FaceRecogProject/TestCase1/dataset/"))
# print(imagePaths)

knownEncodings = names_list
knownNames = encodings_list

for(i,imagePath) in enumerate(imagePaths):
    #print(imagePath)
    dataset_name_list.append(imagePath[44:52])

print(list(set(dataset_name_list)))

    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb,model="hog")

    encodings = face_recognition.face_encodings(rgb, boxes)


    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
    

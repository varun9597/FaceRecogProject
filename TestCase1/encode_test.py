from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

encode_file_path = "encodings/"
encode_file = "encodings/encodings.pickle"
dataset_name_list = []

def check_file_exist():
    if not os.path.exists(encode_file_path):
        os.mkdir(path)
    else:
        return True

def check_encodings_exist():
    with open(encode_file,'rb') as rfp:
        existing_encodes = pickle.load(rfp)
        return existing_encodes
        
#THIS PART IS USED TO GET THE EXISTING NAMES AND ENCODINGS FROM THE EXISTING PICKLE FILE
exist_encode = check_encodings_exist()
existing_names = list(set(list(exist_encode["names"])))
existing_encodings = list(exist_encode["encodings"])

knownEncodings = existing_encodings
knownNames = existing_names

#NOW, WE FETCH LIST OF NAMES IN THE DATASET FOLDER   ------- dataset_name_list ==[]
imagePaths = list(paths.list_images("/home/pi/FaceRecogProject/TestCase1/dataset/"))

for(i,imagePath) in enumerate(imagePaths):
    dataset_name_list.append(imagePath[44:52])

#IF VALUE IN DATASET FOLDER DOES NOT MATCH KNOWN NAMES THEN TRAIN 
for(j,value) in enumerate(dataset_name_list):
    if value not in knownNames:
        print("New value found")

# print(list(set(dataset_name_list)))
# print(knownNames)

#     image = cv2.imread(imagePath)
#     rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     boxes = face_recognition.face_locations(rgb,model="hog")

#     encodings = face_recognition.face_encodings(rgb, boxes)


#     for encoding in encodings:
#         knownEncodings.append(encoding)
#         knownNames.append(name)
    
# print(knownEncodings)
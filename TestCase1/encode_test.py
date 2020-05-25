from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

encode_file_path = "encodings/"
encode_file = "encodings/encodings.pickle"
dataset_name_list = []
encode_format_list = ['encodings','names']
blank_dict = {key:[] for key in encode_format_list}

def check_file_exist():
    if not os.path.isfile(encode_file):
        with open(encode_file,'wb') as file:
            pickle.dump(blank_dict, file)
        return True
    
    else:
        return True

def check_encodings_exist():
    with open(encode_file,'rb') as rfp:
        existing_encodes = pickle.load(rfp)
        return existing_encodes
        
#THIS PART IS USED TO GET THE EXISTING NAMES AND ENCODINGS FROM THE EXISTING PICKLE FILE
encode_file_exist = check_file_exist()
exist_encode = check_encodings_exist()
existing_names = list(set(list(exist_encode["names"])))
existing_encodings = list(exist_encode["encodings"])

knownEncodings = exist_encode["encodings"]
knownNames = exist_encode["names"]

#NOW, WE FETCH LIST OF NAMES IN THE DATASET FOLDER   ------- dataset_name_list ==[]
dataset_folder_path = "/home/pi/FaceRecogProject/TestCase1/dataset/"
#imagePaths = list(paths.list_images("/home/pi/FaceRecogProject/TestCase1/dataset/"))
dataset_name_list = [ f.path[len(dataset_folder_path):] for f in os.scandir(dataset_folder_path) if f.is_dir() ]
print(dataset_name_list)


#IF VALUE IN DATASET FOLDER DOES NOT MATCH KNOWN NAMES THEN TRAIN 
for value in dataset_name_list:
    if value in existing_names:
        print("Value already exist---"+str(value))
        continue
    else :
        imagePaths = list(paths.list_images(str(dataset_folder_path)+str(value)))
        for (i,imagePath) in enumerate(imagePaths):
            
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb, model="hog")

            encodings = face_recognition.face_encodings(rgb, boxes)

            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(value)

data = {"encodings":knownEncodings, "names":knownNames}
f = open(encode_file,"wb")
f.write(pickle.dumps(data))
f.close()
print("Done")



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
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

imagePaths = list(paths.list_images("/home/pi/FaceRecogProject/dataset"))
#print(imagePaths)

for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)
	print(name)

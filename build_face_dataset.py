# USAGE
# python build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/adrian

# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

cont_var = ord("y")

while cont_var==ord("y") :
	sem_num = input("Enter Sem Number : ")
	usr_name = input("Enter User Name : ")


	# load OpenCV's Haar cascade for face detection from disk
	detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	# initialize the video stream, allow the camera sensor to warm up,
	# and initialize the total number of example faces written to disk
	# thus far
	print("[INFO] starting video stream...")
	#vs = VideoStream(src=0).start()
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)
	total = 0

	os.mkdir("dataset/CompSem"+str(sem_num)+"/"+str(usr_name)+"/")

	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream, clone it, (just
		# in case we want to write it to disk), and then resize the frame
		# so we can apply face detection faster
		frame = vs.read()
		orig = frame.copy()
		frame = imutils.resize(frame, width=400)

		# detect faces in the grayscale frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rects = detector.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
		
		# loop over the face detections and draw them on the frame
		for (x, y, w, h) in rects:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			#q = os.path.sep.join([args["output"], "{}.png".format(str(99).zfill(5))])
			
			cv2.imwrite("dataset/CompSem"+str(sem_num)+"/"+str(usr_name)+"/"+str(total)+".jpg", gray[y:y+h,x:x+w])
			total+=1
		
		# show the output frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		 
		# if the `k` key was pressed, write the *original* frame to disk
		# so we can later process it and use it for face recognition
		if key == ord("k"):
		#	p = os.path.sep.join([args["output"], "{}.png".format(
		#		str(total).zfill(5))])
		#	cv2.imwrite(p, orig)
		#	total += 1
			break
		# if the `q` key was pressed, break from the loop
		elif key == ord("q"):
			break
		elif (total>=30):
			break
	# do a bit of cleanup
	print("[INFO] {} face images stored".format(total))
	print("[INFO] cleaning up...")
	cv2.destroyAllWindows()
	vs.stop()
	cont_var = ord(input("Continue? [Y/N]"))

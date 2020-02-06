from tkinter import *
from tkinter import ttk
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
import shutil

#cont_var = ord("y")
def dataset_collection(*args):
	#while cont_var==ord("y") :
	#sem_num = input("Enter Sem Number : ")
	sem_num = str(semester.get())
	#usr_name = input("Enter User Name : ")
	usr_name = str(username.get())
	sam_count = int(sample_count.get())


	# load OpenCV's Haar cascade for face detection from disk
	detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	# initialize the videostream, allow the camera sensor to warm up,
	# and initialize the total number of example faces written to disk
	# thus far
	print("[INFO] starting video stream...")
	#vs = VideoStream(src=0).start()
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)
	total = 0
	
	path = "dataset/CompSem"+str(sem_num)+"/"+str(usr_name)+"/"
	if not os.path.exists(path):
		os.mkdir(path)
	else:
		shutil.rmtree(path)
		os.mkdir(path)

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
		elif (total>=sam_count):
			status.set("COMPLETED")
			break
	# do a bit of cleanup
	print("[INFO] {} face images stored".format(total))
	print("[INFO] cleaning up...")
	cv2.destroyAllWindows()
	vs.stop()
	#cont_var = ord(input("Continue? [Y/N]"))


#def calculate(*args):
#	print(2)
#	value=float(feet.get())
#	meters.set((0.3048 * value * 10000.0 + 0.5 / 10000.0))
	

	
root = Tk()
root.title("Dataset Collection")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

semester=StringVar()
username= StringVar()
status=StringVar()
sample_count=IntVar()

ttk.Label(mainframe, text="Semester:").grid(column=1, row=1, sticky=E)
sem_entry = ttk.Entry(mainframe, width=7,textvariable=semester)
sem_entry.grid(column=3, row=1, sticky=(W,E))

ttk.Label(mainframe, text="Name:").grid(column=1, row=2, sticky=E)
name_entry = ttk.Entry(mainframe, width=7,textvariable=username)
name_entry.grid(column=3, row=2, sticky=(W,E))

ttk.Label(mainframe, text="Samples:").grid(column=1, row=3, sticky=E)
sample_entry = ttk.Entry(mainframe, width=7,textvariable=sample_count)
sample_entry.grid(column=3, row=3, sticky=(W,E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Collect",command=dataset_collection).grid(column=2, row=4,sticky=W)

ttk.Label(mainframe, textvariable=status).grid(column=2, row=5, sticky=(W,E))

root.mainloop()

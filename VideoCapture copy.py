import cv2
import math
import numpy as np
import os
import face_recognition

def captureVid(videoFile, seconds):#mp4 file, seconds to be captured 
	os.mkdir(videoFile[0:3])
	vidcap = cv2.VideoCapture(videoFile)# for face_location in face_locations:
	success,image = vidcap.read()
	fps = vidcap.get(cv2.CAP_PROP_FPS)
	multiplier = int(round(fps * seconds))
	i = 1
	while success: 
		frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
		success, image = vidcap.read()
		if (frameId % multiplier == 0):
			face_locations = face_recognition.face_locations(image)
			face_num = len(face_locations)
			print face_num
			if (face_num > 0): 
				print "%s/face%d.jpg"
				cv2.imwrite("%s/face%d.jpg" % (videoFile[0:3], i), image)
				i=i+1

captureVid('BTS.mp4', 1.5)
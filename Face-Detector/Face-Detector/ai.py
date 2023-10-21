import face_recognition as FR
from cv2 import VideoCapture, resize
from numpy import argmin
import pickle


signatures = None
distance = None

def load_data():
	global signatures
	global distance

	fd = open("facial.bin", "rb")
	data = pickle.load(fd)
	signatures = data["encodings"]
	distance = data["distance"]
	fd.close()
	print("[+] AI Facial Data Loaded...")

def recognize(frame_s):
	global distance
	#frame_s = resize(frame, (0,0), fx=0.50, fy=0.50)
	encodings = FR.face_encodings(frame_s)

	if(len(encodings) > 0):
		for encoding in encodings:
			hits = FR.compare_faces(signatures, encoding)

			distances = FR.face_distance(signatures, encoding)
			match_index = argmin(distances)
			if(distance >= distances[match_index]):
				return hits[match_index]

		return False

def get_frame(cam_uri):
	try:
		return VideoCapture(cam_uri).read()
	except:
		return (False, None)

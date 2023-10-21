#!/usr/bin/python3

print("[*] Loading....")
import face_recognition as FR
import cv2
import pickle
from numpy import argmax
print("[+] Loaded")

from sys import argv

encodings = {"encodings":[], "distance":0}

def encode_face(cam_uri, frame_count):
	global encodings
	counter = 0
	print("[+] Enroll Frame Capture Count: {}".format(frame_count))

	while frame_count > counter:
		flag, frame = cv2.VideoCapture(cam_uri).read()
		if(flag):
			encoding = FR.face_encodings(frame)
			if(len(encoding) > 0):
				print("Face Detected: Frame: {}".format(counter))
				encodings["encodings"].append(encoding[0])
				counter += 1
			else:
				print("[!] No face detected")

	distances = FR.face_distance(encodings["encodings"], encodings["encodings"][5])
	encodings["distance"] = distances[argmax(distances)]
	fd = open("facial.bin", "wb")
	pickle.dump(encodings, fd)
	fd.close()
	print("[+] Saved Facial Encodings...")
	print("[+] Done")


try:

	ip = "192.168.4.1"
	encode_face("http://{}/capture".format(ip), 10)

except IndexError:
	print("Usage: ./{}".format(argv[0]))

except Exception as e:
	print("[!] Exception: '{}' -->>>> [EXEC-SHUTDOWN]".format(str(e)))

from cv2 import VideoCapture
import tensorflow_hub as hub

detector = hub.load("model")
print("[+] Model Ready")

def get_label(classes, scores):
	index = 0

	while index < len(scores):

		check_1 = classes[index].numpy() == 47
		score = int(scores[index].numpy() * 100) >= 35

		if (check_1 and score):
			return True
		index += 1

	return False


def identify(image_tensor):
	neg_img = 1 - image_tensor
	output = detector([neg_img])
	return get_label(output['detection_classes'][0], output['detection_scores'][0])

def get_frame(cam_uri):
	try:
		return VideoCapture(cam_uri).read()
	except:
		return (False, None)

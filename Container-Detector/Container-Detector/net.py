import requests

def scan_net(NET_ID):

	HOST_ID = 1

	while True:
		try:
			response = requests.get("http://{}.{}/id".format(NET_ID, HOST_ID))
			if(response.status_code == 200 and response.text == "RELAY" ):
				return "{}.{}".format(NET_ID, HOST_ID)

		except KeyboardInterrupt:
			exit()
		except:
			pass
		if(HOST_ID == 254):
			HOST_ID = 0;
		else:
			print("[*] Scanning....")
			HOST_ID += 1


def send_command(ip, command):
	try:
		resp = requests.get("http://{}/{}".format(ip, command))
		return resp
	except:
		return None

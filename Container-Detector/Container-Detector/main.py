#!/usr/bin/python3

from net import *
from ml import *
from time import sleep

relay = None

def main():

	global relay

	relay = scan_net("192.168.4")
	print("[+] Control Relay: => {}".format(relay))
	send_command(relay, "off")


	while True:
		try:
			result = get_frame("http://192.168.4.1/capture")
			if(result[0]):
				state = identify(result[1])
				if(state):
					print("[+] TRIGGER ON")
					send_command(relay, "on")
					sleep(5)
					print("[+] TRIGGER OFF")
					send_command(relay, "off")
				else:
					print("[-] NO DETECTION")

		except KeyboardInterrupt:
			exit()

		except Exception as e:
			print(e)
			pass


main()

#!/usr/bin/python3

import ai
from net import *
from time import sleep

relay = None

def main():
	global relay

	relay = scan_net("192.168.4")
	print("[+] Control Relay: => {}".format(relay))
	send_command(relay, "off")
	ai.load_data()

	while True:
		try:
			result = ai.get_frame("http://192.168.4.1/capture")
			if(result[0]):
				match = ai.recognize(result[1])
				if(match):
					print("[+] Activating Circuit")
					send_command(relay, "on")
					sleep(2)
					print("[+] Deactivating Circuit")
					send_command(relay, "off")
					sleep(2)

		except KeyboardInterrupt:
			exit()

		except Exception as e:
			print(e)
			pass


main()

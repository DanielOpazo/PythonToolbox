#!/usr/bin/python
import sys
import socket
#sys.stdout.write("hello from Python %s\n" % (sys.version,))

def sendTCP(ip, port, bufferSize):
	TCP_IP = ip
	TCP_PORT = port
	TCP_BUFFER = bufferSize
	MESSAGE = "test message"
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((TCP_IP, TCP_PORT))
	sock.send(MESSAGE)
	data = sock.recv(TCP_BUFFER)
	sock.close()
	print "Message Sent"
	print 'received data: ', data

def TCPServer(ip, port, bufferSize):
	TCP_IP = ip
	TCP_PORT = port
	BUFFER_SIZE = bufferSize
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((TCP_IP, TCP_PORT))
	sock.listen(1)

	conn, addr = sock.accept()
	print 'Connection address:', addr
	data = conn.recv(BUFFER_SIZE)
	print 'recevied data:', data
	conn.send(data)
	conn.close()
		
if __name__ == "__main__":
	"""
	Warning: There is no checking if the inputs are valid or not, only that the correct number are there
	If you enter an invalid IP address or port number, the program will crash.
	So type carefully.
	"""
	if len(sys.argv) < 2:
		print "incorrect number of arguments"
	else:
		mode = sys.argv[1]
		if mode == "s":
			#run server
			if len(sys.argv) > 4:
				print "running server"
				TCPServer(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
			else:
				print "incorrect number of arguments"
		elif mode == "c":
			#run client
			if len(sys.argv) > 4:
				print "running client"
				sendTCP(sys.argv[2], int(sys.argv[3]), int (sys.argv[4]))
			else:
				print "incorrect number of arguments"
		else:
			print "unknown mode %s" % mode

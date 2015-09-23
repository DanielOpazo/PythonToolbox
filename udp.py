#! python
import sys
import socket
#sys.stdout.write("hello from Python %s\n" % (sys.version,))

def sendUDP(ip, port):
	UDP_IP = ip
	UDP_PORT = port
	MESSAGE = "test message"
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	print "Message sent"

def udpServer(ip, port, bufferSize):
	UDP_IP = ip
	UDP_PORT = port
	BUFFER_SIZE = bufferSize
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((UDP_IP, UDP_PORT))
	
	data, addr = sock.recvfrom(BUFFER_SIZE)
	print "received message: %s from %s" % (data, addr)

if __name__ == "__main__":
	"""
	Warning: There is no checking if the inputs are valid or not, only that the correct number are there"
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
				udpServer(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
			else:
				print "incorrect number of arguments"
		elif mode == "c":
			#run client
			if len(sys.argv) > 3:
				print "running client"
				sendUDP(sys.argv[2], int(sys.argv[3]))
			else:
				print "incorrect number of arguments"
		else:
			print "unknown mode %s" % mode
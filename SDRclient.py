from socket import * 
serverName = '127.0.0.1' 
serverPort = 400



while 1:
	print()
	data = input("Data to send: ")
	clientSocket = socket(AF_INET, SOCK_STREAM) 
	clientSocket.connect((serverName,serverPort)) 
	clientSocket.send(data.encode()) 
	print ("Data sent")
	clientSocket.close()

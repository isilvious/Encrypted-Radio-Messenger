from socket import *
import sounddevice as sd
import math
import numpy as np
import random
import time

	
#Set up server
fs = 44100
encriptionkey = 90

serverAddress = '127.0.0.1'
serverPort = 400
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverAddress,serverPort)) 
serverSocket.listen(1) 
print('The server is ready to receive')

#Tools
def asciiToBinary(message):
    binary = ""
    hexString = ""
    for i in message:
        hexString += hex(ord(i)) + " "
        bits = bin(ord(i))[2:].zfill(8)
        binary += bits
    #  print(hexString)
    return binary

def BinaryToAscii(binary):
    hexP = b''
    hexString = ''
    for i in range(0, len(binary), 8):
        hexP += int((binary[i: i + 8]), 2).to_bytes(1, byteorder='big')
        hexString += hex(int((binary[i: i + 8]), 2)) + " "
    #print(hexString)
    #print(hexP)
    return hexP

#encryption/decryption
def encrypt(data):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.','!','?',',']
	newalphabet = []
	random.seed(encriptionkey)
	newdata = ''
	
	for i in range(0, len(alphabet)-1):
		newalphabet.append(alphabet.pop(random.randint(0, len(alphabet)-1)))
	
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.','!','?',',']
	
	for c in data:
		charnotfound = True
		for i in range(0, len(alphabet)-1):
			if c == alphabet[i]:
				newdata += newalphabet[i]
				charnotfound = False
		if charnotfound:
			newdata += ' '
	
	print('encrypted data: ' + newdata)
	
#def decrypt(data):
	
	
	
#play the bits through the sound card

def tone(time, frequency):
    toneArray = []
    for t in np.arange(0, time, time/(frequency*4)):
        toneArray.append(math.sin(2*math.pi*frequency*t))
    return toneArray

# The function below amplitude modulates the signal

def demodulate(samples):
    #Sync with preamble. 
	#randome line to delete later
	sample =+ 1

def modulate(message, frequency, time):
	output = []
	print('Msg to bits: ' + message)
	for c in message:
		if c == '1':
			output.extend(tone(time, frequency))
		else:
			output.extend([0]*frequency*4)

	return output

#assemble/prepare data
def send(data):
	
	datastr = data.decode('utf-8')
	encrypt(datastr)
	databin = asciiToBinary(datastr)
	
	nparray = modulate(databin, 440, 3.8)
	#for i in range (1, 30):
	sd.play(nparray, fs)
		#time.sleep(10)
	
	datastr = data.decode('utf-8')
	databin = asciiToBinary(datastr)
	#print(databin)

#constant listener
while 1: 
	connectionSocket, addr = serverSocket.accept()
	print()
	print("Connection Accepted")
	data = connectionSocket.recv(1024)
	print('Message recv: ' + data.decode())
	send(data)
	connectionSocket.send(data) 
	connectionSocket.close()

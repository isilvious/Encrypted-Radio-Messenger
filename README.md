Encrypted-Radio-Messenger By: Isaac Silvious

Includes: SDRclient.py SDRserver.py

The idea of this project was to have computers on a closed network be able to send "encrypted" packets over the radio. As of right now, the server accepts strings from the client, applies a simply encryption, converts it to bits, and plays the bits through the sound card (sound on for 1, sound off for 0). If the computer is connected to a radio transmitter, the bits can be captured by a different computer through a SDR. I currently do not have a program to capture the bits and convert them back to a string. 

Important: The encryption method is currently not good. Don't rely on it at all!
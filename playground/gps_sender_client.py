import socket

import time
starttime = time.time()

while True:
    try:
        time.sleep(3)
        # print("hi")
        #direction
        #buzzer

        msgFromClient = "16.381392,48.211338"
        bytesToSend = str.encode(msgFromClient)
        serverAddressPort = ("127.0.0.1", 24001)
        bufferSize = 1024
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])

        print(msg)
    except Exception as e:
        continue
import socket

# msgFromClient = "lep_2021_03_04_T_11_17_07__893.png"
# msgFromClient = "187-184.312-530.22-501-lep_2021_03_04_T_11_17_07__893.png"
msgFromClient = "187-184.312-530.22-501-lep_2021_04_12_T_17_29_01__335.png"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
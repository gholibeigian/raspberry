#it works with project learn_server2.client
# it takes msgFromClient = "187-184.312-530.22-501-lep_2021_03_04_T_11_17_07__893.png"
#TODO chage the udp socket on raspberry -> remove altitude and longitude from tne massage
import socket
import time
from datetime import datetime
import socket_file_request
import corona_alarm

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    data = message.decode("utf-8")
    print('DATA:   received ', data)
    raw_data = data.split("-")
    print(raw_data)
    max_red = raw_data[0]
    avgRedMinValue = raw_data[1]
    avgRedMaxValue = raw_data[2]
    hightRedCount = raw_data[3]
    date_time_data = raw_data[4]
    # receive data(alarm) here and load the gui!
    alarm_date_time = datetime.strptime(date_time_data, 'lep_%Y_%m_%d_T_%H_%M_%S__%f.png')
    print(alarm_date_time)
    # sleep for 3 seconds
    print(alarm_date_time)
    # send the soncket request for 3 second
    # request_files_after_alarm = socket_file_request.Socket_file_request("alarm/" + alarm_date_time,3.00)

    # TypeError: can only concatenate str (not "float") to str
    request_files_after_alarm = socket_file_request.Socket_file_request("alarm/" + "lep_2021_04_12_T_17_29_02__258.png",
                                                                        "3.00")
    request_files_after_alarm.send_socket()
    # time.sleep(3)

    alarm_label = "New Alarm From Corona Alarm Kit\nmaxRed: {}\nAverage Min Value: {}\nAverage Max Value: {}\nCount of Hightest pixels: {}\nDate Time:{}\nAltitude: 48.20302872428539\nLaltitude: 16.36892920432462".format(max_red,avgRedMinValue,avgRedMaxValue,hightRedCount,alarm_date_time)

    time.sleep(15)
    new_corona_alarm = corona_alarm.Corona_alarm("images", alarm_label)
    print(clientMsg)
    print(clientIP)

    # Apply here:


    # UDPServerSocket.sendto(bytesToSend, address)


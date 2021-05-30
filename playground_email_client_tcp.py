# it is integrated into the raspberry pi iot_raspberry_class_final
import socket#, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"#socket.gethostname()
port = 7897#24015
# connection to hostname on the port.
s.connect((host, port))

#new_msg = "16.334343,48.239931"

# new_msg = "email"
s.sendall("kokolubilubi@gmail.com".encode("ascii"))
# time.sleep(1)

# Receive no more than 1024 bytes
# msg = s.recv(1024)

s.close()
# print(msg.decode('ascii'))
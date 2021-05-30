# it works with gps server
import socket, time

while True:
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    #host = socket.gethostname()
    host = "127.0.0.1"
    port = 9999
    # connection to hostname on the port.
    s.connect((host, port))
    # new_msg = "16.334343,48.239931"
    # new_msg = "16.372796,48.209020" #(False, True, 4, 145, 321, False, False)
    # new_msg = "16.373803,48.208442" #(False, True, 4, 28, 273, False, True)
    # new_msg = "16.373562,48.208095" #(False, True, 4, 29, 16, False, True)
    # new_msg = "16.373834,48.208112" #(False, True, 4, 7, 103, False, True)
    # new_msg = "16.373872,48.207973" #(False, True, 4, 22, 105, False, True)
    # new_msg = "16.373872,48.207973" #(False, True, 4, 22, 105, False, True)
    # #new + 90
    # new_msg = "16.372853,48.208153" #(False, True, 3, 107, 1, False, False)
    # new_msg = "16.371695,48.208199" #(False, True, 3, 236, 89, False, False)
    # new_msg = "16.373500,48.209622" #(False, True, 3, 107, 1, False, False)
    # new_msg = "16.375448,48.208248" #(False, True, 3, 107, 1, False, False)
    # new_msg = "16.373476,48.208807" #(False, True, 3, 107, 1, False, False)
    # new_msg = "16.373444,48.207440" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.372760,48.208153" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.373778,48.207341" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.373673,48.208699" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.373838,48.208584" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.374053,48.208595" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.374061,48.208267" #(False, True, 4, 88, 152, False, False)
    # new_msg = "16.371857,48.208101" #(False, True, 3, 218, 2, False, False) must be 0
    # new_msg = "16.373735,48.207331" #(False, True, 4, 90, 84, False, False) must be 90
    # new_msg = "16.373503,48.209602" #(False, True, 4, 156, 76, False, False) must be 180
    # new_msg = "16.375662,48.208189" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.371809,48.208061" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.373641,48.209702" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.373743,48.208634" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.373801,48.207318" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.371769,48.208259" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375163,48.208314" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.374729,48.209024" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375533,48.207586" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375150,48.208812" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372429,48.208668" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372316,48.208493" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372383,48.207791" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375662,48.207728" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.373025,48.207542" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372397,48.208298" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.373684,48.208766" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372488,48.208798" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375111,48.208830" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372402,48.208651" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.372922,48.207611" #(False, True, 4, 205, 179, False, False) must be 180
    # new_msg = "16.375583,48.207625" #(False, True, 4, 205, 179, False, False) must be 180
    new_msg = "16.374054,48.207167" #(False, True, 4, 205, 179, False, False) must be 180



    s.sendall(new_msg.encode("ascii"))
    time.sleep(5)

    # Receive no more than 1024 bytes
    msg = s.recv(1024)

    s.close()
    print(msg.decode('ascii'))
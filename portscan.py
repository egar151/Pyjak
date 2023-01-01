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
    t1 = datetime.now()
    try:
        for port in range (1,5000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result ==0:
                print ("Port {}:        Open".format(port))
                sock.close()  
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print ("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()
    input("Press any key to continue...")


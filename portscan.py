import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import Figlet


def portmain(ips=['None'],port=666):


    subprocess.call('clear')
    f = Figlet(font='standard') 
    print(f.renderText('Port Scanner'))
    print('Enter Q to Exit')
    if port != 666:
        print("_" * 60)
        print ("Please wait, scanning remote host", ips[0], ' on port ' , port)
        print ("_" *60)
        remoteServerIP = socket.gethostbyname(ips[0])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port: ',port,' is Open')
        else:
            print('Port: ',port,' is Closed')
        sock.close()
        print()
        input("Press Any Key to Continue...")
        return
    else:
        if ips[0] == 'None':
            ips[0] = input("Enter a remote host to scan: ")
            if ips[0].upper() == 'Q':
                ips[0] = 'None'
                return
        else:
            print("Port Scaning the following Host: ")
            for i in range(len(ips)):
                print(ips[i])
        
        for i in ips:
            t1 = datetime.now()
            remoteServerIP = socket.gethostbyname(i)

            print("_" * 60)
            print ("Please wait, scanning remote host", remoteServerIP)
            print ("_" *60)
            try:
                for port in range (1,5000):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP, port))
                    if result == 0:
                        print ("Port {}:        Open".format(port))
                    sock.close()  
            except KeyboardInterrupt:
                print ("You pressed Ctrl+C")
                input("Press any key to continue...")
            except socket.gaierror:
                print ("Hostname could not be resolved. Exiting")
                input("Press any key to continue...")
                sys.exit()
            except socket.error:
                print ("Couldn't connect to server")
                input("Press any key to continue...")
                sys.exit()
            t2 = datetime.now()
            total = t2 - t1
            print('Scanning Completed of',remoteServerIP,' in ', total)
    ips[0] = 'None' 
    input("Press any key to continue...")


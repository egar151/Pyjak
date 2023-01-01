import subprocess
from pyfiglet import Figlet
import os


def pingmain(stat):
    if stat == 0:
        os.system('clear')
        f = Figlet(font='standard') 
        print(f.renderText('Ping IP'))
    else:
        print()   
    print("""
A: All
B: Specific 
Q: Back to Main Menu""")
    choice = input("""
Please enter your choice: """)

    if choice == "A" or choice =="a":
        bynet()
    elif choice == "B" or choice =="b":
        selected()
    elif choice=="Q" or choice=="q":
        print("Bye")
    else:
        print("You must only select either A or B")
        print("Please try again")
        pingmain(1)



###########################################################################################

def bynet():
    os.system('clear')
    f = Figlet(font='standard')
    print(f.renderText('Ping IP'))
    IP = input("Enter the Host IP Address:\t")
    ipnetpar = IP.split('.')
    IPs=IP

    dot = IP.rfind(".")
    IP = IP[0:dot + 1]

    ipsub = input("Please enter subnet: ")

    live = 0
    dead = 0

    start = int(ipnetpar[3])
    end = 1
    hosts='a'
    hostlist = []

    if ipsub == '28':
        end = start + 14
        if end < 255:
         hosts = str(ipnetpar[0])+'.'+str(ipnetpar[1])+'.'+str(ipnetpar[2])+'.'+str(end-1)

    if ipsub == '24':
        end = start + 254
        if end <= 255:
         hosts = str(ipnetpar[0])+'.'+str(ipnetpar[1])+'.'+str(ipnetpar[2])+'.'+str(end-1)

    print("Starting Ping Sweeper on " + IPs + " To " + hosts)

    for i in range(start, end):
        host = IP + str(i)
        try:
           response = subprocess.check_output(['ping', '-c 1', '-W 1' , host]) 
           print(host + ' is live')
           hostlist.insert(live,host)
           live = live + 1
        except:
            dead = dead + 1
            print(host + ' is down')
    print(str(live) + ' host are up and ' + str(dead) +' host are down')
    print ("Totals IPs Scaned: "+str(live+dead))
    print("Live IPs")
    for ipss in hostlist:
        print(ipss) 
    print()
    input("Press Any Key to Continue...")
    pingmain(0)



###########################################################################################

def selected():
    os.system('clear')
    f = Figlet(font='standard')
    print(f.renderText('Ping IP'))
    ipnet = input("Please enter IP: ")
    try:
        outputs = subprocess.check_output(['ping', '-c 1', ipnet])
        subprocess.run(['ping', '-c 4', ipnet])
        if b'0 packets received' in outputs:
            print("IP Not Live")
        else:
            print()
            print()
            print('IP is Live')
    except:
        print()
        print('Not Found')
    print()
    input("Press any key to Continue...")
    pingmain(0)



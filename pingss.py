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

def bynet():
    os.system('clear')
    f = Figlet(font='standard')
    print(f.renderText('Ping IP'))
    ipnet = input("Please enter Network Gateway: ")
    ipsub = input("Please enter subnet: ")
    print('Pass')

def selected():
    os.system('clear')
    f = Figlet(font='standard')
    print(f.renderText('Ping IP'))
    ipnet = input("Please enter IP: ")
    output = subprocess.check_output(['ping', '-c 4', ipnet]) 
    print(output) 
    try:
        output = subprocess.check_output(['ping', '-c 4', ipnet]) 
        if '0 received' in output: 
            print('IP unreachable') 
        else: 
            print('IP reachable') 
        print(output) 
    except: 
        print('IP unreachabless') 
    print('Pass')
    pingmain(1)



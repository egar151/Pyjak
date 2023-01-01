from pyfiglet import Figlet
import sys
import os
import pingss
import portscan

#Title for App
f = Figlet(font='standard')
os.system('clear')
print("***************************************************")
print(f.renderText('--PyJak--'))

def main():
   menu()

def menu():
    print("******************* Main Menu *********************")
    choice = input("""
A: Ping
B: Port Scan
Q: Exit

Please enter your choice: """)

    if choice == "A" or choice =="a":
        ping()
    elif choice == "B" or choice =="b":
        port()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def ping():
    os.system('clear')
    pingss.pingmain(0)
    backmenu()


def port():
    portscan.portmain()
    backmenu()

def backmenu():
    os.system('clear')
    print(f.renderText('--PyJak--'))
    menu()

main()
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
C: Tests
Q: Exit

Please enter your choice: """)

    if choice == "A" or choice =="a":
        os.system('clear')
        pingss.pingmain(0)
    elif choice == "B" or choice =="b":
        portscan.portmain()
    elif choice == "c" or choice =="C":
        submenu()
    elif choice=="Q" or choice=="q":
        quit()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
    backmenu()
    
def backmenu():
    os.system('clear')
    print(f.renderText('--PyJak--'))
    menu()


def submenu():
    f = Figlet(font='standard')
    os.system('clear')
    print("*" * 70)
    print(f.renderText('Tests Functions'))
    print("*" * 70)
    choice = input("""
A: Test Open Port
Q: Exit

Please enter your choice: """)

    if choice == "A" or choice =="a":
        iput = input("Enter Host IP: ")
        ip = [iput]
        port = int(input('Input Port: '))
        portscan.portmain(ip,port)
        backmenu()
    elif choice == "B" or choice =="b":
        port()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu() 

main()

# Hi whoever is looking at this code! Testing thingy is a file for just trying to get devcon in general to work the way I want it to
#devcon enable *keyboard*
#JUST IN CASE I DISABLE MY KEYBOARD WIHT NO BACKUP PLAN

import subprocess
import time
a = []

def checkWithWrite():
    # Define the command you want to execute
    cmd_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" hwids *hid*keyboard* > "C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\hwid_trust.txt"'

    # output = subprocess.Popen(cmd_code)

    subprocess.run(cmd_code, shell=True)
def check():
    cmd_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" hwids *hid*keyboard* > "C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon_hid.txt"'

    subprocess.run(cmd_code, shell=True)

def disableHID():
    dis_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" disable *hid*keyboard*'
    subprocess.run(dis_code, shell= True)
    print("Bye-Bye silly Keyboards \n")


def enableHID():
    en_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" enable *hid*keyboard*'
    subprocess.run(en_code, shell=True)
    print("We back with da keyboards \n")

time.sleep(10) #snoozez the program

def readFile():
    with open('hwid_trust.txt') as j:
        lines = j.readlines()
        if lines.__contains__('Name'):
            a.append(j.readline() - 1)
    print(a)
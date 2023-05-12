# Hi whoever is looking at this code! Testing thingy is a file for just trying to get devcon in general to work the way I want it to
#devcon enable *keyboard*
#JUST IN CASE I DISABLE MY KEYBOARD WIHT NO BACKUP PLAN

import subprocess
import time
import linecache
fileNon = open('CyberFinal\defend\devcon_hid.txt')
fileTrust = open('CyberFinal\defend\hwid_trust.txt', "w")

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

def readFileTrust():
    check()
    count = 0
    fileTrust.truncate(0)
    for line in fileNon.readlines():
        print(line)
        if 'Name' in line:
            fileTrust.write(linecache.getline("CyberFinal\defend\devcon_hid.txt", count))
            print('We got into this if statement!')
        count = count + 1

readFileTrust()

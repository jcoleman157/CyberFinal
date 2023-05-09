import subprocess
import time

def check():
    # Define the command you want to execute
    cmd_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" hwids *hid*keyboard* > "C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\hwid_trust.txt"'

    # output = subprocess.Popen(cmd_code)

    subprocess.run(cmd_code, shell=True)



def disableHID():
    dis_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" disable *hid*keyboard*'
    subprocess.run(dis_code, shell= True)
    print("Bye-Bye silly Keyboards \n")

disableHID()

def enableHID():
    en_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" enable *hid*keyboard*'
    subprocess.run(en_code, shell=True)
    print("We back with da keyboards \n")

time.sleep(10) #snoozez the program

enableHID()

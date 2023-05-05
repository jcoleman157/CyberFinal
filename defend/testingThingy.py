import subprocess

# Define the command you want to execute
cmd_code = '"C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\devcon" hwids *hid*keyboard* > "C:\\Users\\JColeman2023\\OneDrive - amsacs.org\\Documents\\rubberDuckyShnanaganery\\CyberFinal\\defend\\hwid_trust.txt"'

# output = subprocess.Popen(cmd_code)

subprocess.run(cmd_code, shell=True)
 
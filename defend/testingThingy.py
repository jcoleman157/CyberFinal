import subprocess

# Define the command you want to execute
devcon_command = 'devcon hwids * > hwid_trust.txt'

# Use subprocess to execute the devcon command
subprocess.Popen(devcon_command, stdout=subprocess.PIPE, shell=True)

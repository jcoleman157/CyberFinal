import subprocess

# Define the command you want to execute
devcon_command = 'devcon hwids *'

# Use subprocess to execute the devcon command
process = subprocess.Popen(devcon_command, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

# Print the output of the devcon command
print(output.decode('utf-8'))

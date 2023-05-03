import subprocess

# Define the command you want to execute
cmd_code = 'ipconfig'

# Use subprocess to execute the devcon command
output = subprocess.Popen(cmd_code, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Print the output of the devcon command
print(output)
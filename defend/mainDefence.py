# credits to, (i stole this code on stack overflow) nosklo
# https://stackoverflow.com/questions/53913408/how-to-disable-enable-a-specific-usb-port-in-windows-with-python

import subprocess
# Fetches the list of all usb devices:
result = subprocess.run(['devcon', 'hwids', '=usb'], 
    capture_output=True, text=True)

# ... add code to parse the result and get the hwid of the device you want ...

subprocess.run(['devcon', 'disable', 'HID\VID_03EB&PID_2401&REV_0100']) # to disable
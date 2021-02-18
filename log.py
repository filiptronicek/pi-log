import subprocess
import timec, netc, tempc

def run(command):
    output = subprocess.check_output(command.split(" "))
    return output.decode('unicode_escape')

tempc.check() # Check the Pi's CPU temperature
netc.check() # Check the Pi's connection
timec.check() # Check the Pi's system clock
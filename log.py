import subprocess

def run(command):
    output = subprocess.check_output(command.split(" "))
    return output.decode('unicode_escape')

print(run("python3 temp-check.py")) # Check the Pi's CPU temperature
print(run("python3 time-check.py")) # Check the Pi's system clock
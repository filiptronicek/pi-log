import subprocess

def run(command):
    output = subprocess.check_output(command.split(" "))
    return output

temp = int(run("cat /sys/class/thermal/thermal_zone0/temp"))

formattedTemp  = temp / 1000

status = "Couldn't read the temperature correctly."

if formattedTemp >= 75:
    status = "Pretty hot, the CPU could be throttled."
else:
    status = "Everything looks good!"

print(f"Your CPU temperature is {formattedTemp}. {status}")
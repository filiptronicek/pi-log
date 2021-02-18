import subprocess

def run(command):
    output = subprocess.check_output(command.split(" "))
    return output

def check():
    temp = int(run("cat /sys/class/thermal/thermal_zone0/temp"))

    formattedTemp  = temp / 1000

    status = "Couldn't read the temperature correctly."
    icon = ""

    if formattedTemp >= 75:
        status = "Pretty hot, the CPU could be throttled."
        icon = "❌"
    else:
        status = "Everything looks good!"
        icon = "✅"

    print(f"{icon} Your CPU temperature is {formattedTemp}°C. {status}")
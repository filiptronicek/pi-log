import subprocess

def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
             .decode('unicode-escape') # Perform the actual octal-escaping decode
             .encode('latin1')         # 1:1 mapping back to bytes
             .decode(encoding))        # Decode original encoding


def run(command):
    output = subprocess.check_output(command.split(" "))
    return string_escape(output)

print(run("python3 temp-check.py")) # Check the Pi's CPU temperature
print(run("python3 time-check.py")) # Check the Pi's system clock
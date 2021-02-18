from time import time_ns
import requests

print("Starting sync..")

epoch_time = int(time_ns()) / 1_000_000

syncResponce = requests.get(f"https://trnck.dev/time?ts={epoch_time}").json()
syncOffset = syncResponce['result']['ms']

status = "Something went wrong.. hmmmm"

if syncOffset == 0:
    status = "Actually WHAT?"
elif syncOffset <= 250:
    status = "The time on your system is synced very well."
elif syncOffset > 250 and syncOffset <= 750:
    status = "Everything is a-okay"
elif syncOffset >= 750:
    status = "You might want to resync" 
elif syncOffset >= 2000:
    raise RuntimeError(f"Offset too high ({syncOffset}ms). Please resync your system clock.")

print(f"Your system time offset is {syncOffset} ms. {status}")
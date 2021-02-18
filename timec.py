from time import time_ns
import requests

def check():
    runFor = 5

    def cal_average(num):
        sum_num = 0
        for t in num:
            sum_num = sum_num + t           

        avg = sum_num / len(num)
        return avg

    def getSyncOffset():
        syncs = []

        for i in range(runFor):
            epoch_time = int(time_ns()) / 1_000_000
            syncResponce = requests.get(f"https://trnck.dev/time?ts={epoch_time}").json()
            syncOffsetMs = syncResponce['result']['ms']
            syncs.append(syncOffsetMs)
        return cal_average(syncs)


    syncOffset = getSyncOffset()

    status = "Something went wrong.. hmmmm"
    icon = ""

    if syncOffset == 0:
        status = "Actually WHAT?"
        icon = "✅"
    elif syncOffset <= 250:
        status = "The time on your system is synced very well."
        icon = "✅"
    elif syncOffset > 250 and syncOffset <= 750:
        status = "Everything is a-okay"
        icon = "✅"
    elif syncOffset >= 750:
        status = "You might want to resync" 
        icon = "✅"
    elif syncOffset >= 2000:
        status = "Offset is too high. Please resync your system clock."
        icon = "❌"

    print(f"{icon} Your system time offset is {syncOffset} ms. {status}")
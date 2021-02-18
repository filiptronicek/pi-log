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
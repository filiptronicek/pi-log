# https://stackoverflow.com/questions/316866/ping-a-site-in-python

from icmplib import ping

primHostIP = '1.1.1.1'
altHostIP = '8.8.8.8'

host = ping('1.1.1.1', count=5, interval=0.05, timeout=2, privileged=False)

if host.is_alive:
    print(f'{host.address} is up meaning your connection is alive! avg_rtt={host.avg_rtt} ms')
else:
    print(f'{host.address} is dead... Trying {altHostIP}')
    altHost = ping('8.8.8.8', count=3, interval=0.05, timeout=2, privileged=False)
    if altHost.is_alive:
        print(f'{altHost.address} is reachable. Your internet is up!')
        print(f'{altHost.address} is unreachable... You are not connected')

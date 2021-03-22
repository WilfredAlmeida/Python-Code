import os
import subprocess

def ping(ip):
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
                    ['ping', '-n', '1', ip],
                    stdout=DEVNULL,  # suppress output
                    stderr=DEVNULL
                )

                return True
            except subprocess.CalledProcessError:
                return False


for i in range(1, 257):
    for j in range(1, 257):
        for k in range(1, 257):
            for l in range(1, 257):
                ip = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
                print(ip," ")

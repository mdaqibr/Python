# ❌ CPU-bound example (threading fails due to GIL):

import threading

def calculate():
    count = 0
    for _ in range(10**7):
        print("Hey!")
        count += 1

threads = []

for _ in range(4):
    t = threading.Thread(target=calculate)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
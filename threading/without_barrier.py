import threading
import time

def worker(n):
    print(f"🚀 Worker {n} started")
    time.sleep(n)
    print(f"🏁 Worker {n} done")

for i in range(1, 4):
    threading.Thread(target=worker, args=(i,)).start()
import threading
import time

def task():
    time.sleep(2)
    print("🧵 Thread task completed")

t = threading.Thread(target=task)
# t.join() # raise RuntimeError("cannot join thread before it is started")
t.start()
t.start()
t.start()

print("🔚 Main thread ends") # May print before thread finishes if you not used join().
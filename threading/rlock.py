# 🔄 What is RLock?
#   RLock = Reentrant Lock
#   Same thread can acquire the lock multiple times.
#   Useful when a function holding a lock calls another function that needs the same lock.

import threading
rlock = threading.RLock()
# 👉 Using a normal Lock here would deadlock, because the same thread tries to acquire it again.
lock = threading.Lock()

def outer():
    rlock.acquire()
    # lock.acquire()
    print("Outer acquired")
    inner()
    # lock.release()
    rlock.release()

def inner():
    rlock.acquire()
    # lock.acquire()
    print("Inner acquired")
    # lock.release()
    rlock.release()

threading.Thread(target=outer).start()
# ✅ What is a Lock?
#   A Lock allows only one thread at a time to access a critical section.

import threading

# lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100):
        print("Range:")
        # lock.acquire()
        counter += 1
        # lock.release()

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t3 = threading.Thread(target=increment)
t4 = threading.Thread(target=increment)

t1.start()
print("Final counter1:", counter)
t2.start()
print("Final counter2:", counter)
t3.start()
print("Final counter3:", counter)
t4.start()
print("Final counter4:", counter)
t1.join()
print("Final counter11:", counter)
t2.join()
print("Final counter22:", counter)
t3.join()
print("Final counter33:", counter)
t4.join()
print("Final counter44:", counter)

print("\nFinal counter:", counter)
